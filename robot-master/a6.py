	
##I ran across this thread when searching for a timeout call on unit tests. I didn't find anything simple in the answers or 3rd party packages so I wrote the decorator below you can drop right into code:

import multiprocessing.pool
import functools

def timeout(max_timeout):
    """Timeout decorator, parameter in seconds."""
    def timeout_decorator(item):
        """Wrap the original function."""
        @functools.wraps(item)
        def func_wrapper(*args, **kwargs):
            """Closure for function."""
            pool = multiprocessing.pool.ThreadPool(processes=1)
            async_result = pool.apply_async(item, args, kwargs)
            # raises a TimeoutError if execution exceeds max_timeout
            return async_result.get(max_timeout)
        return func_wrapper
    return timeout_decorator


@timeout(5.0)  # if execution takes longer than 5 seconds, raise a TimeoutError
def test_base_regression(self):
    print ('hello')
