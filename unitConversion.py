# The variable feet ask's the user to input the number for feet

feet = float(input("Please Enter the Value for Feet: "))

# The variable meters multiplies the number of feet by 0.305

meters = feet * 0.305

# The variable inch multiplies feet by 12 to calculate inches

inch = feet * 12

# The variable centimetre multiplies inch by 0.3937 to calculate centimetre

centimetre = inch * 0.3937


#Print's the output feet and show's it's conversion in meter's as well

print(feet, "Feet Are", meters, "In Meters", inch, "In Inches", centimetre, "In Centimetres")
