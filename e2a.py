# e2a.py 

"""
Example code for python class.
"""

import math 

def dub(x):
    """
    doubles x
    """
    ret = x*2
    return ret

def fib(max_digits=2):
    """ 
    generate Fibonacci numbers 
    stop when size exceds passed parrameter
    """

    x1,x2 = 0,1
    while math.log(x2,10)<max_digits:
        yield x1
        x1,x2 = x2,x1+x2
    raise StopIteration

if __name__=="__main__":
    print "dub",
    if dub(3) == 6:
        print "pass"
    else:
        print "broken"

    print "fib",
    if list(fib(1)) == [0, 1, 1, 2, 3, 5]:
        print "pass"
    else:
        print "broken"


