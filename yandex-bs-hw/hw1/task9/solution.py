def myown_wraps(doc_from):
    """decorator with args that copies name and docstring from wrapped to wrapper"""

    def dec_myown_wraps(wrapped):
        def doc_wrapper(*args, **kwargs):
            wrapped(*args, **kwargs)

        doc_wrapper.__name__ = doc_from.__name__
        doc_wrapper.__doc__ = doc_from.__doc__
        return doc_wrapper

    return dec_myown_wraps


def dec(wrapped):
    @myown_wraps(wrapped)
    def wrapper(*args, **kwargs):
        """wrapper docstring"""
        print('before')
        wrapped(*args, **kwargs)
        print('after')

    return wrapper


@dec
def f():
    """f docstring"""
    print('f()')


assert f.__doc__ == 'f docstring'
