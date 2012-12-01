# e2a.py 

"""
Example code for python class.
"""

def dub(x):
    """
    doubles x
    """
    ret = x*2
    return ret

def fib(count):
    """ 
    generate Fibonacci numbers 
    stop when size exceds passed parrameter
    """

    x1,x2 = 0,1
    counter=0
    while counter<count:
        yield x1
        x1,x2 = x2,x1+x2
        counter += 1
    raise StopIteration

if __name__=="__main__":
    print "dub",
    if dub(3) == 6:
        print "pass"
    else:
        print "broken"

    print "fib",
    if list(fib(9)) == [0, 1, 1, 2, 3, 5, 8, 13, 21]:
        print "pass"
        print len(list(fib(9)))
    else:
        print "broken"


