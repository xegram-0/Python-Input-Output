# Exercise 5: Accept a list of 5 float numbers as an input from the user
numlist = []
index = int(input("How many: "))

for i in range(index):
    num = float(input("Enter number: "))
    numlist.append(num)
print(numlist)
