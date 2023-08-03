from replit import clear
#If you try this code on Replit the clear() will work

import art

#art is basically this

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


#First Part
print(art.logo)
name=input("Enter the name of the bidder: ")
amount=int(input("Enter the amount: $"))
auc_dict={}
auc_dict[name]=amount

#Definition of Auction
def auction(auc_dict,name,amount):
  auc_dict[name]=amount
  return auc_dict

#Conditional Statements
bidder=True
while bidder==True:
  choice=input("Is there another bidder,if yes, type 'yes', else print 'no': ")
  if choice=="yes":
    #Continue the Program
    clear()
    print(art.logo)
    name=input("Enter the name of the bidder: ")
    amount=int(input("Enter the amount: $"))
    auction(auc_dict,name,amount)
  else:
    #Exit the Program
    bidder=False
    person=max(auc_dict,key=lambda x: auc_dict[x])
    print(f"{person} has the highest bid with an amount of ${auc_dict[person]} ")
  

