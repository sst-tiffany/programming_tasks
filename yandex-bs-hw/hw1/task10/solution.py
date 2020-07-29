def my_own_context_manager_decorator(wrapped):
    class example_context_manager_func:
        def __init__(self, func, *args, **kwargs):
            self.func = func
            self.args = args
            self.kwargs = kwargs

        def __enter__(self):
            self.gen = self.func(*self.args, **self.kwargs)
            return next(self.gen)

        def __exit__(self, exc_type, exc_value, tb):
            pass

    def wrapper(*args, **kwargs):
        return example_context_manager_func(wrapped, *args, **kwargs)

    return wrapper


@my_own_context_manager_decorator
def example_context_manager_func(arg1, arg2):
    try:
        print(f'enter {arg1} {arg2}')
        mananged_resource_result = arg1 + arg2
        yield mananged_resource_result
    finally:
        print('exit')


with example_context_manager_func('arg1', 'arg2') as managed_resource:
    print(managed_resource)
