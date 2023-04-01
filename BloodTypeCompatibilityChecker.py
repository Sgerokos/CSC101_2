# Prints a hello and welcomes the user to doner match
print("Hello")
print("Welcome to the Donor Match Program")

# Requests the user to input the type of blood they have 
# The input can be A+. A-, B+, B-, O+, O-, AB+, AB-
blood_Type = input("\nPlease Input The Donor's Blood Type." 
                   "You May Enter A+, A-, B+, B-, O+, O-, AB+, AB-: ")


# If the user chooses one of the selected blood types 
# The user will be asked to input the recipient's blood type
if blood_Type == ("A+"):
    print("\nYou Input A+.")
    
    # This line will ask for the recipient's blood type
    recipient_Blood_type = input("\nPlease Input The Recipient's Blood Type." 
                             "You May Enter A+, A-, B+, B-, O+, O-, AB+, AB-: ")
    
    # Once the recipient's blood type is entered 
    # it will print if it is compatable or not lines 22-44 will determine this
    if recipient_Blood_type == ("A+"):
        print("A+ And A+ Are Compatable")
    
    elif recipient_Blood_type == ("A-"):
        print("A+ And A- Are Not Compatable")
        
    elif recipient_Blood_type == ("B+"):
        print("A+ And B+ Are Not Compatable")
        
    elif recipient_Blood_type == ("B-"):
        print("A+ And B- Are Not Compatable")
        
    elif recipient_Blood_type == ("O+"):
        print("A+ And O+ Are Not Compatable")
    
    elif recipient_Blood_type == ("O-"):
        print("A+ And O- Are Not Compatable")
        
    elif recipient_Blood_type == ("AB+"):
        print("A+ And AB+ Are Compatable")        
        
    elif recipient_Blood_type == ("AB-"):
        print("A+ And AB- Are Not Compatable")
    
    # If anything besides the listed blood types is typed in 
    # An error message will print and will explain to the user what to type in   
    else:
        print("Sorry Wrong Input Please Input A+, A-, B+, B-, O+, O-, AB+, AB-")
        
elif blood_Type == ("A-"):
    print("\nYou Input A-.")
    
    # This line will ask for the recipient's blood type
    recipient_Blood_type = input("\nPlease Input The Recipient's Blood Type." 
                             "You May Enter A+, A-, B+, B-, O+, O-, AB+, AB-: ")
    
    # Once the recipient's blood type is entered 
    # it will print if it is compatable or not lines 60-82 will determine this    
    if recipient_Blood_type == ("A+"):
        print("A- And A+ Are Compatable")
    
    elif recipient_Blood_type == ("A-"):
        print("A- And A- Are Compatable")
        
    elif recipient_Blood_type == ("B+"):
        print("A- And B+ Are Not Compatable")
        
    elif recipient_Blood_type == ("B-"):
        print("A- And B- Are Not Compatable")
        
    elif recipient_Blood_type == ("O+"):
        print("A- And O+ Are Not Compatable")
    
    elif recipient_Blood_type == ("O-"):
        print("A- And O- Are Not Compatable")
        
    elif recipient_Blood_type == ("AB+"):
        print("A+ And AB+ Are Compatable")        
        
    elif recipient_Blood_type == ("AB-"):
        print("A+ And AB- Are Compatable")
    
    # If anything besides the listed blood types is typed in 
    # An error message will print and will explain to the user what to type in         
    else:
        print("Sorry Wrong Input Please Input A+, A-, B+, B-, O+, O-, AB+, AB-")    
    
    
elif blood_Type == ("B+"):
    print("\nYou Input B+.")
    
    # This line will ask for the recipient's blood type
    recipient_Blood_type = input("\nPlease Input The Recipient's Blood Type." 
                             "You May Enter A+, A-, B+, B-, O+, O-, AB+, AB-: ")
    
    # Once the recipient's blood type is entered 
    # it will print if it is compatable or not lines 97-119 will determine this    
    if recipient_Blood_type == ("A+"):
        print("B+ And A+ Are Not Compatable")
    
    elif recipient_Blood_type == ("A-"):
        print("B+ And A- Are Not Compatable")
        
    elif recipient_Blood_type == ("B+"):
        print("B+ And B+ Are Compatable")
        
    elif recipient_Blood_type == ("B-"):
        print("B+ And B- Are Not Compatable")
        
    elif recipient_Blood_type == ("O+"):
        print("B+ And O+ Are Not Compatable")
    
    elif recipient_Blood_type == ("O-"):
        print("B+ And O- Are Not Compatable")
        
    elif recipient_Blood_type == ("AB+"):
        print("B+ And AB+ Are Compatable")        
        
    elif recipient_Blood_type == ("AB-"):
        print("B+ And AB- Are Not Compatable")
    
    # If anything besides the listed blood types is typed in 
    # An error message will print and will explain to the user what to type in         
    else:
        print("Sorry Wrong Input Please Input A+, A-, B+, B-, O+, O-, AB+, AB-")    
    
elif blood_Type == ("B-"):
    print("\nYou Input B-.")
    
    # This line will ask for the recipient's blood type
    recipient_Blood_type = input("\nPlease Input The Recipient's Blood Type." 
                             "You May Enter A+, A-, B+, B-, O+, O-, AB+, AB-: ")
    
    # Once the recipient's blood type is entered 
    # it will print if it is compatable or not lines 133-155 will determine this    
    if recipient_Blood_type == ("A+"):
        print("B- And A+ Are Not Compatable")
    
    elif recipient_Blood_type == ("A-"):
        print("B- And A- Are Not Compatable")
        
    elif recipient_Blood_type == ("B+"):
        print("B- And B+ Are Compatable")
        
    elif recipient_Blood_type == ("B-"):
        print("B- And B- Are Compatable")
        
    elif recipient_Blood_type == ("O+"):
        print("B- And O+ Are Not Compatable")
    
    elif recipient_Blood_type == ("O-"):
        print("B- And O- Are Not Compatable")
        
    elif recipient_Blood_type == ("AB+"):
        print("B- And AB+ Are Compatable")        
        
    elif recipient_Blood_type == ("AB-"):
        print("B- And AB- Are Compatable")
    
    # If anything besides the listed blood types is typed in 
    # An error message will print and will explain to the user what to type in         
    else:
        print("Sorry Wrong Input Please Input A+, A-, B+, B-, O+, O-, AB+, AB-")     
     
    
elif blood_Type == ("O+"):
    print("\nYou Input O+.")
    
    # This line will ask for the recipient's blood type
    recipient_Blood_type = input("\nPlease Input The Recipient's Blood Type." 
                             "You May Enter A+, A-, B+, B-, O+, O-, AB+, AB-: ")
    
    # Once the recipient's blood type is entered 
    # it will print if it is compatable or not lines 170-195 will determine this    
    if recipient_Blood_type == ("A+"):
        print("O+ And A+ Are Compatable")
    
    elif recipient_Blood_type == ("A-"):
        print("O+ And A- Are Not Compatable")
        
    elif recipient_Blood_type == ("B+"):
        print("O+ And B+ Are Compatable")
        
    elif recipient_Blood_type == ("B-"):
        print("O+ And B- Are Not Compatable")
        
    elif recipient_Blood_type == ("O+"):
        print("O+ And O+ Are Compatable")
    
    elif recipient_Blood_type == ("O-"):
        print("O+ And O- Are Not Compatable")
        
    elif recipient_Blood_type == ("AB+"):
        print("O+ And AB+ Are Compatable")        
        
    elif recipient_Blood_type == ("AB-"):
        print("O+ And AB- Are Not Compatable")
    
    # If anything besides the listed blood types is typed in 
    # An error message will print and will explain to the user what to type in         
    else:
        print("Sorry Wrong Input Please Input A+, A-, B+, B-, O+, O-, AB+, AB-")      
    
    
elif blood_Type == ("O-"):
    print("\nYou Input O-.")
    
    # This line will ask for the recipient's blood type
    recipient_Blood_type = input("\nPlease Input The Recipient's Blood Type." 
                             "You May Enter A+, A-, B+, B-, O+, O-, AB+, AB-: ")
    
    # Once the recipient's blood type is entered 
    # it will print if it is compatable or not lines 207-229 will determine this    
    if recipient_Blood_type == ("A+"):
        print("O- And A+ Are Compatable")
    
    elif recipient_Blood_type == ("A-"):
        print("O+ And A- Are Compatable")
        
    elif recipient_Blood_type == ("B+"):
        print("O- And B+ Are Compatable")
        
    elif recipient_Blood_type == ("B-"):
        print("O- And B- Are Compatable")
        
    elif recipient_Blood_type == ("O+"):
        print("O- And O+ Are Compatable")
    
    elif recipient_Blood_type == ("O-"):
        print("O- And O- Are Compatable")
        
    elif recipient_Blood_type == ("AB+"):
        print("O- And AB+ Are Compatable")        
        
    elif recipient_Blood_type == ("AB-"):
        print("O- And AB- Are Compatable")
    
    # If anything besides the listed blood types is typed in 
    # An error message will print and will explain to the user what to type in         
    else:
        print("Sorry Wrong Input Please Input A+, A-, B+, B-, O+, O-, AB+, AB-")      
    

elif blood_Type == ("AB+"):
    print("\nYou Input AB+.")
    
    # This line will ask for the recipient's blood type
    recipient_Blood_type = input("\nPlease Input The Recipient's Blood Type." 
                             "You May Enter A+, A-, B+, B-, O+, O-, AB+, AB-: ")
    
    # Once the recipient's blood type is entered 
    # it will print if it is compatable or not lines 244-266 will determine this    
    if recipient_Blood_type == ("A+"):
        print("AB+ And A+ Are Not Compatable")
    
    elif recipient_Blood_type == ("A-"):
        print("AB+ And A- Are Not Compatable")
        
    elif recipient_Blood_type == ("B+"):
        print("AB+ And B+ Are Not Compatable")
        
    elif recipient_Blood_type == ("B-"):
        print("AB+ And B- Are Not Compatable")
        
    elif recipient_Blood_type == ("O+"):
        print("AB+ And O+ Are Not Compatable")
    
    elif recipient_Blood_type == ("O-"):
        print("AB+ And O- Are Not Compatable")
        
    elif recipient_Blood_type == ("AB+"):
        print("AB+ And AB+ Are Compatable")        
        
    elif recipient_Blood_type == ("AB-"):
        print("AB+ And AB- Are Not Compatable")
    
    # If anything besides the listed blood types is typed in 
    # An error message will print and will explain to the user what to type in         
    else:
        print("Sorry Wrong Input Please Input A+, A-, B+, B-, O+, O-, AB+, AB-")      
    
   
elif blood_Type == ("AB-"):
    print("\nYou Input AB-.")
    
    # This line will ask for the recipient's blood type
    recipient_Blood_type = input("\nPlease Input The Recipient's Blood Type." 
                             "You May Enter A+, A-, B+, B-, O+, O-, AB+, AB-: ")
    
    # Once the recipient's blood type is entered 
    # it will print if it is compatable or not lines 281-303 will determine this    
    if recipient_Blood_type == ("A+"):
        print("AB- And A+ Are Not Compatable")
    
    elif recipient_Blood_type == ("A-"):
        print("AB- And A- Are Not Compatable")
        
    elif recipient_Blood_type == ("B+"):
        print("AB- And B+ Are Not Compatable")
        
    elif recipient_Blood_type == ("B-"):
        print("AB- And B- Are Not Compatable")
        
    elif recipient_Blood_type == ("O+"):
        print("AB- And O+ Are Not Compatable")
    
    elif recipient_Blood_type == ("O-"):
        print("AB- And O- Are Not Compatable")
        
    elif recipient_Blood_type == ("AB+"):
        print("AB- And AB+ Are Compatable")        
        
    elif recipient_Blood_type == ("AB-"):
        print("AB- And AB- Are Compatable")
    
    # If anything besides the listed blood types is typed in 
    # An error message will print and will explain to the user what to type in         
    else:
        print("Sorry Wrong Input Please Input A+, A-, B+, B-, O+, O-, AB+, AB-")      
    
# If anything besides the listed blood types is typed in
# An error message will print and will explain to the user what to type in         
else:
    print("You Have Entered An Improper Blood Type." 
          "\nPlease Enter One of The Selections Listed A+, A-, O+, O-, AB+, AB-")