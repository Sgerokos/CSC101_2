# The variable lbs ask's the user to input the weight in pounds

lbs = float(input("Please Enter Weight to be Converted in Pounds: "))

# The variable kgs is set to the variable lbs multiplied by 0.454 to calculate the output

kgs = lbs * 0.454

# Print's the output in kilograms and rounds it to the 3rd decimal number

print("The Wight in Kilograms is", round(kgs, 3), ("kgs"))

