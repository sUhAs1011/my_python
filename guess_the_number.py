
import random

num=random.randint(0,100)


def choi_easy(num,choi):
  num_found=False
  if choi=='easy':
    num_attempts=10
  else:
    num_attempts=5
  while num_attempts>0 & num_found==False:
    print(f"You have {num_attempts} left")
    user_num=int(input("Make Guess: "))
    if user_num==num:
      print(f"Hurray!!,You got it correct. The number was {num}.")
      break
    elif user_num<num:
      print("Too Low")
    else:
      print("Too High")
    num_attempts=num_attempts-1
  if num_attempts==0:
    print(f"Game Over, You Lost, the number was {num}")




print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 100.")
choi=input("Choose a difficulty. Type 'hard' or 'easy': ")
choi_easy(num,choi)



  