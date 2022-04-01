import random;
import add

def is_win(player, opponnets):
     if (player == 'r' and opponnets == 's') or (player == 's' and opponnets == 'p') or (player == 'p' and opponnets == 'r'):
         return True;
     else:
         return False;

def play():
     # r > s , s> p , p> r
     user = input("'r' for Rock , 'p' for Paper ,'s' for Scissors :") 
     computer= random.choice(['r','p','s'])

     if computer == user :
         return "it's a tie";

     if is_win(user,computer):
        return 'You win!'

     return 'You Lost!'
print(play());


# print(add.add(4,5,4,5,7))

