def add(n1,n2):
  return n1+n2
def sub(n1,n2):
  return n1-n2
def mul(n1,n2):
  return n1*n2
def div(n1,n2):
  return round(n1/n2,3)

def work(n1,n2,x):
  return eval(x)(n1,n2)
  


n1=int(input("Enter the first number: "))
n2=int(input("Enter the other number: "))
op=input("For adding type 'add',for subtracting type 'sub',for multiplying type 'mul' and for dividing type 'div': ")

ans=work(n1,n2,op)
print(f"Ans is {ans}")
st=True
while st==True:
  choice=input("Would you like to continue?.If yes type 'yes', else type 'no'")
  if choice=="yes":
      n2=int(input("Enter the other number: "))
      op=input("For adding type 'add',for subtracting type 'sub',for multiplying type 'mul' and for dividing type 'div': ")
      ans=work(ans,n2,op)
      print(f"Ans: {ans}")
  else:
    st=False


print(f"Final Ans: {ans}")