#A set is a collection which is unordered, unchangeable*, and unindexed.
# to change or update u need to convert inti list then u can do slicing and all
# duplicate not allowed in set

set_ ={'gulam',1,2,3,4}

def set_method(s):
    for n in enumerate(s):
        print(n)
    # add item
    s.add("mustafa")
    print(s)
    a=[10,20]
    s.update(a)
    print('after update',s)
    # we have all other method set method join,union,intersection etc


set_method(set_)