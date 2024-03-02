'''
To practice the use of nested shorthand if statements in assisting a shopping decision.

Task 1: Code Correction

You are provided with a Python script that is supposed to assist in shopping,
 but it has errors. Identify and fix them.

Buggy Code:
'''

weather = input("Enter the weather sunny, rainy, or cold: ")
clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather == "rainy" else "sweater"
print(clothing)