# Imports the module sys into python

import sys

# Ask's the user to input the first side of the triangle

a = float(input("Please Enter The First Side of The Triangle: "))

# Ask's the user to input the second side of the triangle

b = float(input("Please Enter The Second Side of The Triangle: "))

# Ask's the user to input the third side of the triangle

c = float(input("Please Enter The Third Side of The Triangle: "))

# System exit's if the sum of two is less than the third

if a + b < c:
    
    print("Two Sides Are Less Than The Third Please Try Again.\n" "Now Exeting!!!")
    
    sys.exit()

# System exit's if the sum of two is less than the third

if a + c < b:
    
    print("Two Sides Are Less Than The Third Please Try Again.\n" "Now Exeting!!!")
    
    sys.exit()    

# System exit's if the sum of two is less than the third

if b + c < a:
    
    print("Two Sides Are Less Than The Third Please Try Again.\n" "Now Exeting!!!")
    
    sys.exit()

# Add the sum of the three sides and display the perimeter for the user

else:
    
    p = a + b + c
    
    print("The Perimeter is", p)