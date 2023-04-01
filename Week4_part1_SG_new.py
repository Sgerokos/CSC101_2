import sys

# Welcome's the user to the establiment
print("Hello Welcome to Tru Astoria")
print("\nWhat Would You Enjoy Today?")

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
sales_Tax = 0.0875
price = 0
#total = price
# Line's 18 - 22 are the selection's that the user will choose from
# The choice selected will print out what the item is and the price

while burger_Sandwiches_Wraps < 10 or burger_Sandwiches_Wraps > 1:
    
    if burger_Sandwiches_Wraps < 1 or burger_Sandwiches_Wraps > 10:
#else:
        print("You have Inputed an Invalid Number For Burgers, Sandwiches," 
        "and Wraps."
        "\nPlease Enter a number Between 1 - 10 For This Selection")      
    
    elif burger_Sandwiches_Wraps == 1:
        price += 18.72
        
        print("Tru Burger - sautéed onions, roasted red pepper, bacon," 
            "\nSwiss cheese, sriracha maple mayo, brioche bun." 
            "This is $18.72")
                                                   
    elif burger_Sandwiches_Wraps == 2:     
        price += 16.64
        
        print("Classic Cheeseburger - Lettuce, tomato, onion," 
            "and American cheese on brioche bun." 
            "This is $16.64") 
                                                         
    elif burger_Sandwiches_Wraps == 3:
        price += 19.76
        
        print("Salmon Burger" 
            "- char-grilled wild-caught Atlantic salmon burger with a" 
            "\nsignature Worcestershire sauce, shredded cabbage," 
            "\nand mustard aioli. This is $19.76")
                                                   
    elif burger_Sandwiches_Wraps == 4:
        
        price += 15.60
        
        print("Vegetable Panini - farmers pick of fresh grilled," 
            "\nvegetables, sun dried tomato aioli on a pressed Italian roll." 
            "This is $15.60")
                                                        
                                                        
    elif burger_Sandwiches_Wraps == 5:
        
        price += 17.68
        
        print("Greek Roast Chicken Panini - breaded chicken breast,"
            "\namerican cheese, guacamole spread, tomatoes," 
            "\nhoney mustard, on a brioche. " 
            "\nThis is $17.68")
                
    elif burger_Sandwiches_Wraps == 6:
        
        price += 17.68
        
        print("Fried Chicken Sandwich - breaded chicken breast, american cheese," 
            "\nguacamole spread, tomatoes, honey mustard, on a brioche. "
            "\nThis is $17.68")            
                                                   
    elif burger_Sandwiches_Wraps == 7:
        
        price += 17.68
        
        print("Cubano - pulled pork, deli ham," 
            "Swiss cheese, pickles, and mustard."
            "\nThis is $17.68")
                                                   
    elif burger_Sandwiches_Wraps == 8:
        
        price += 16.64
        
        print("Falafel Wrap - Bhummus, tabbouleh, tahini sauce," 
            "rugula, falafel fritters."
            "\nThis is $16.64")
            
    elif burger_Sandwiches_Wraps == 9:
        
        price += 16.64
        
        print("Grilled Chicken Wrap - roasted sliced turkey, Swiss cheese, bacon," 
            "\nromaine hearts, sliced tomato, avocado," 
            "sriracha mayo, on toasted wheat bread."
            "\nThis is $16.64")        
            
    elif burger_Sandwiches_Wraps== 10:
        
        price += 18.72
        
        print("Turkey Avocado BLT - roasted sliced turkey, Swiss cheese, bacon," 
            "\nromaine hearts, sliced tomato, avocado," 
            "\nsriracha mayo, on toasted wheat bread." 
            "\nThis is $18.72")
    
    anything_Else = input("Would You Like Something Else? \
        #\nPlease Enter Y For Yes or N For No:")
    
    if anything_Else == "Y":
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
        
        if burger_Sandwiches_Wraps < 1 or burger_Sandwiches_Wraps > 10:
            print("You have Inputed an Invalid Number For Burgers, Sandwiches," 
                "and Wraps."
                "\nPlease Enter a number Between 1 - 10 For This Selection") 
            
    elif anything_Else == "N":
            
            
        #total = price 
            tax = price * sales_Tax
            
            total = price + tax
            
            ten_Tip = total * 0.10
            
            fifteen_Tip = total * 0.15
            
            twenty_tip = total * 0.20
            
            
            
            print(round(total, 2), "tip", round(ten_Tip, 2), round(sales_Tax, 2))
            sys.exit()
            
    


    
    
# If a number not used is selected an error message will be printed out 
# An else statement or elif statement can be used 
# Uncomment the statement underneath and comment the other to implament.

#elif burger_Sandwiches_Wraps < 1 or burger_Sandwiches_Wraps > 10:
#else:
    #print("You have Inputed an Invalid Number For Burgers, Sandwiches," 
        #"and Wraps."
        #"\nPlease Enter a number Between 1 - 10 For This Selection")
