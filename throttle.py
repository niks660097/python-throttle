import time
import asyncio
import functools

now_milliseconds = lambda : int(round(time.time()*1000))

def throttle(rps=50):#Requests per second, todo change it arbitrary req/time
    def decorator(func):
        count = 0
        first_req_time = None

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            nonlocal count
            nonlocal first_req_time
            if not first_req_time:
                first_req_time = now_milliseconds()
                count = 1

            if count == rps:
                diff = now_milliseconds() - first_req_time
                if diff < 1000:
                    time.sleep(1 if diff == 0 else 1 - diff/10**len(str(diff)))
                    return wrapped(*args, **kwargs)

            if now_milliseconds() - first_req_time >= 1000:
                count = 0
                first_req_time = now_milliseconds()

            count += 1
            rt_val = func(*args, **kwargs)
            return rt_val
        return wrapped
    return decorator


def async_throttle(rps=50):
    def decorator(func):
        count = 0
        first_req_time = None

        @functools.wraps(func)
        async def wrapped(*args, **kwargs):
            nonlocal count
            nonlocal first_req_time
            if not first_req_time:
                first_req_time = now_milliseconds()
                count = 1

            if count == rps:
                diff = now_milliseconds() - first_req_time
                if diff < 1000:
                    time.sleep(1 if diff == 0 else 1 - diff/10**len(str(diff)))
                    return await wrapped(*args, **kwargs)

            if now_milliseconds() - first_req_time >= 1000:
                count = 0
                first_req_time = now_milliseconds()

            count += 1
            rt_val = await func(*args, **kwargs)
            return rt_val
        return wrapped
    return decorator
