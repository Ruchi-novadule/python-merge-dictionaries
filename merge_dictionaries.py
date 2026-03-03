# Program to merge two dictionaries

dict1 = eval(input("Enter first dictionary (e.g., {'a':1, 'b':2}): "))
dict2 = eval(input("Enter second dictionary (e.g., {'c':3, 'd':4}): "))

# Merging dictionaries
dict1.update(dict2)

print("Merged Dictionary:", dict1)
