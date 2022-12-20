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
        print("Geçerli rakam girmediniz!")



withdrawMoney(accountInformation)


# Başta kullanıcı adı ve şifre bilgileri'ni alır, hesaba bu bilgilere göre giriş yapar.
# Hesaba giriş yaptıktan sonra liste içinde bulunan isim ve soyisim bilgileri ile selamlama yapar.
# Programa ilk girdiğimizde bir menü ile karşılaşılır, menüde para çekme ve para yatırma seçenekleri vardır.

# Para çekme seçeneğine tıklarsak bize hesap bakiyemizi ve ek hesabımızın bilgilerini aktarır.
# Çekeceğimiz para miktarının durumuna göre işlemler farklıdır:
# 1- Eğer çekeceğimiz miktar bakiyemizden az ise parayı çeker ve kalan bakiyemizi söyler.
# 2- Eğer çekeceğimiz miktar bakiyemiz kadar ise yine parayı çeker ve kalan bakiyemizi söyler.
# 3- Eğer çekeceğimiz miktar bakiyemizden fazla ise ek hesap kullanıp kullanmayacağımızı sorar. Bu durumda yine 2 ihtimal doğar:
#  a- Eğer çekeceğimiz miktar bakiyemiz ve ek hesabımızın toplamından fazla ise parayı çekmez.
#  b- Eğer çekeceğimiz miktar bakiyemiz ve ek hesabımızın toplamından az ise ek hesaptan ve bakiyeden parayı çeker, hesap ve ek hesap bilgilerini söyler.
# Tüm bu para çekme olayları sonucunda karşımıza hep bir menü daha çıkar. Bu menüde ana menüye dönme ve çıkış yapma seçenekleri vardır.
# Ana menüye'de dönsek çıkışta yapsak çektiğimiz para miktarına göre bakiyemiz save edilmez, hala bakiye aynı kalır.

# Para yatırma seçeneğine tıklarsak bize hesap bakiyemizi ve ek hesabımızın bilgilerini aktarır.
# Yatırılacak miktarı sorar ve işlem tamamlanınca yeni hesap bakiyemizi ve ek hesabımızın bilgilerini aktarır.
# Karşımıza hep bir menü daha çıkar. Bu menüde ana menüye dönme ve çıkış yapma seçenekleri vardır.
# Ana menüye'de dönsek çıkışta yapsak çektiğimiz para miktarına göre bakiyemiz save edilmez, hala bakiye aynı kalır.