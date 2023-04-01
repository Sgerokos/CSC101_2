# The variable balance ask's the user to input the balance they wish to calculate 

balance = float(input("Please Enter The Balance You Wish to Calculate: " ))

# The variable annualInterestRate ask's the user to input the annual interest

annualInterestRate = float(input("Please Enter The Annual Interest Rate Percentage: "))

# The variable interest calculates the balance and annual interest

interest = balance * annualInterestRate / 1200

# Print's the interest calcualted to the 5th decimal number 

print("The Annual Interest Rate is: ", round(interest, 5))