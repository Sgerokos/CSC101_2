import sys

# Prints a hello and welcomes the user to doner match
print("Hello")
print("Welcome to the Donor Match Program")

# Requests the user to input the type of blood they have 
# The input can be A+. A-, B+, B-, O+, O-, AB+, AB-
blood_Type = input("\nPlease Input The Donor's Blood Type." 
                   "You May Enter A+, A-, B+, B-, O+, O-, AB+, AB-: ")

if blood_Type != "A+" or blood_Type != "A-" or \
   blood_Type != "B+" or blood_Type != "B-" or \
   blood_Type != "O+" or blood_Type != "O-" or \
   blood_Type != "AB+" or blood_Type != "AB-":
    print("Incorrect input. Enter one of A+, A-, B+, B-, O+, O-, AB+, AB-")
    sys.exit()

# This line will ask for the recipient's blood type
recipient_Blood_type = input("\nPlease Input The Recipient's Blood Type." 
                         "You May Enter A+, A-, B+, B-, O+, O-, AB+, AB-: ")

if recipient_Blood_type != "A+" or recipient_Blood_type != "A-" or \
   recipient_Blood_type != "B+" or recipient_Blood_type != "B-" or \
   recipient_Blood_type != "O+" or recipient_Blood_type != "O-" or \
   recipient_Blood_type != "AB+" or recipient_Blood_type != "AB-":
    print("Incorrect input. Enter one of A+, A-, B+, B-, O+, O-, AB+, AB-")
    sys.exit()

if (blood_Type == "A+") and (recipient_Blood_type == "A+" 
                             or recipient_Blood_type ==  "AB+"):
    print(blood_Type, "And", recipient_Blood_type, "Are Compatable")  
  
elif (blood_Type == "A-") and (recipient_Blood_type == "A+" 
                               or recipient_Blood_type ==  "A-" 
                               or recipient_Blood_type ==  "AB+" 
                               or recipient_Blood_type ==  "AB-"):
        print(blood_Type, "And", recipient_Blood_type, "Are Compatable") 
    
elif (blood_Type == "B+") and (recipient_Blood_type == "B+"  
                               or recipient_Blood_type ==  "AB-"):
        print(blood_Type, "And", recipient_Blood_type, "Are Compatable")

elif (blood_Type == "B-") and (recipient_Blood_type == "B+" 
                               or recipient_Blood_type ==  "B-" 
                               or recipient_Blood_type ==  "AB+" 
                               or recipient_Blood_type ==  "AB-"):
        print(blood_Type, "And", recipient_Blood_type, "Are Compatable") 
            
elif (blood_Type == "O+") and (recipient_Blood_type == "A+" 
                               or recipient_Blood_type ==  "B+" 
                               or recipient_Blood_type ==  "O+" 
                               or recipient_Blood_type ==  "AB+"):
        print(blood_Type, "And", recipient_Blood_type, "Are Compatable") 
            
elif (blood_Type == "O-") and (recipient_Blood_type == "A+" 
                               or recipient_Blood_type ==  "A-" 
                               or recipient_Blood_type ==  "B+" 
                               or recipient_Blood_type ==  "B-" 
                               or recipient_Blood_type ==  "AB+" 
                               or recipient_Blood_type ==  "AB-"):
        print(blood_Type, "And", recipient_Blood_type, "Are Compatable") 
            
elif (blood_Type == "AB+") and (recipient_Blood_type ==  "AB+"):
        print(blood_Type, "And", recipient_Blood_type, "Are Compatable") 
            
    
elif (blood_Type == "AB-") and (recipient_Blood_type ==  "AB-" 
                                or recipient_Blood_type ==  "AB-"):
        print(blood_Type, "And", recipient_Blood_type, "Are Compatable") 
            
      
# If anything besides the listed blood types is typed in
# An error message will print and will explain to the user what to type in         
else:
    print("Blood types are not compatible.")