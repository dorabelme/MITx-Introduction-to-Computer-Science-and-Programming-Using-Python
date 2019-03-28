def applyToEach(L, abs):
    for i in range(len(L)):
        L[i] = f(L[i])
 

applyToEach(testlist, abs)



 def inc(a):
    return a + 1
    
applyToEach(testList, inc)


def square(a):
    return a * a
    
applyToEach(testList, square)
