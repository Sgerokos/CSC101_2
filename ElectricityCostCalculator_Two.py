# Imports the module sys into python
import sys
# Calls a function erpk
def erpk():
        # The value hours ask's the user to input 
        # the number of hour's the device will be on in a day
        watts = float(input("Please Enter the Wattage of Your Device: "))
        
        # If less zero or less than zero 
        # the program will terminate and print exit
        if watts <= 0:    
                print("Sorry The Input Must Be Above 0.\n" 
                      "Please Try Again.\n" "Now Exiting!!!") 
                sys.exit()
                
        hours = float(input("How Many Hour's in a Day Does it Run? "))
                # If less zero or less than zero 
                # the program will terminate and print exit
        if hours <= 0:        
                print("Sorry The Input Must Be Above 0.\n" 
                      "Please Try Again.\n" "Now Exiting!!!")        
                sys.exit()   
        # The value cents_kwh ask's the user to input how 
        # much the electric rate is in cent's per kilowatt per hour                
        cents_kwh = float(input("How Much is Your Electric Rate Per" 
                                "Kilowatt an Hour in Cents? "))
        # If less zero or less than zero 
        # the program will terminate and print exit
        if cents_kwh <= 0:        
                print("Sorry The Input Must Be Above 0.\n" 
                      "Please Try Again.\n" "Now Exiting!!!")       
                sys.exit()    
        # The value monthly calculates the monthly rate 
        # by multiplying watts by the number hours divided 
        # by 1000 multiplied by cents_kwh multiplied by 30                        
        monthly = (((watts * hours) / 1000) * cents_kwh * 30)
        # Print's the monthly rate by rounding monthly to the nearest second decimal 
        print("You Will Pay Monthly $", round(monthly, 2), 
              "More on Your Electric Bill")   
        
# Calls the function made                         
erpk()