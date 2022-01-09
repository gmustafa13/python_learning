#inmutable data type hance we can update it 
# index based so we have slicing and indexing
#inbuild method

t = (10,20,30,40)

def tuple_method(t):
    for n in enumerate(t):
        print('for loop',n)
    #slicing
    print(t[:4])
    print(t[::-1]) # reverse
    print(t[::2]) # every secound element
    print(t[-3:-1])

# tuple_method(t)

t1 = ("gulam",10,20,30,"mustafa")

def update_tuple(t1):
    #its unmutable to change it u need to convert into list
    x = list(t1)
    x[0] = "gulam__"
    t1 = tuple(x)
    print(t1) 
    # add item
    x = list(t1)
    x.append("new")
    print(x)
    x.insert(200,'hu')
    print(x)
    t1 = tuple(x)
    print('last tuple',t1)
    # destructring of tuple
    (gulam,a,b,c,*d) = t1
    print(gulam,a,b,c,d)

    t2 =(1,2,34,5)
    t3 = t1+t2
    print(t3)

update_tuple(t1)