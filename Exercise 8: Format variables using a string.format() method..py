# Exercise 8: Format variables using a string.format() method.

# Given: 
totalMoney = 1000
quantity = 3
price = 450
# Expected:
# I have 1000 dollars so I can buy 3 football for 450.00 dollars.

#{2:2f} is for having fix .00 at the end of the number.
#Don't know why it does not work in my code.
txt ="I have {0} dollars so I can buy {1} footbal for {2:2f} dollars."
print(txt.format(totalMoney, quantity, price))
