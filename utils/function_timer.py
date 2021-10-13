from functools import wraps
import time

def func_timer(func):
    """
    装饰器实现函数计时
    """
    @wraps(func)
    def function_timer(*args, **kwargs):
        print(f'Function: {func.__name__} start ...')
        t0 = time.time()
        result = func(*args, **kwargs)
        spent_time = time.time() - t0
        print(f'Function: {func.__name__} finished, spent time: {spent_time*1e6:.2f}microseconds\n')
        return result
    return function_timer
