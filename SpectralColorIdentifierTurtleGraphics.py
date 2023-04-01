# Imports the turtle module in python
import turtle

# Ask's the user to input a specrum number ranging from 380 - 700
spectral = int(input("Please Enter a Spectral Color in Wavelength" 
                     "nano-meters (nm) Ranging From  380-700: "))

# Line's 8 - 56 Print's the color if the number is between 380 and 700
# This also writes with turtle and show's color and the word
# In turtle color the color of the text can be changed
# Style can be used to change the font, the letter size in this case 90 and if 
# it should be italic or even bold
# Turtle.write is the information that will be writen in turtle font 
# style can be changed and so can the alignment

#if spectral >= 380 and spectral < 450:
if 380 <= spectral < 450:   
    print("The Color is Violet")
    turtle.color("violet")
    style = ("Courier", 90, "italic")
    turtle.write("Violet", font = style, align = "center")       
    
#elif spectral > 450 and spectral < 485:
elif 450 < spectral < 485:  
    print("The Color is Blue")
    turtle.color("blue")
    style = ("Courier", 90, "italic")
    turtle.write("Blue", font = style, align = "center")   
    
#elif spectral > 485 and spectral < 500:
elif 485 < spectral < 500:  
    print("The Color is Cyan")
    turtle.color("Cyan")
    style = ("Courier", 90, "italic")
    turtle.write("Cyan", font = style, align = "center")       

#elif spectral > 500 and spectral < 565:
elif 500 < spectral < 565:     
    print("The Color is Green")
    turtle.color("green")
    style = ("Courier", 90, "italic")
    turtle.write("Green", font = style, align = "center")       
    
#elif spectral > 565 and spectral < 590:
elif 565 < spectral < 590: 
    print("The Color is Yellow")
    turtle.color("yellow")
    style = ("Courier", 90, "italic")
    turtle.write("Yellow", font = style, align = "center")       

#elif spectral > 590 and spectral < 625:
elif 590 < spectral < 625:
    print("The Color is Orange")
    turtle.color("orange")
    style = ("Courier", 90, "italic")
    turtle.write("Orange", font = style, align = "center")       
    
#elif spectral > 625 and spectral <= 700:
elif 625 < spectral <= 700:
    print("The Color is Red")
    turtle.color("red")
    style = ("Courier", 90, "italic")
    turtle.write("Red", font = style, align = "center")

# If the number is not in the range of 380 - 700 an error message will print out

else:
    print("The Input You Have Entered is Not Recognized." 
          "\nPlease Input a Number Ranging From 380 - 700. Thank You!!!")