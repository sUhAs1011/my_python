rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper,2 for Scissors.: "))
comp_choice=random.randint(0,2)
print("Your Choice: ")
if choice==0:
  print(rock)
elif choice==1:
  print(paper)
elif choice==2:
  print(scissors)
else:
  print("Invalid Entry")

print("Computer chose")
if comp_choice==0:
  print(rock)
elif comp_choice==1:
  print(paper)
elif comp_choice==2:
  print(scissors)
else:
  print("Invalid Entry")

if comp_choice==0:
  if choice==0:
    print("It is a draw")
  elif choice==1:
    print("You Win!!!")
  else:
    print("You Loose")
elif comp_choice==1:
  if choice==0:
    print("You Loose")
  elif choice==1:
    print("It is a draw")
  else:
    print("You Win!!!")
else:
  if choice==0:
    print("You Win!!!")
  elif choice==1:
    print("You Loose")
  else:
    print("It is a draw")
  
  

