from functools import reduce
def add(*numbers):
    data = reduce(lambda x,y: x+y ,numbers )
    print(f"bsdk  {data}")
    return data


# print(add(1,2,4,5,5,5,5,5))