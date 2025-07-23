#method 1: using slicing for string
string=input("Enter a string: ")
reversed_string = string[::-1]
if (reversed_string == string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")    

#method 2:using number
def num_palindrome(n):
    return str(n) == str(n)[::-1]
   
num = int(input("Enter a number: "))
if num_palindrome(num):
    print(f" {num} The number is a palindrome.")
else:
    print(f"{num} The number is not a palindrome.")    
