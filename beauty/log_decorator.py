import logging

logging.basicConfig()

def logged(func, *args, **kwargs):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    def new_func(*args, **kwargs):
        logger.debug('calling {func_name} with args {args} and kwargs {kwargs}'.format(
        	func_name=func.__name__, args=args, kwargs=kwargs))
        return func(*args, **kwargs)
    return new_func

# logging.getLogger().setLevel(logging.DEBUG)

@logged
def sxn():
	print('I am in sxn.')

if __name__ == '__main__':
	sxn()