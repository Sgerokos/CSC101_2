# Prints a hello and welcomes the user to doner match
print("Hello")
print("Welcome to the Donor Match Program")

# Requests the user to input the type of blood they have 
# The input can be A+. A-, B+, B-, O+, O-, AB+, AB-
blood_Type = input("\nPlease Input The Donor's Blood Type." 
                   "You May Enter A+, A-, B+, B-, O+, O-, AB+, AB-: ")

# This line will ask for the recipient's blood type
recipient_Blood_type = input("\nPlease Input The Recipient's Blood Type." 
                         "You May Enter A+, A-, B+, B-, O+, O-, AB+, AB-: ")

# If the user chooses one of the selected blood types 
# The user will be asked to input the recipient's blood type
if (blood_Type == "A+") and (recipient_Blood_type == "A+" 
                             or recipient_Blood_type ==  "AB+"):
    print(blood_Type, "And", recipient_Blood_type, "Are Compatable")  

    
elif (blood_Type == "A+") and (recipient_Blood_type == "A-" or recipient_Blood_type == "B+" 
                               or recipient_Blood_type == "B-" 
                               or recipient_Blood_type == "O+" 
                               or recipient_Blood_type == "O-" 
                               or recipient_Blood_type ==  "AB-"):
    print(blood_Type, "And", recipient_Blood_type, "Are Not Compatable") 
        
elif (blood_Type == "A-") and (recipient_Blood_type == "A+" 
                               or recipient_Blood_type ==  "A-" 
                               or recipient_Blood_type ==  "AB+" 
                               or recipient_Blood_type ==  "AB-"):
        print(blood_Type, "And", recipient_Blood_type, "Are Compatable") 
    
        
elif (blood_Type == "A-") and (recipient_Blood_type == "B+" 
                               or recipient_Blood_type == "B-" 
                               or recipient_Blood_type == "O+" 
                               or recipient_Blood_type == "O-"):
        print(blood_Type, "And", recipient_Blood_type, "Are Not Compatable")        

elif (blood_Type == "B+") and (recipient_Blood_type == "B+"  
                               or recipient_Blood_type ==  "AB-"):
        print(blood_Type, "And", recipient_Blood_type, "Are Compatable") 
    
        
elif (blood_Type == "B+") and (recipient_Blood_type == "A+" 
                               or recipient_Blood_type == "A-" 
                               or recipient_Blood_type == "B-" 
                               or recipient_Blood_type == "O+" 
                               or recipient_Blood_type == "O-" 
                               or recipient_Blood_type == "AB-"):
        print(blood_Type, "And", recipient_Blood_type, "Are Not Compatable") 


elif (blood_Type == "B-") and (recipient_Blood_type == "B+" 
                               or recipient_Blood_type ==  "B-" 
                               or recipient_Blood_type ==  "AB+" 
                               or recipient_Blood_type ==  "AB-"):
        print(blood_Type, "And", recipient_Blood_type, "Are Compatable") 
            
elif (blood_Type == "B-") and (recipient_Blood_type == "A+" 
                               or recipient_Blood_type == "A-" 
                               or recipient_Blood_type == "O+" 
                               or recipient_Blood_type == "O-"):
        print(blood_Type, "And", recipient_Blood_type, "Are Not Compatable") 

elif (blood_Type == "O+") and (recipient_Blood_type == "A+" 
                               or recipient_Blood_type ==  "B+" 
                               or recipient_Blood_type ==  "O+" 
                               or recipient_Blood_type ==  "AB+"):
        print(blood_Type, "And", recipient_Blood_type, "Are Compatable") 
            
elif (blood_Type == "O+") and (recipient_Blood_type == "A-" 
                               or recipient_Blood_type == "B-" 
                               or recipient_Blood_type == "O-" 
                               or recipient_Blood_type == "AB-"):
        print(blood_Type, "And", recipient_Blood_type, "Are Not Compatable") 

elif (blood_Type == "O-") and (recipient_Blood_type == "A+" 
                               or recipient_Blood_type ==  "A-" 
                               or recipient_Blood_type ==  "B+" 
                               or recipient_Blood_type ==  "B-" 
                               or recipient_Blood_type ==  "AB+" 
                               or recipient_Blood_type ==  "AB-"):
        print(blood_Type, "And", recipient_Blood_type, "Are Compatable") 
            
elif (blood_Type == "AB+") and (recipient_Blood_type ==  "AB+"):
        print(blood_Type, "And", recipient_Blood_type, "Are Compatable") 
            
elif (blood_Type == "AB+") and (recipient_Blood_type == "A+" 
                                or recipient_Blood_type ==  "A-" 
                                or recipient_Blood_type == "B+" 
                                or recipient_Blood_type == "B-" 
                                or recipient_Blood_type == "O+" 
                                or recipient_Blood_type == "O-" 
                                or recipient_Blood_type == "AB-"):
        print(blood_Type, "And", recipient_Blood_type, "Are Not Compatable")   
    
elif (blood_Type == "AB-") and (recipient_Blood_type ==  "AB-" 
                                or recipient_Blood_type ==  "AB-"):
        print(blood_Type, "And", recipient_Blood_type, "Are Compatable") 
            
elif (blood_Type == "AB-") and (recipient_Blood_type == "A+" 
                                or recipient_Blood_type == "A-" 
                                or recipient_Blood_type == "B+" 
                                or recipient_Blood_type == "B-" 
                                or recipient_Blood_type == "O+" 
                                or recipient_Blood_type == "O-"):
        print(blood_Type, "And", recipient_Blood_type, "Are Not Compatable")  
        
# If anything besides the listed blood types is typed in
# An error message will print and will explain to the user what to type in         
else:
    print("You Have Entered" 
          "\nDonor's Blood Type:", blood_Type, 
          "\nAnd Recipient's Blood Type:", recipient_Blood_type, 
          "\nThis is an Improper Input." 
          "\nPlease Enter One of The Selections Listed A+, A-, O+, O-, AB+, AB-" 
          "\nFor The Donor and Recipient")