#This code splits the bill with the number of ppl sharing it,with the tip you want to pay the waiter.....



bill_t=int(input("Enter the total bill: "))
n_ppl=int(input("Enter the total ppl: "))
tip=int(input("Enter the tip percentage: "))
bill_per_person=round((bill_t+bill_t*(tip/100))/n_ppl,2)
print(bill_per_person)
