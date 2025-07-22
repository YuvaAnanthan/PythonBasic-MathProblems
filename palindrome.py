#method 1: using slicing for string
string=input("Enter a string: ")
reversed_string = string[::-1]
if (reversed_string == string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")    