# Request's the user to input the employee's name

employees_Name = input("Please Enter The Employee's Name: ")

# Request's the user to input number of hours the employee worked

hrs_Worked = float(input("Please Enter Thr Number of Hours Worked in a Week: "))

# If the hour's are zero or less than zero a message will prompt telling the user wrong input

if hrs_Worked <= 0:
   
    print("Sorry You Have Entered a Wrong Input")

# If a number above zero is entered the program will continue 

else:        

    pay_Rate = float(input("Please Enter Hourly Pay Rate: "))
    
    # If the pay rate is zero or less than zero a message will prompt telling the user wrong input
    
    if pay_Rate <= 0:
       
        print("Sorry You Have Entered a Wrong Input") 
   
   # If a number above zero is entered the program will continue      
    
    else:         

        fed_Tax = float(input("Please Enter Federal Tax Withholding Rate: "))
        
        # If the federal tax is zero or less than zero a message will prompt telling the user wrong input
        
        if fed_Tax <= 0:
           
            print("Sorry You Have Entered a Wrong Input") 
            
        # If a number above zero is entered the program will continue 
         
        else:   
            
            state_Tax = float(input("Please Enter State Tax Withholding Rate: "))
            
            # If the state tax is zero or less than zero a message will prompt telling the user wrong input
            
            if state_Tax <= 0:
               
                print("Sorry You Have Entered a Wrong Input") 
            
            # If a number above zero is entered the program will continue 
            
            else:               
                
                # Calculates the gross pay by multiplying hours worked by pay rate
                
                gross_Pay = hrs_Worked * pay_Rate
                
                # Calculates the federal withholdings by multiplying gross pay by federal tax

                fed_With = gross_Pay * fed_Tax
                
                # Calculates the sate withholdings by multiplying gross pay by state tax

                state_With = gross_Pay * state_Tax
                
                # Calculates the total deductions by adding the state withholdings and the federal withholdings

                total_Deduc = state_With + fed_With
                
                # Calculates the bet pay by subtracting gross pay by total deductions

                net_Pay = gross_Pay - total_Deduc
                
                # Print's the result's for the user to see the \t is an escape key used for indenting

                print("The Employee's Name is:", employees_Name)

                print("The Number of Hours Worked is: $", round(hrs_Worked, 2))

                print("The Employee's Pay Rate is: $", round(pay_Rate, 2))

                print("The Federal Tax Withholding Rate is: $", round(fed_Tax, 2))
    
                print("The State Tax is: $", round(state_Tax, 2))

                print("Deductions Are:") 

                print("\t Federal Withholding: $", round(fed_With, 2))
        
                print("\t State Withholding: $", round(state_With, 2))

                print("\t Total Deduction: $", round(total_Deduc, 2))

                print("Net Pay: $", round(net_Pay, 2))