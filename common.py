import inspect

def checkargs(function):
    def _f(*arguments):
        for index, argument in enumerate(inspect.getfullargspec(function)[0]):
            if not isinstance(arguments[index], function.__annotations__[argument]):
                raise TypeError("{} is not of type {}".format(arguments[index], function.__annotations__[argument]))
        return function(*arguments)
    _f.__doc__ = function.__doc__
    return _f
