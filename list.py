#define list [] it may contain string,number
#list hv update,delete,indexing,order,slicing

l = [10,20,30,'gulam']
#type check it have list calss
print(type(l))
for index,v in enumerate(l):
    print(index,v)

# indexing and slicing
def index_slice(l):
   # 1 for from left to right  -1 for right to left
   print(l[0], l[-1])
   #slicing
   print(l[0:3] , ' in revarse ',l[::-1])
   print(l[-2:])

   # append will add elemnt in last
   l.append('mustafa')
   print(l)

   #to add multiple elemnt 
   l.extend([10,20,2,3])
   print(l)
   #insert u can add by passing index
   l.insert(1,3000)
   print(l)

   #for copy 
   l2 = l.copy()

# index_slice(l)

def update_delete(l):
    #pop() removed element based on index
    #remove() removed element based on value
    #clear() all the element
    #del() remove element/memory
    #sort() it will sort not return new array it will modefy og list
    #reverse() modify org list
    #sorted() return new sorted list
    #count() number of occurancy
    # for sort and sorted only one data type should be there else it will throuh error
    print(l.pop(1))
    print(l)
    print(l.remove('gulam'),l.remove('mustafa'))
    print(l)
    l.sort()  #does not have return value
    print("after sort() ",l)
    print(sorted(l))
    print(l.reverse()) # it will change og list
    print(l)
    l.clear()
    print(l)
    del(l)
    # print(l)

# update_delete(l)
