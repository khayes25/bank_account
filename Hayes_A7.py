"""
See instructions in CSCI111_A7.pdf

Be sure to rename this file Lastname_A7.py, using your last name
in place of "Lastname".

Your name: Keon Hayes

"""

balance = float(input("Please enter the staring balance: "))         #Prompting the user to enter the starting balance, which will be returned to the balance variable.

"""
A procedure called read_deposit_file is created to read the deposit file and add the amounts contained in the file to the balance variable.
"""

def read_deposit_file() :
    global balance                                                   #Declaring the balance variable global so its value can be used outside of this procedure.
    deposit_file = open("Deposits.txt", "r")                         #Opens the Deposits.txt file in read-only mode.
    for line in deposit_file :                                       #A for loop is used to iterate over the lines of text in the file.
        balance += float(line.rstrip("\n"))                          #Any linefeed escape sequences will be stripped before the line is typecast as a float, which will be added to the balance variable.
    deposit_file.close()                                             #Closes the Deposits.txt file.

"""
A procedure called read_withdrawal_file is created to read the withdrawal file subtract the amounts contained in the file from the balance variable.
"""

def read_withdrawal_file() :                                
    global balance                                                   #Declaring the balance variable global so its value can be used outside of this procedure.
    withdrawal_file = open("Withdrawals.txt", "r")                   #Opens the Withdrawals.txt file in read-only mode.
    for line in withdrawal_file :                                    #A for loop is used to iterate over the lines of text in the file.
        balance -= float(line.rstrip("\n"))                          #Any linefeed escape sequences will be stripped before the line is typecast as a float, which will be added to the balance variable.
    withdrawal_file.close()                                          #Closes the Withdrawals.txt file.

print("Your starting balance is: $", format(balance, ".2f"), sep="") #The starting balance that the user entered will be printed back to them, with a dollar sign in front and formatted to two decimal places.
read_deposit_file()                                                  #The read_deposit_file procedure is called which will change the value of the balance variable.
read_withdrawal_file()                                               #The read_withdrawal_file procedure is called which will change the value of the balance variable.
print("Your ending balance is: $", format(balance, ".2f"), sep="")   #The new value of the balance variable will be printed with a dollar sign in front and formatted to two decimal places.
















































































