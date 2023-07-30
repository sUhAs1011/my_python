#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill_t=int(input("Enter the total bill: "))
n_ppl=int(input("Enter the total ppl: "))
tip=int(input("Enter the tip percentage: "))
bill_per_person=round((bill_t+bill_t*(tip/100))/n_ppl,2)
print(bill_per_person)
