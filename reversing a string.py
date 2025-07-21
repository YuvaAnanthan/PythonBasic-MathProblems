#method 1: using slicing
string=input("Enter a string: ")
reversed_string=string[::-1]
print("The reversed string is:", reversed_string)

#method 2: using a loop
string=input("Enter a string: ")
reversed_string_loop = ""
for char in string:
    reversed_string_loop = char + reversed_string_loop
print("The reversed string using loop is:", reversed_string_loop)       

#method 3: using recursion
def reverse_string_recursive(s):    
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string_recursive(s[:-1]) 
reversed_string_recursive = reverse_string_recursive(string)
print("The reversed string using recursion is:", reversed_string_recursive)

#method 4: using the reversed() function
reversed_string_reversed = ''.join(reversed(string))
print("The reversed string using reversed() is:", reversed_string_reversed)                                                     