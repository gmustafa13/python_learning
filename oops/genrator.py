'''genrator is used for handel infine data of stream '''

def genrator():
    n= 1
    print(f"first print 1 {n}")
    yield

    n +=n
    print(f"first print 2 {n}")
    yield

a =genrator()
next(a)
next(a)