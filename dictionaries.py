# dict. stored data in key value paired , key name should not repeat 
# order , changable allow indexing , slicing ,update etc

dictionary = {
    'name':'gulam',
    'age':28,
    'gender':'male'
}
# print(dictionary)

def dict_(d):
    print(d.keys())
    print(d.values())
    print(d.get('name'))
    print('list of tuple',d.items())
    #accessing

    d['phn'] =9987780051
    d.update({'name':'gulam_'})
    print(d)
    
    #pop will remove based on key whwre as popitems remove last key value
    d.pop('phn')
    print(d)

    d.popitem()
    print(d)

    #copy 
    copy_ = d.copy()
    print(copy_)
    newCopy_ = dict(d)
    print(newCopy_)

    for n in d.keys():
        print(d[n])

dict_(dictionary)
