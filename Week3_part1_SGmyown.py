print("Hello Welcome to Tru Astoria")
print("\nhThis is The Menu")
print("\nWhat Would You Enjoy Today?")

menu = int(input("\nClick 1 For Breakfast, 2 For Starters, 3 For Savory Crepes,"
                   "\n4 For Salads And Bowls, 5 For Burgers, Sandwiches," 
                   "\nand Wraps, 6 for Pizza, 7 For Pasta, 8 For Desserts?"))

if menu == 1:
    print("\nYou Have Chosen 1 For Breakfast Which is Eggs and Omelets -"
    "\nServed With Choice Of Hand Cut Fries, Home Fries," 
    "\nor Seasonal Fruit Salad.")
    
    breakfast = int(input("Please Choose 1 For Main Breakfast," 
                        "2 Sweet Beginnings, 3 Sides:"))
    
    if breakfast == 1:
        
        print("\nYou have Chosen Main BreakFast")
        
        main_Breakfast_menu = int(input("\nPlease Choose 1 For" 
                                        "\nMediterranean Egg White Wrap,"
                                        "\n2 For BreakFast Wrap,"
                                        "\n3 For"
                                        "Two Eggs, Bacon or Sausage, Toast,"
                                        "\n4 For Waffle, Eggs, Bacon or Sausage,"
                                        "\n5 For Power Omelet"
                                        "\n6 For Athenian Omelet,"
                                        "\n7 For Western Omelet,"))
        
        if main_Breakfast_menu == 1:
            print("\nMediterranean Egg White Wrap" 
                  "- Sun-dried tomato pesto, spinach," 
                  "\nfresh mozzarella. This is $12.48")
            
        elif main_Breakfast_menu == 2:          
            print("BreakFast Wrap" 
                    "- Scrambled eggs, smoked turkey," 
                    "Swiss cheese, avocado. This is $12.48") 
                  
        elif main_Breakfast_menu == 3:
            print("Two Eggs, Bacon or Sausage. Toast This is $11.44")
            
        elif main_Breakfast_menu == 4:    
            print("Waffle, Eggs, Bacon or Sausage. This is $15.60")
                 
                 
        elif main_Breakfast_menu == 5:
            
            print("Power Omelet - Egg whites, turkey, Swiss cheese, spinach." 
                  "This is $15.60")
            
        elif main_Breakfast_menu == 6:
            
            print("Athenian Omelet - Spinach, tomato, feta cheese."
                  "This is $15.60")
            
        elif main_Breakfast_menu == 7:
            
            print("Western Omelet - Bell peppers, onions, ham, American cheese." 
                  "This is $15.60")
        
        elif breakfast < 1 or breakfast > 7:
            print("You have Inputed an Invalid Number For The Menu." 
                  "\nPlease Enter a number Between 1 - 7 For This Selection")
             
    
    elif breakfast == 2:
        
        print("You Have Chosen Sweet Beginnings")
        
        main_Breakfast_menu = int(input("\nPlease Choose 1 For Maple Frech Toast,"
                                        "\n2 For Nutella French Toast,"
                                        "\n3 For Simple Pancake Stack,"
                                        "\n4 Blueberry Pancakes"))
        
        if main_Breakfast_menu == 1:
            print("Maple Frech Toast - Maple syrup. This is $11.44")
            
        elif main_Breakfast_menu == 2:          
            print("Nutella French Toast. This is $14.56") 
                  
        elif main_Breakfast_menu == 3:
            print("Simple Pancake Stack - Maple syrup.. This is $10.40")
            
        elif main_Breakfast_menu == 4:    
            print("Blueberry Pancakes. This is $12.48")
                 
                 
        elif breakfast < 1 or breakfast > 4:
            print("You have Inputed an Invalid Number For The Menu." 
                  "\nPlease Enter a number Between 1 - 7 For This Selection")        

        
    elif breakfast == 3:
        print("You Have Chosen Sides"
              "\nHome Fries is $4.16"
              "\nHand-Cut Fries is $6.24"
              "\nSausage is $4.16"
              "\nBacon is $4.16"
              "\nfruit Salad is $5.20")
        
    elif breakfast < 1 or breakfast > 3:
        print("You have Inputed an Invalid Number For Main BreakFast." 
              "\nPlease Enter a number Between 1 - 3 For This Selection")
 
    
if menu == 2:
    print("You Have Chosen 2 For Starters" 
          "\nEnjoy as an Appetizer or Combine as a Meal.")
    
    starters = int(input("Please Choose 1 For Greek Spreads Trio,"
                         "\n2 For Guacamole,"
                         "\n3 For Zucchini Croquettes,"
                         "\n4 For Vegettable Platter,"
                         "\n5 For Greek Rigani Fries,"
                         "\n6 For Halloumi Fries,"
                         "\n7 For Mini Burgers,"
                         "\n8 For Chicken Skewers,"
                         "\n9 Tru Tacos,"
                         "\n10 Grilled Octupus"
                         "\n11 Crab Cake"
                         "\n12 Tempura Shrimp"
                         "\n13 Fried Calamari"
                         "\n14 Spanakopita (Spinach Pie)"
                         "\n15 Tiropita (Cheese pie)"))
                   
    if starters == 1:
        print("Greek Spreads Trio - Tzatziki, tirokafteri, hummus." 
            "This is $9.36 Each or $14.56 For The Trio")
                       
    elif starters == 2:     
            print("Guacamole - Made fresh daily served with seasoned pita chips." 
                  "This is $12.48") 
                             
    elif starters == 3:
            print("Zucchini Croquettes" 
                  "- Zucchini and cheese fritters served with yogurt cucumber" 
                  "sauce. This is $12.48")
                       
    elif starters == 4:    
        print("Vegettable Platter - Grilled vegetables, falafel patties," 
            "roasted red peppers, avocado, cherry tomatoes," 
            "hummus and lemon tahini sauce. This is $16.64")
                            
                            
    elif starters == 5:
        print("Greek Rigani Fries - Hand cut fries, tossed in a garlic oil," 
            "parmesan, oregano, and feta sauce." 
            "This is $11.44")
                       
    elif starters == 6:
        print("Halloumi Fries - Breaded and fried sticks of halloumi cheese."
            "This is $12.48")
                       
    elif starters == 7:
        print("Mini Burgers - 3 seasoned all beef sliders," 
            "pickle-Mayo sauce, American cheese."
            "This is $13.52")
    elif starters == 8:
        print("Chicken Skewers - Chargrilled cubes of chicken breast served with" 
              "\npickled sweet peppers, shaved marinated cucumbers, hummus," 
              "\ntzatzitki sauce." "This is $14.56")
                               
    elif starters == 9:     
        print("Tru Tacos You Can Choose Between - Pulled Pork"
              "slow cooked pork in brine, creamy cilantro sauce, pico de Gallo," 
              "\nguac. or - Shrimp Mildly spicy grilled shrimp, red and white" 
              "cabbage, avocado, creamy cilantro sauce."
              "\nThis is $15.60") 
                                     
    elif starters == 10:
        print("Grilled Octupus" 
            "- Grilled sushi grade Spanish octopus white bean & Manouri cheese" 
            "\npurée, piquillo pepper glaze, Chickpeas, baby greens."
            "\nThis is $23.92")
                               
    elif starters == 11:    
        print("Crab Cake - 1 crab cake pan seared lump crab meat served" 
              "with grilled sweet corn salsa, chipotle aioli." 
              " This is $19.76")
                                    
                                    
    elif starters == 12:
        print("Tempura Shrimp - Crispy cauliflower, sriracha Mayo sauce." 
            "This is $14.56")
                               
    elif starters == 13:
        print("Fried Calamari- A TRU classic, flash fried served with" 
              "marinara and lemon wedges."
              "This is $16.64")
                               
    elif starters == 14:
        print("Spanakopita (Spinach Pie) - Light and flaky homemade dough filled" 
              "with a family recipe of leeks spinach and a feta cheese" 
              "blend baked to perfection."
              "This is $7.28")
    elif starters == 15:
        print("Tiropita (Cheese pie) - Light and flaky homemade dough filled" 
              "with a family recipe blend of feta cheese and delicious flavors" 
              "baked to perfection." "This is $728")
                   
    elif breakfast < 1 or breakfast > 15:
        print("You have Inputed an Invalid Number For Starters." 
            "\nPlease Enter a number Between 1 - 15 For This Selection")

if menu == 3:
    print("You Have Chosen 3 For Savory Crepes" 
        "\nServed With house Salad.")
            
    savory_Crepes = int(input("Please Choose 1 For Grilled Salmon,"
                        "\n2 For Sautéed Spinach,"
                        "\n3 For Grilled Chicken,"
                        "\n4 For Grilled Shrimp"))
                           
    if savory_Crepes == 1:
        print("Grilled Salmon - Dill cream cheese, avocado, grilled red onions." 
            "This is $18.72")
                               
    elif savory_Crepes == 2:     
        print("Sautéed Spinach - Mushrooms and feta with creamy cilantro sauce." 
            "This is $14.56") 
                                     
    elif savory_Crepes == 3:
        print("Grilled Chicken" 
            "- Mozzarella, charred tomatoes, sriracha mayo. This is $16.64")
                               
    elif savory_Crepes == 4:    
        print("Grilled Shrimp - Avocado, whipped feta and roasted red peppers." 
              "This is $16.64")
        
    elif breakfast < 1 or breakfast > 4:
        print("You have Inputed an Invalid Number For Savory Crepes." 
            "\nPlease Enter a number Between 1 - 4 For This Selection")

if menu == 4:
            print("You Have Chosen 4 For Salads And Bowls" 
                  "\nAdd Chicken - $5 Salmon - $8 Shrimp - $7.")
            
            salads_Bowls = int(input("Please Choose 1 For Baby Argula" 
                                     "and Berry Salad,"
                                 "\n2 For Baby Beet,"
                                 "\n3 For Greek Salad,"
                                 "\n4 For Tru Cobb,"
                                 "\n5 For Avocado Falafel Bowl,"
                                 "\n6 For Mexican Bowl,"
                                 "\n7 For Mini Burgers,"
                                 "\n8 For Grilled Salmon Quinoa Bowl"))
                           
            if salads_Bowls == 1:
                print("Baby Argula and Berry Salad" 
                      "- Baby arugula, fresh strawberries, blueberries," 
                      "avocado, candied walnuts, goat cheese," 
                      "raspberry viniagrette." 
                      "This is $14.56")
                               
            elif salads_Bowls == 2:     
                    print("Baby Beet - Baby arugula, grape tomatoes, crumbled" 
                          "goat cheese, lemon and olive oil dressing." 
                          "This is $14.56") 
                                     
            elif salads_Bowls == 3:
                    print("Zucchini Croquettes" 
                          "- Zucchini and cheese fritters served with yogurt cucumber" 
                          "sauce. This is $12.48")
                               
            elif salads_Bowls == 4:    
                print("Greek Salad - Baby arugula, grape tomatoes," 
                      "crumbled goat cheese, lemon and olive oil dressing." 
                      "This is $13.52")
                                    
                                    
            elif salads_Bowls == 5:
                print("Tru Cobb - Chopped romaine lettuce, tomatoes, hard" 
                      "boiled eggs, avocado," 
                      "\nsmoked bacon, feta cheese," 
                      "\ngrilled chicken, lemon and olive oil dressing." 
                      "\nThis is $15.60")
                               
            elif salads_Bowls == 6:
                print("Avocado Falafel Bowl - Pearl cous cous, romaine lettuce,"
                      "tabbouleh, avocado, chickpeas," 
                      "\nfalafel patties," 
                      "radishes, lemon tahini sauce."
                      "\nThis is $12.48")
                               
            elif salads_Bowls == 7:
                print("Mexican Bowl - Brown rice, black beans, avocado," 
                      "\nroasted chicken, pico de gallo, baby spinach," 
                      "\nroasted red peppers, creamy cilantro sauce."
                      "\nThis is $13.52")
            elif salads_Bowls == 8:
                print("Grilled Salmon Quinoa Bowl - Baby spinach, white cabbage," 
                      "red beets, quinoa, avocado, cannellini beans,"
                      "\ngrilled wild-caught atlantic salmon." 
                      "\nThis is $14.56")
                           
            elif salads_Bowls < 1 or salads_Bowls > 8:
                print("You have Inputed an Invalid Number For Salads And Bowls." 
                    "\nPlease Enter a number Between 1 - 8 For This Selection")
if menu == 5:
    print("You Have Chosen 5 For For Burgers, Sandwiches, and Wraps" 
          "\nServed with hand-cut fries or house salad.")
                            
    burger_Sandwiches_Wraps = int(input("Please Choose 1 For Tru Burger"
                             "\n2 For Classic Cheeseburger,"
                             "\n3 For Salmon Burger,"
                             "\n4 For Vegetable Panini,"
                             "\n5 For Greek Roast Chicken Panini,"
                             "\n6 For Fried Chicken Sandwich,"
                             "\n7 For Cubano,"
                             "\n8 For Falafel Wrap"
                             "\n9 For Grilled Chicken Wrap,"
                             "\n10 For Turkey Avocado BLT:"))
                                           
    if burger_Sandwiches_Wraps == 1:
        print("Tru Burger - sautéed onions, roasted red pepper, bacon," 
              "\nSwiss cheese, sriracha maple mayo, brioche bun." 
              "This is $18.72")
                                               
    elif burger_Sandwiches_Wraps == 2:     
        print("Classic Cheeseburger - Lettuce, tomato, onion," 
              "and American cheese on brioche bun." 
              "This is $16.64") 
                                                     
    elif burger_Sandwiches_Wraps == 3:
        print("Salmon Burger" 
              "- char-grilled wild-caught Atlantic salmon burger with a" 
              "\nsignature Worcestershire sauce, shredded cabbage," 
              "\nand mustard aioli. This is $19.76")
                                               
    elif burger_Sandwiches_Wraps == 4:    
            print("Vegetable Panini - farmers pick of fresh grilled," 
                  "\nvegetables, sun dried tomato aioli on a pressed Italian roll." 
                  "This is $15.60")
                                                    
                                                    
    elif burger_Sandwiches_Wraps == 5:
            print("Greek Roast Chicken Panini - breaded chicken breast,"
                  "\namerican cheese, guacamole spread, tomatoes," 
                  "\nhoney mustard, on a brioche. " 
                  "\nThis is $17.68")
            
    elif burger_Sandwiches_Wraps == 6:
        print("Fried Chicken Sandwich - breaded chicken breast, american cheese," 
              "\nguacamole spread, tomatoes, honey mustard, on a brioche. "
              "\nThis is $17.68")            
                                               
    elif burger_Sandwiches_Wraps == 7:
        print("Cubano - pulled pork, deli ham," 
              "Swiss cheese, pickles, and mustard."
              "\nThis is $17.68")
                                               
    elif burger_Sandwiches_Wraps == 8:
        print("Falafel Wrap - Bhummus, tabbouleh, tahini sauce," 
              "rugula, falafel fritters."
              "\nThis is $16.64")
        
    elif burger_Sandwiches_Wraps == 9:
        print("Grilled Chicken Wrap - roasted sliced turkey, Swiss cheese, bacon," 
              "\nromaine hearts, sliced tomato, avocado," 
              "sriracha mayo, on toasted wheat bread."
              "\nThis is $16.64")        
        
    elif burger_Sandwiches_Wraps== 10:
        print("Turkey Avocado BLT - roasted sliced turkey, Swiss cheese, bacon," 
              "\nromaine hearts, sliced tomato, avocado," 
              "\nsriracha mayo, on toasted wheat bread." 
              "\nThis is $18.72")
                                           
    elif burger_Sandwiches_Wraps < 1 or burger_Sandwiches_Wraps > 10:
        print("You have Inputed an Invalid Number For Burgers, Sandwiches," 
              "and Wraps."
              "\nPlease Enter a number Between 1 - 10 For This Selection")

if menu == 6:
    print("You Have Chosen 6 For Pizza" 
        "\nAdd Chicken - $5 Salmon - $8 Shrimp - $7.")
                    
    pizza = int(input("Please Choose 1 For Tru Pizza,"
                            "\n2 For Margherita Pizza,"))
                                   
    if pizza == 1:
        print("Tru Pizza - Mozzarella cheese, Bacon, Ham, Bell Peppers, Onion,"
              "\nMushrooms, homemade pizza sauce." 
              "This is $19.76")
                                       
    elif pizza == 2:     
        print("Margherita Pizza - Fresh Mozzarella, Basil, homemade pizza sauce." 
            "This is $16.64") 
                
    elif pizza< 1 or pizza > 2:
        print("You have Inputed an Invalid Number For Pizza." 
            "\nPlease Enter a number Between 1 - 2 For This Selection")

if menu == 7:
    print("You Have Chosen 6 For Pasta" 
        "\nAdd Chicken - $5 Salmon - $8 Shrimp - $7.")
                            
    pasta = int(input("Please Choose 1 For Penne Ala Vodka,"
                               "\n2 For Penne Alfredo,"
                               "\n3 For Shrimp Scampi"))
                                           
    if pasta == 1:
        print("Penne Ala Vodka - penne al dente tossed in" 
              "\na vodka marinara cream sauce." 
              "This is $16.64")
                                               
    elif pasta == 2:     
        print("Penne Alfredo - penne al dente tossed in a white" 
              "\nwine creamy cheese sauce." 
              "\nThis is $16.64") 
        
    elif pasta == 3:     
        print("Shrimp Scampi - Linguini al dente with grilled shrimp" 
              "\ntossed in a garlic lemon butter sauce." 
              "\nThis is $19.76")         
                        
    elif pasta  < 1 or pasta  > 3:
        print("You have Inputed an Invalid Number For Pasta." 
            "\nPlease Enter a number Between 1 - 2 For This Selection")

if menu == 8:
        print("You Have Chosen 8 For Dessert.")
                                    
        dessert = int(input("Please Choose 1 For Yiaourti"
                                    "\n2 For Desset Waffle,"
                                    "\n3 For Nutella Crepe,"
                                    "\n4 For Nutella Royale Crepe,"
                                    "\n5 For Nutella Brownie Crepe,"
                                    "\n6 For Nutella Berry Crepe,"
                                    "\n7 For Scoop of Ice Cream,"))
                                                   
        if dessert == 1:
            print("Yiaourti - Greek Yogurt topped with natural" 
                  "\nhoney, nuts, and berries"
                  "\nThis is $10.40")
                                                       
        elif dessert == 2:     
            print("Desset Waffle - Waffles topped with banana, blueberries," 
                  "\nstrawberries, nutella, and scoop of vanilla ice cream." 
                  "\nThis is $14.56") 
                                                             
        elif dessert == 3:
            print("Nutella Crepe" 
                "- Crepe filled with nutella and topped with powdered sugar." 
                "\nThis is $10.40")
                                                       
        elif dessert == 4:    
            print("Nutella Royale Crepe - Crepe filled with nutella, bananas," 
                  "\nstrawberries, and topped with powdered sugar." 
                  "This is $12.48")
                                                            
                                                            
        elif dessert == 5:
            print("Greek Roast Chicken Panini - breaded chicken breast,"
                "\namerican cheese, guacamole spread, tomatoes," 
                "\nhoney mustard, on a brioche. " 
                "\nThis is $17.68")
                                                       
        elif dessert == 6:
            print("Cubano - pulled pork, deli ham," 
                "Swiss cheese, pickles, and mustard."
                "\nThis is $17.68")
                                                       
        elif dessert == 7:
            print("Scoop of Ice Cream - Vanilla, or Chocolate"
                "\nThis is $2.08")
                
                                                   
        elif dessert < 1 or dessert > 7:
            print("You have Inputed an Invalid Number For Dessert." 
                "\nPlease Enter a Number Between 1 - 7 For This Selection")
        
                                    
else:
    print("You have Inputed an Invalid Number For Menu." 
        "\nPlease Enter a number Between 1 - 8 For This Selection")           