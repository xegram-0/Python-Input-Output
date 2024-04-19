# Exercise 7: Accept any three string from one input() call
"""
name1=""
name2=""
name3=""
name1, name2, name3 = input("Enter 3 strings: ").split()
print("We have these names:", name1,name2,name3)
"""

num = int(input("How many names: "))
names = []

for i in range(num):
    names.append(input("Enter a name: "))

#print(names)
for name in names:
    print("Name is", name)