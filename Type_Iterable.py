
"""
SOURCE:

    http://stackoverflow.com/questions/1952464/in-python-how-do-i-determine-if-an-object-is-iterable


DESCRIPTION:

    This implements what is known as a 
        `Duck typing`

    Does it quack?
    Does it look like a duck?

        
ARGS:
    IterableCandidate
        Description:
            The object of which to check if it is an iterable python object

RETURNS:
    True on iterable
    False on NOT iterable


"""

def Main(
    IterableCandidate = None
    ):

    Result = None

    try:
        iterator = iter(IterableCandidate)
    except TypeError:
        # not iterable
        Result = False
    else:
        # iterable
        Result = True

    return Result


