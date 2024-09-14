print("Welcome to the tip calculator!")

#read bill amount
bill = float(input("What was the total bill? $"))

#read tip amount
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
#tip calculation
tip = (bill * tip) / 100

#actual bill amount calculation
bill += tip

people = int(input("How many people to split the bill? "))

#split the bill
splitedBill = bill / people
final_amount = round(splitedBill, 2)
print(f"Each person should pay: ${final_amount}")