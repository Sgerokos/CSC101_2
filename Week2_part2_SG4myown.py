# The value watts ask's the user to input the number of watts the device use's

watts = float(input("Please Enter the Wattage of Your Device: "))

# Ask's the user if the input was correct y for Yes n for No

yes_No = input((" The Device's Wattage is", watts, "Correct? Type y for Yes or n for No"))

if (yes_No == "n"):
    
    # Re ask's the user for the input
    
    watts = float(input("Please Enter the Wattage of Your Device: "))
    
    # The value hours ask's the user to input the number of hour's the device will be on in a day
    
    hours = float(input("How Many Hour's in a Day Does it Run? "))
    
    # The value cents_kwh ask's the user to input how much the electric rate is in cent's per kilowatt per hour
    
    cents_kwh = float(input("How Much is Your Electric Rate Per Kilowatt an Hour in Cents? "))
    
    # The value monthly calculates the monthly rate by multiplying watts by the number hours divided by 1000 multiplied by cents_kwh multiplied by 30
    
    monthly = (((watts * hours) / 1000) * cents_kwh * 30)
    
    # Print's the monthly rate by rounding monthly to the nearest second decimal 
    
    print("You Will Pay Monthly $", round(monthly, 2), "More on Your Electric Bill")    

# If not No it will continue from here

else:    

    # Re ask's the user for the input

    hours = float(input("How Many Hour's in a Day Does it Run? "))
    
    # Ask's the user if the input was correct y for Yes n for No
    
    yes_No = input((" The Device Will be Running for", hours, "in a Day Correct? Type y for Yes or n for No"))
    
    if (yes_No == "n"):
        
        # Re ask's the user for the input
        
        hours = float(input("Please Re-Enter How Many Hour's in a Day Does it Run? "))
        
        # The value cents_kwh ask's the user to input how much the electric rate is in cent's per kilowatt per hour
        
        cents_kwh = float(input("How Much is Your Electric Rate Per Kilowatt an Hour in Cents? "))
        
        # The value monthly calculates the monthly rate by multiplying watts by the number hours divided by 1000 multiplied by cents_kwh multiplied by 30
        
        monthly = (((watts * hours) / 1000) * cents_kwh * 30)
        
        # Print's the monthly rate by rounding monthly to the nearest second decimal 
        
        print("You Will Pay Monthly $", round(monthly, 2), "More on Your Electric Bill")  
        
    # If not No it will continue from here
    
    else:
    
        # The value cents_kwh ask's the user to input how much the electric rate is in cent's per kilowatt per hour

        cents_kwh = float(input("How Much is Your Electric Rate Per Kilowatt an Hour in Cents? "))
        
        # Ask's the user if the input was correct y for Yes n for No
        
        yes_No = input((" Your Electric Rate Per Kilowatt an Hour is", cents_kwh, "Correct? Type y for Yes or n for No"))
        
        if (yes_No == "n"): 
            
            # Re ask's the user for the input
            
            cents_kwh = float(input("Please Re-Enter Your Electric Rate Per Kilowatt an Hour in Cents? "))
            
            # The value monthly calculates the monthly rate by multiplying watts by the number hours divided by 1000 multiplied by cents_kwh multiplied by 30
                        
            monthly = (((watts * hours) / 1000) * cents_kwh * 30)
            
            # Print's the monthly rate by rounding monthly to the nearest second decimal 
            
            print("You Will Pay Monthly $", round(monthly, 2), "More on Your Electric Bill")            

        # If not No it will continue from here
        
        else:
            
            # The value monthly calculates the monthly rate by multiplying watts by the number hours divided by 1000 multiplied by cents_kwh multiplied by 30
            
            monthly = (((watts * hours) / 1000) * cents_kwh * 30)

            # Print's the monthly rate by rounding monthly to the nearest second decimal 

            print("You Will Pay Monthly $", round(monthly, 2), "More on Your Electric Bill")
