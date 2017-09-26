# Throttle
Throttle execution of a python co-routine or function.

Usage

```
async def test_throttle():
    current_id = 0
    @async_throttle(rps=50)
    async def foo():
        nonlocal current_id
        current_id += 1
        print('CURRENT ID', current_id)
    tasks = [[foo() for i in range(500)] for j in range(10)]
    for gather_ind, t in enumerate(tasks):
        res = await asyncio.gather(*t)
```
