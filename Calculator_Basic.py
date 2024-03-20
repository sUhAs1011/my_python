logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

#art
print(logo)

#functions for different operators
def add(n1,n2):
  return n1+n2
def sub(n1,n2):
  return n1-n2
def mul(n1,n2):
  return n1*n2
def div(n1,n2):
  return round(n1/n2,3)
def power(n1,n2):
  return n1**n2

#Callback
def work(n1,n2,x):
  return eval(x)(n1,n2)
  

#input statements for the start
n1=float(input("Enter the first number: "))
n2=float(input("Enter the other number: "))
op=input("For adding type 'add',for subtracting type 'sub',for multiplying type 'mul' and for dividing type 'div': ")

ans=work(n1,n2,op)
print(f"Ans is {ans}")


#This will work if the person wants to do more operations only.
st=True
while st==True:
  choice=input("Would you like to continue?.If yes type 'yes', else type 'no': ")
  if choice=="yes":
      n2=float(input("Enter the other number: "))
      op=input("For adding type 'add',for subtracting type 'sub',for multiplying type 'mul' and for dividing type 'div': ")
      ans=work(ans,n2,op)
      print(f"Ans: {ans}")
  else:
    st=False


print(f"Final Ans: {ans}")