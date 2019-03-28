def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here

    s = min(a,b)
    for i in range(s,0,-1):
        if a % i == 0 and b % i == 0:
            return i

assert(gcdIter(2,12) == 2)
assert(gcdIter(6,12) == 6)
assert(gcdIter(9,12) == 3)
assert(gcdIter(17,12) == 1)
