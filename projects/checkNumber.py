import random

# lowerLimit = input("prime Number Lower limit : ")
# upperLimit = input("prime Number upperlimit : ")
# def primeNumberInrange(lowerLimit,upperLimit):
#     primeList=[]
#     for num in range(lowerLimit,upperLimit+1):
#         if(num%2 != 0):
#             primeList.append(num)
#     print(f'prime number between {lowerLimit} - {upperLimit} : {primeList}')

# primeNumberInrange(int(lowerLimit),int(upperLimit))


def guessTheNumber(x):
    random_number = random.randint(1,x)
    guess =0 
    while guess != random_number:
        guess = int(input(f'guess the number between 1-{x} : '))
        if guess > random_number:
            print('Sorry , guess again ,Too high')
        elif guess < random_number:
             print('Sorry , guess again ,Too low')
    print(f'Yay , you Guess the correct number {random_number} !!')

guessTheNumber(10)