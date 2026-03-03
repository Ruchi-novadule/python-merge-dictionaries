🔗 Merge Two Dictionaries in Python

This Python program merges two dictionaries provided by the user into a single dictionary.

📌 Features

Takes dictionary input from user

Uses built-in update() method

Simple and clean implementation

Beginner-friendly

Interview-ready logic

💻 Technology Used

Python 3

🚀 How It Works

The program takes two dictionary inputs from the user.

Uses the update() method to merge the second dictionary into the first.

Prints the final merged dictionary.

📝 Code
# Program to merge two dictionaries

dict1 = eval(input("Enter first dictionary (e.g., {'a':1, 'b':2}): "))
dict2 = eval(input("Enter second dictionary (e.g., {'c':3, 'd':4}): "))

dict1.update(dict2)

print("Merged Dictionary:", dict1)
▶️ Example

Input:

{'a':1, 'b':2}
{'c':3, 'd':4}

Output:

Merged Dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


🎯 Learning Concepts

Dictionaries in Python

Dictionary methods

User input handling

Data structures
