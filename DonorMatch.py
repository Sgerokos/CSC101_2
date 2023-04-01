# Prints a hello and welcomes the user to doner match
print("Hello")
print("Welcome to the Doner Match Program")

# Requests the user to input the type of blood they have 
# The input can be A+. A-, B+, B-, O+, O-, AB+, AB-
blood_Type = input("\nPlease Input Your Blood Type." 
                   "You May Enter A+, A-, B+, B-, O+, O-, AB+, AB-: ")

# If the user chooses one of the selected blood types 
# 3 new selections will be offered
# The Selecions are 1, 2, 3 
# giving either facts, choosing to give, or recieve blood respectfully
# The selections are given in the lines bellow for each type
if blood_Type == ("A+"):
    print("\nYou Input A+.")

    # This line is the info and the selections 1, 2, 3    
    info = int(input("What Would You Like to Know About This Blood Type?"
                     "\nInput 1 For Fact's, 2 to Give Blood, 3 to Recieve Blood:"))
    
    # If 1 is selected fact's about the blood type is printed
    if info == 1:
        print("You Have Requested 1 For Fact's")
        print("1 in 3 People are Blood Type A+." 
              "\nThis Blood Type is One of The Most Common Blood Types.")
    
    # If 2 is selected the types this blood type can give to will print
    elif info == 2:
        print("You Have Requested 2 to Give Blood")
        print("You Can Give to Anyone With A+, and AB+")
    
    # If 3 is selected the types this blood type can recieve from will be printed   
    elif info == 3:
        print("You Have Requested 3 to Recieve Blood")
        print("You Can Recieve From Anyone With A+, A-, O+, O-")
    
    # If anything besides 1, 2, or 3 is selected an error message will print out
    # This message will tell the user why they are getting this error
    else:
        print("Sorry Wrong Input Please Input 1, 2, or 3 For This Selection")
        
if blood_Type == ("A-"):
    print("\nYou Input A-.")
    
    # This line is the info and the selections 1, 2, 3            
    info = int(input("What Would You Like to Know About This Blood Type?"
                    "\nInput 1 For Fact's, 2 to Give Blood, 3 to Recieve Blood:"))
    
    # If 1 is selected fact's about the blood type is printed        
    if info == 1:
        print("You Have Requested 1 For Fact's")
        print("Only 1 in 16 Have Blood Type A-")
     
    # If 2 is selected the types this blood type can give to will print       
    elif info == 2:
        print("You Have Requested 2 to Give Blood")
        print("You Can Give to Anyone With A, and AB Regardless of" 
              "\nThem Being Negative or Positive")
    
    # If 3 is selected the types this blood type can recieve from will be printed            
    elif info == 3:
        print("You Have Requested 3 to Recieve Blood")
        print("You Can Recieve From Anyone With A-, O-")
    
    # If anything besides 1, 2, or 3 is selected an error message will print out
    # This message will tell the user why they are getting this error                
    else:
        print("Sorry Wrong Input Please Input 1, 2, or 3 For This Selection")
        
if blood_Type == ("B+"):
    print("\nYou Input B+.")
    
    # This line is the info and the selections 1, 2, 3          
    info = int(input("What Would You Like to Know About This Blood Type?"
                    "\nInput 1 For Fact's, 2 to Give Blood, 3 to Recieve Blood:"))
    
    # If 1 is selected fact's about the blood type is printed        
    if info == 1:
        print("You Have Requested 1 For Fact's")
        print("Around 9% of The Population Has Blood Type B+")
    
    # If 2 is selected the types this blood type can give to will print        
    elif info == 2:
        print("You Have Requested 2 to Give Blood")
        print("You Can Give to Anyone With B+, and AB+.")
    
    # If 3 is selected the types this blood type can recieve from will be printed            
    elif info == 3:
        print("You Have Requested 3 to Recieve Blood")
        print("You Can Recieve From Anyone With B+, B-, O+, O-")
        
    # If anything besides 1, 2, or 3 is selected an error message will print out
    # This message will tell the user why they are getting this error                
    else:
        print("Sorry Wrong Input Please Input 1, 2, or 3 For This Selection")
        
if blood_Type == ("B-"):
    print("\nYou Input B-.")
     
    # This line is the info and the selections 1, 2, 3                   
    info = int(input("What Would You Like to Know About This Blood Type?"
                    "\nInput 1 For Fact's, 2 to Give Blood, 3 to Recieve Blood:"))
    
    # If 1 is selected fact's about the blood type is printed                
    if info == 1:
        print("You Have Requested 1 For Fact's")
        print("Less Than 2% of The Population Has Blood Type B-")
    
    # If 2 is selected the types this blood type can give to will print                
    elif info == 2:
        print("You Have Requested 2 to Give Blood")
        print("You Can Give to Anyone With B, and AB Regardless of"
              "Them Being Negative or Positive")
    
    # If 3 is selected the types this blood type can recieve from will be printed                    
    elif info == 3:
        print("You Have Requested 3 to Recieve Blood")
        print("You Can Recieve From Anyone With B+, B-, O+, O-")
        
    # If anything besides 1, 2, or 3 is selected an error message will print out
    # This message will tell the user why they are getting this error                        
    else:
        print("Sorry Wrong Input Please Input 1, 2, or 3 For This Selection")
        
if blood_Type == ("O+"):
    print("\nYou Input O+.")
    
    # This line is the info and the selections 1, 2, 3                    
    info = int(input("What Would You Like to Know About This Blood Type?"
                    "\nInput 1 For Fact's, 2 to Give Blood, 3 to Recieve Blood:"))
    
    # If 1 is selected fact's about the blood type is printed                
    if info == 1:
        print("You Have Requested 1 For Fact's")
        print("O+ is Given to Patients More Than Any Other Blood Type,"
              "\nThis is Why O+ is Considered The Most Needed Blood Type")
        print("\n38% of The Population Has O+ Blood," 
              "\nThis Makes it The Most Common Blood type")
        print("\nO+ is Not universaly Compatible to All types," 
              "\nBut They Are Compatable to Any Red Blood Cells" 
              "\nThat Are Positive A+, B+, O+, AB+")
        print("\nOver 80% of The Population Has positive Blood Types" 
              "\nAnd Can Receive O+." 
              "\nThis is Another reason it is in Such High Demand.")
        print("\nO+ Donors Who Are CMV Negative Are Known as," 
              "\nHeroes For Babies at The Red Cross Because it is"
              "\nThe Safest Blood For Transfusions For Immune Deficient Newborns")
        print("\nIn Major traumas With Massive Blood Loss, Many Hospitals" 
              "\nTransfuse O+ Blood, Even if The Patient's Blood is Unknown." 
              "\nThe Risk of Reaction is Much Lower in Ongoing Blood loss" 
              "\nSituations and O+ is More Available Than O-."
              "\nType O+ Blood is Critical in Trauma Care")
        print("\nType O+ Blood is One of The first To Run Out During"
              "\na Shortage Due to It's high Demand.")
        print("\nO+ is Not Universaly Compatable But Are Compatable to" 
              "All Positive types")
    
    # If 2 is selected the types this blood type can give to will print                
    elif info == 2:
        print("You Have Requested 2 to Give Blood")
        print("You Can Give to Anyone With A+, B+, O+, and AB+.")
    
    # If 3 is selected the types this blood type can recieve from will be printed                    
    elif info == 3:
        print("You Have Requested 3 to Recieve Blood")
        print("You Can Recieve From Anyone With O+, or O-")
    
    # If anything besides 1, 2, or 3 is selected an error message will print out
    # This message will tell the user why they are getting this error                        
    else:
        print("Sorry Wrong Input Please Input 1, 2, or 3 For This Selection")
                
if blood_Type == ("O-"):
    print("\nYou Input O-.")
    
    # This line is the info and the selections 1, 2, 3                            
    info = int(input("What Would You Like to Know About This Blood Type?"
                    "\nInput 1 For Fact's, 2 to Give Blood, 3 to Recieve Blood:"))
    
    # If 1 is selected fact's about the blood type is printed                        
    if info == 1:
        print("You Have Requested 1 For Fact's")
        print("O- is The Most Common Blood Type Used For Transfusions"
              "\nWhen The Blood Type is Unknown."
              "\nThis is Why it is Used most Often in Cases of Trauma,"
              "\nEmergencies, Surgeries, And Any Situation Where Blood Type is"
              "is Unknown."
              "O- is The universal Blood Type")
        print("O- Can Only Receive O- Blood")
        print("\nO- Donors Who Are CMV Negative Are Known as," 
              "\nHeroes For Babies at The Red Cross Because it is"
              "\nThe Safest Blood For Transfusions For Immune Deficient Newborns")
        print("\nOnly 7% of The Population have O- Blood Type.," 
              "\nDue to The Versatility For O- Transfusions, it is in High Demand."
              "\nIn an Emergency, it is The Blood Product of Choice."
              "\nA good Example is, Just One Car Accident Victim"
              "\nCan Require up to 100 Units of O-."
              "\nMeeting The Demand For O- Blood is Always a Priority")   
        print("\nO- is The First Blood Supply to Run Out"
              "\nDuring a Shortage Due to It's universality")
    
    # If 2 is selected the types this blood type can give to will print                        
    elif info == 2:
        print("You Have Requested 2 to Give Blood")
        print("You Can Give to Anyone Blood Type Regardless"
            "Them Being Negative or Positive")
    
    # If 3 is selected the types this blood type can recieve from will be printed                            
    elif info == 3:
        print("You Have Requested 3 to Recieve Blood")
        print("You Can Recieve From Anyone With O-")
    
    # If anything besides 1, 2, or 3 is selected an error message will print out
    # This message will tell the user why they are getting this error                                
    else:
        print("Sorry Wrong Input Please Input 1, 2, or 3 For This Selection")
        
if blood_Type == ("AB+"):
    print("\nYou Input AB+.")
    
    # This line is the info and the selections 1, 2, 3                                    
    info = int(input("What Would You Like to Know About This Blood Type?"
                    "\nInput 1 For Fact's, 2 to Give Blood, 3 to Recieve Blood:"))
    
    # If 1 is selected fact's about the blood type is printed                                
    if info == 1:
        print("You Have Requested 1 For Fact's")
        print("Less Than 4% of The U.S. population Have AB+")
    
    # If 2 is selected the types this blood type can give to will print                                
    elif info == 2:
        print("You Have Requested 2 to Give Blood")
        print("You Can Give to AB+ Only")
    
    # If 3 is selected the types this blood type can recieve from will be printed                                    
    elif info == 3:
        print("You Have Requested 3 to Recieve Blood")
        print("You Can Recieve Blood From All Blood Types")
    
    # If anything besides 1, 2, or 3 is selected an error message will print out
    # This message will tell the user why they are getting this error                                        
    else:
        print("Sorry Wrong Input Please Input 1, 2, or 3 For This Selection")
        
if blood_Type == ("AB-"):
    print("\nYou Input AB-.")
    
    # This line is the info and the selections 1, 2, 3                                            
    info = int(input("What Would You Like to Know About This Blood Type?"
                        "\nInput 1 For Fact's, 2 to Give Blood, 3 to Recieve Blood:"))
    
    # If 1 is selected fact's about the blood type is printed                                        
    if info == 1:
        print("You Have Requested 1 For Fact's")
        print("Less Than 1% of The U.S. population Have AB-" 
        "\nBlood, Making it The Least Common Blood Type Among Americans.")
    
    # If 2 is selected the types this blood type can give to will print                                        
    elif info == 2:
        print("You Have Requested 2 to Give Blood")
        print("You Can Give to AB-, and AB+ Blood Types")
    
    # If 3 is selected the types this blood type can recieve from will be printed                                            
    elif info == 3:
        print("You Have Requested 3 to Recieve Blood")
        print("You Can Recieve From Anyone With Negative Blood Types"
            "\nThis Includes A-, B-, O-, AB-")
    
    # If anything besides 1, 2, or 3 is selected an error message will print out
    # This message will tell the user why they are getting this error                                                
    else:
        print("Sorry Wrong Input Please Input 1, 2, or 3 For This Selection")

# If anything besides A+, A-, O+, O-, AB+, AB- is selected an error message will print out
# This message will tell the user why they are getting this error        
else:
    print("You Have Entered An Improper Blood Type." 
          "\nPlease Enter One of The Selections Listed A+, A-, O+, O-, AB+, AB-")