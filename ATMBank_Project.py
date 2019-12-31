#ATM Detailed assignment
BankDetails=["Sege Play",23,"Male","student",85000,9881,50169002]
print("Welcome to XYZ Bank")
toContinue ="yes"
while toContinue =="yes":
# getting user information pin
    userPin = eval(input("Account Pin:"))
    if userPin ==BankDetails[5]:
        print("Good Day Mr."+BankDetails[0])
        print("choose any options below")
        print("1) Withdraw \t2) Deposit \n3) Balance  \t4) Online Transfer")
        userChoice =eval(input("choice: "))
        if userChoice ==1:
            wAmount = eval(input("Amount:"))
            if wAmount >=BankDetails[4]:
                print("insufficient Funds")
            else:
                print("Withdrawer successful\nBalance is {}".format(BankDetails[4]-wAmount))
        elif userChoice ==2:
            dAmount = eval(input("Naira Amount:"))
            print("Put your cash in the tray")
            print("Deposit successful\nBalance is {}".format(BankDetails[4]+dAmount))







        #if input wrong information
    else:
        print("Invalid Pin")

