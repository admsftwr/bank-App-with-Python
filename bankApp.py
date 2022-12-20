import os
accountA = {
    "id" : "robertid",
    "password" : "robertpassword",
    "name" : "Robert",
    "surname" : "Dawney",
    "balance" : 5000,
    "additional acc" : 2000
}
accountB = {
    "id" : "jhonid",
    "password" : "jhonpassword",
    "name" : "Jhon",
    "surname" : "Smith",
    "balance" : 6000,
    "additional acc" : 3000
}


id = input("Username:")
password = input("Password:")
if id == accountA["id"] and password == accountA["password"]:
    accountInformation = accountA
elif id == accountB["id"] and password == accountB["password"]:
    accountInformation = accountB
else: 
    print("Username or password is incorrect!")



def withdrawMoney(account):
    print(f"Hello {account['name']} {account['surname']}, welcome to the ATM")
    print(
        """
        What do you want?
        1-Withdraw the money.
        2-Deposit the money.
        """
    )
    def exitOrMenu():
        print("What do you want?\n1-I want to return to the main menu.\n2-I'd like to check out!")
        exitOrMenu = int(input("Enter the number of the transaction you want to do(1/2):"))
        if exitOrMenu == 1:
            print("Transferring to the menu..")
            os.system("cls")
            withdrawMoney(account)
        elif exitOrMenu == 2:
            print("Checking out..")
    def accountBalanceInformation():
        print(f"You have a balance of ${balance} in your account. You also have an additional ${additional} account.")

    balance = account['balance']
    additional = account["additional acc"]
    withdrawOrDeposit = int(input("Enter the number of the transaction you want to do(1/2):"))
    if withdrawOrDeposit ==1: # WİTHDRAW
        accountBalanceInformation()
        withdrawAmount = int(input("Enter the amount of money you will withdraw from the bank:"))
        if balance >= withdrawAmount:
            balance -= withdrawAmount
            accountBalanceInformation()
            exitOrMenu()

        else:
            print("Your balance is not enough!")
            additionalAcc = input("Would you like to withdraw money from the additional account?(E/H):")
            if additionalAcc == "E":
                totalMoney = balance + additional
                if totalMoney >= withdrawAmount:
                    addWithdrawAmountr = withdrawAmount - balance
                    additional -= addWithdrawAmountr
                    balance = 0
                    accountBalanceInformation()
                    exitOrMenu()
                else:
                    print("Your additional account is not sufficient to withdraw funds.")
                    exitOrMenu()

            else:
                exitOrMenu()    
    elif withdrawOrDeposit == 2: # DEPOSİT
        accountBalanceInformation()
        depositAmount = int(input("Enter the amount to be deposited:"))
        balance +=depositAmount
        accountBalanceInformation()
        exitOrMenu()


    else: #NO VALID NUMBER ENTERED
        print("No valid number entered!")



withdrawMoney(accountInformation)
