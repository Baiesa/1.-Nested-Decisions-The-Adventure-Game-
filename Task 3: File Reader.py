'''
Ask the user for a filename to read. 
Try to open and read the file. If the file doesn't exist,
use the pass statement to handle the error silently.
'''

filename = input("Enter the filename to read: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    pass