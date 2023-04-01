# Imports the sys package into python
import sys

# Welcome's the user to the establiment
print("Hello Welcome to Tru Astoria")
print("\nWhat Would You Enjoy Today?")

# This variable is the tax 8.75%
sales_Tax = 0.0875
# The price is 0 but will be changed as the loop continue's or end's
price = 0
# anything_Else will be set to Y till the user change's it in line 270
anything_Else = "Y"
# variable order will be set as an empty string till all selections are made
order = ""
# As long as anything_Else is Y the loop will continue from here
while anything_Else == "Y":
    
    # Ask's the user to input a number for one of the items
    burger_Sandwiches_Wraps = int(input("Please Choose \n1 For Tru Burger"
                                        "\n2 For Classic Cheeseburger,"
                                        "\n3 For Salmon Burger,"
                                        "\n4 For Vegetable Panini,"
                                        "\n5 For Greek Roast Chicken Panini,"
                                        "\n6 For Fried Chicken Sandwich,"
                                        "\n7 For Cubano,"
                                        "\n8 For Falafel Wrap"
                                        "\n9 For Grilled Chicken Wrap,"
                                        "\n10 For Turkey Avocado BLT:"))    
     
    # If the input is below 1 or above 10 an error message will print   
    if burger_Sandwiches_Wraps < 1 or burger_Sandwiches_Wraps > 10:
        print("You have Inputed an Invalid Number For Burgers, Sandwiches," 
              "and Wraps."
              "\nPlease Enter a number Between 1 - 10 For This Selection")        
    
    # If 1 is selected the the item will be displayed  
    elif burger_Sandwiches_Wraps == 1:
        
        print("Tru Burger - sautéed onions, roasted red pepper, bacon," 
              "\nSwiss cheese, sriracha maple mayo, brioche bun." 
              "\nThis is $18.72")
        
        # The user will be asked if they want to add this to the order
        y_N = input("Do You Want to Add This to Your order? "
                              "Y For Yes N For No: ")
        
        # If Y is selected the price will be added to the variable price
        # The order variable will be added to the variable order
        if y_N == "Y":
            price += 18.72
            order += "\nTru Burger: $18.72"
        
        # If N is selected no price will be added to the price variable
        # order variable will remain as it did before
        elif y_N == "N":
            order += ""
            
    # If 2 is selected the the item will be displayed                                                     
    elif burger_Sandwiches_Wraps == 2:     
        
        print("Classic Cheeseburger - Lettuce, tomato, onion," 
              "and American cheese on brioche bun." 
              "\nThis is $16.64")
        
        # The user will be asked if they want to add this to the order
        y_N = input("Do You Want to Add This to Your order? "
                              "Y For Yes N For No: ")
        
        # If Y is selected the price will be added to the variable price
        # The order variable will be added to the variable order
        if y_N == "Y":
            price += 16.64
            order += "\nClassic Cheeseburger: $16.64"
        
        # If N is selected no price will be added to the price variable
        # order variable will remain as it did before
        elif y_N == "N":
            order += ""        
        
    # If 3 is selected the the item will be displayed                                                             
    elif burger_Sandwiches_Wraps == 3:
        
        print("Salmon Burger" 
              "- char-grilled wild-caught Atlantic salmon burger with a" 
              "\nsignature Worcestershire sauce, shredded cabbage," 
              "\nand mustard aioli." 
              "\nThis is $19.76")
        
        # The user will be asked if they want to add this to the order
        y_N = input("Do You Want to Add This to Your order? "
                              "Y For Yes N For No: ")
        
        # If Y is selected the price will be added to the variable price
        # The order variable will be added to the variable order
        if y_N == "Y":
            price += 19.76
            order += "\nSalmon Burger: $19.76"
        
        # If N is selected no price will be added to the price variable
        # order variable will remain as it did before
        elif y_N == "N":
            order += ""           
    
    # If 4 is selected the the item will be displayed                                                       
    elif burger_Sandwiches_Wraps == 4:
        
        print("Vegetable Panini - farmers pick of fresh grilled," 
              "\nvegetables, sun dried tomato aioli on a pressed Italian roll." 
              "\nThis is $15.60")
        
        # The user will be asked if they want to add this to the order
        y_N = input("Do You Want to Add This to Your order? "
                              "Y For Yes N For No: ")
        
        # If Y is selected the price will be added to the variable price
        # The order variable will be added to the variable order
        if y_N == "Y":
            price += 15.60
            order += "\nVegetable Panini: $15.60"
        
        # If N is selected no price will be added to the price variable
        # order variable will remain as it did before
        elif y_N == "N":
            order += ""           
    
    # If 5 is selected the the item will be displayed                                                                                                            
    elif burger_Sandwiches_Wraps == 5:
        
        print("Greek Roast Chicken Panini - breaded chicken breast,"
              "\namerican cheese, guacamole spread, tomatoes," 
              "\nhoney mustard, on a brioche. " 
              "\nThis is $17.68")
        
        # The user will be asked if they want to add this to the order
        y_N = input("Do You Want to Add This to Your order? "
                              "Y For Yes N For No: ")
        
        # If Y is selected the price will be added to the variable price
        # The order variable will be added to the variable order
        if y_N == "Y":
            price += 17.68
            order += "\nGreek Roast Chicken Panini: $17.68"
        
        # If N is selected no price will be added to the price variable
        # order variable will remain as it did before
        elif y_N == "N":
            order += ""           
    
    # If 6 is selected the the item will be displayed                    
    elif burger_Sandwiches_Wraps == 6:
        
        print("Fried Chicken Sandwich - breaded chicken breast, american cheese," 
              "\nguacamole spread, tomatoes, honey mustard, on a brioche. "
              "\nThis is $17.68")
        
        # The user will be asked if they want to add this to the order
        y_N = input("Do You Want to Add This to Your order? "
                              "Y For Yes N For No: ")
        
        # If Y is selected the price will be added to the variable price
        # The order variable will be added to the variable order
        if y_N == "Y":
            price += 17.68
            order += "\nFried Chicken Sandwich: $17.68"
        
        # If N is selected no price will be added to the price variable
        # order variable will remain as it did before
        elif y_N == "N":
            order += ""           
        
    # If 7 is selected the the item will be displayed                                                       
    elif burger_Sandwiches_Wraps == 7:
        
        print("Cubano - pulled pork, deli ham," 
              "Swiss cheese, pickles, and mustard."
              "\nThis is $17.68")
        
        # The user will be asked if they want to add this to the order
        y_N = input("Do You Want to Add This to Your order? "
                              "Y For Yes N For No: ")
        
        # If Y is selected the price will be added to the variable price
        # The order variable will be added to the variable order
        if y_N == "Y":
            price += 17.68
            order += "\nCubano: $17.68"
        
        # If N is selected no price will be added to the price variable
        # order variable will remain as it did before
        elif y_N == "N":
            order += ""   
            
    # If 8 is selected the the item will be displayed                                                      
    elif burger_Sandwiches_Wraps == 8:
        
        print("Falafel Wrap - hummus, tabbouleh, tahini sauce," 
              "rugula, falafel fritters."
              "\nThis is $16.64")
        
        # The user will be asked if they want to add this to the order
        y_N = input("Do You Want to Add This to Your order? "
                              "Y For Yes N For No: ")
        
        # If Y is selected the price will be added to the variable price
        # The order variable will be added to the variable order
        if y_N == "Y":
            price += 16.64
            order += "\nFalafel Wrap: $16.64"
        
        # If N is selected no price will be added to the price variable
        # order variable will remain as it did before
        elif y_N == "N":
            order += ""           
    
    # If 9 is selected the the item will be displayed                
    elif burger_Sandwiches_Wraps == 9:
        
        print("Grilled Chicken Wrap - roasted sliced turkey, Swiss cheese, bacon," 
              "\nromaine hearts, sliced tomato, avocado," 
              "sriracha mayo, on toasted wheat bread."
              "\nThis is $16.64")
        # The user will be asked if they want to add this to the order
        y_N = input("Do You Want to Add This to Your order? "
                              "Y For Yes N For No: ")
        
        # If Y is selected the price will be added to the variable price
        # The order variable will be added to the variable order
        if y_N == "Y":
            price += 16.64
            order += "\nGrilled Chicken Wrap: $16.64"
        
        # If N is selected no price will be added to the price variable
        # order variable will remain as it did before
        elif y_N == "N":
            order += ""           
        
    # If 10 is selected the the item will be displayed                
    elif burger_Sandwiches_Wraps == 10:
        
        print("Turkey Avocado BLT - roasted sliced turkey, Swiss cheese, bacon," 
              "\nromaine hearts, sliced tomato, avocado," 
              "\nsriracha mayo, on toasted wheat bread." 
              "\nThis is $18.72")
        
        # The user will be asked if they want to add this to the order
        y_N = input("Do You Want to Add This to Your order? "
                              "Y For Yes N For No: ")
        
        # If Y is selected the price will be added to the variable price
        # The order variable will be added to the variable order
        if y_N == "Y":
            price += 18.72
            order += "\nTurkey Avocado BLT : $18.72"
        
        # If N is selected no price will be added to the price variable
        # order variable will remain as it did before
        elif y_N == "N":
            order += ""           
        
    # This variable will change line 15 look at line 14
    anything_Else = input("Would You Like Something Else? \
        \nPlease Enter Y For Yes or N For No:")
    
    # If N is selected the folowing will be used        
    if anything_Else == "N":
            
            # Variable's used
            # Tax will be calculated by price times sales_Tax
            tax = price * sales_Tax
            
            # Total will add price and tax
            total = price + tax
            
            # This is 10% tip, total time's 10%
            ten_Tip = total * 0.10
            
            # This is 15% tip, total time's 15%
            fifteen_Tip = total * 0.15
            
            # This is 20% tip, total time's 20%
            twenty_tip = total * 0.20
            
            #order -= order + order
            # This will print total along with the sale's tax  
            # As well as the recomended tip's and then exit
            print("Order's:", order, "\nTotal Without Tax", price,
                  "\nThe Total With Tax is:", round(total, 2), 
                  "\nThe Sale's Tax 8.75% is:", round(tax, 2), 
                  "\n10% Tip is:", round(ten_Tip, 2), 
                  "15% Tip is:", round(fifteen_Tip, 2), 
                  "20% Tip is:", round(twenty_tip, 2))
            sys.exit()
                  
    # If a anything besides Y or N is selected an error message will be printed        
    elif anything_Else != "N" or anything_Else != "Y":
        print("Bad Input", anything_Else)
