# Throttle
Throttling execution of a python function.

Usage
from throttle import throttle

```
@throttle(rps=5)
def foo(*args, **kwargs):
    print("LIMITED RESOURCE")
