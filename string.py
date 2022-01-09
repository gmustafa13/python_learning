# whrite a program those number whitch is divisable by 7 & 5 between range 1500
# l =[]
# for value in range(1,1501):
#     if (value%7 == 0) and (value%5 == 0):
#         l.append(value)
#         print(value)
#     else:
#         print('not found')

# print('list witch is divisable by 7 and 5',l)


def string_methods(s):
    print('id of string ',id(s))
    print('printing first 5 character ',s[:6])
    print('every secound charater this is called stride  ',s[::2])
    print('reverse string this is called stride :: notation   ',s[::-1])
    print('print every secound charachter in reverse order  ',s[::-2])
    # string itration
    for value in s:
        print(value)

    # itrar over every secound cahracher
    for value in s[::2]:
        print(value)    

# string_methods('gulam mustafa')

def build_in_str_fn(s1,v1,v2):
    # to see build in function type help(str) or print(dir(str))
    # foramat() => infinite arrgument it will assign first value to first variable
    print("the value of v1 is {} and v2 is {}".format(v1,v2))
    # u can assign by index
    print("the value of v2 is {1} and v1 is {0}".format(v1,v2))
    # or we can assign value by variable
    print("the value of v2 is {m1} and v1 is {m2}".format(m1=v1, m2=v2))

    #capitalized first char of string
    print(s1.capitalize())
    #upper
    #lower
    #title will change 1st char in upper of every word

    print(s1.upper())
    print(s1.title())
    
    # isupper() check whether string is in upper case or not based on that it will return true or false

build_in_str_fn("gulam mustafa",100,200)


