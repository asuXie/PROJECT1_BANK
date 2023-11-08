import random
from datetime import datetime
from currency_converter import CurrencyConverter
from tkinter import Tk
c = CurrencyConverter()

dtNow = datetime.now()
dtNowString = dtNow.strftime("%d/%m/%Y %H:%M:%S")

class Currency:
    pass
class User:
    def __init__(self, id, name, surname, cardNumber):
        self.id = id
        self.name = name
        self.surname = surname
        self.balance = {
            "USD":0,
            "EUR":0,
            "JPY":0,
            "GBP":0,
            "AUD":0,
            "PLN":0
                        }
        self.cardNumber = cardNumber 
        self.currienciesNum = 0
        self.currency = {
            "USD":False,
            "EUR":False,
            "JPY":False,
            "GBP":False,
            "AUD":False,
            "PLN":False
                        }
        self.history = []
    
    def typeAssign(self, amount, variety, currency):
        result = (variety, amount, currency, dtNowString)
        (self.history).append(result)

    def typeShow(self):
        for variety in self.history:
            print(variety)

    def withdraw(self): #wypłata
        variety = "Withdrawal"
        currency = str(input("Wybierz rodzaj waluty: "))
        currency.upper()
        withdrawal = float(input("Kwota do wypłacenia: "))
        withdrawal = round(withdrawal, 2)
        for key in self.currency:
            if key == currency:
                if withdrawal <= self.balance[currency]:
                    self.balance[currency] -= withdrawal
                    print("Operacja zakończona pomyślnie")   
                    self.typeAssign(variety, withdrawal, currency)
                    if self.balance[currency] == 0:
                        self.currency[currency] = False
                        

    def deposit(self): #wpłata
        variety = "Deposit"
        currency = str(input("Wybierz rodzaj waluty: "))
        currency.upper()
        deposit = float(input("Kwota do wpłacenia: "))
        deposit = round(deposit, 2)
        for key in self.currency:
            if key == currency:
                self.balance[currency] += deposit
                self.currency[currency] = True
                print("Operacja zakończona pomyślnie")
                self.typeAssign(variety, deposit, currency)      
                   

    def userInfo(self): #info o użytkowniku
        print("Imię: ", self.name) 
        print("Nazwisko: ", self.surname)
        print("Numer karty: ", self.cardNumber)
        print(" ")
        print("Waluty: ")
        for keys in self.balance:
            print(keys, "Kwota: ", self.balance[keys])
   
    def currenciesAvailable(self, current):
        currencyAvailability = False
        if self.currency[current] == True:
            currencyAvailability = True
        return currencyAvailability

    
    


def currencyTransfer():
    type = "Currency Transfer"
    fromCurrency = str(input("Podaj walutę do przewalutowania: "))
    toCurrency = str(input("Podaj walutę docelową: "))
    amount = float(input("Podaj kwotę: "))
    if account[id].currenciesAvailable(fromCurrency) == True:
        tempMoney = c.convert(amount, fromCurrency, toCurrency)
        
        tempMoney = round(tempMoney, 2)
        account[id].balance[fromCurrency] -= amount
        account[id].balance[toCurrency] += tempMoney
        print("Operacja zakończona pomyślnie")
    
    else:
        print("Operacja nieudana")


accountsNum = int(input("Podaj liczbę użytkowników: "))
account = []

for id in range(0, accountsNum):
    name = str(input("Podaj imię: ")) 
    surname = str(input("Podaj nazwisko: "))
    cardNumber = random.randrange(100000, 999999)  ##Losowanie liczby - nr karty 
    print("Twój numer karty", cardNumber)

    account.append(User(id, name, surname, cardNumber)) ##Powoływanie obiektu User
term = 1
while term != 0:
    print("1. Zaloguj się")
    print("0. Wyjdź")
    
    term = int(input("Wybierz: "))
    match term:
        case 1:
            cardNumber = int(input("Podaj nr karty: "))
            surname = str(input("Podaj nazwisko: "))
    

            for id in range(0, accountsNum):
                if account[id].cardNumber == cardNumber and account[id].surname == surname:
                   termInside = 1
                   while termInside != 0:
                        print("1. Wyświetl dane konta")    
                        print("2. Wpłać") 
                        print("3. Wypłać") 
                        print("4. Historia transakcji")
                        print("4. Transfer walut") 
                        print("0. Wyloguj")
                        termInside = int(input("Wybierz: "))


                        match termInside:
                            
                            case 1:
                                account[id].userInfo()

                            case 2:
                                account[id].deposit()
                            
                            case 3:
                                account[id].withdraw()

                            case 4:
                                account[id].typeShow()
                            
                            case 5:
                                currencyTransfer()
            
            else:
                print("Brak użytkownika: ", surname)
print("Do widzenia!")                    

            #Program do obsługi bankomatu, należy wykonać historię transakcji, wypłatę, wpłatę, przewalutowanie, wyświetlenie informacji o użytkowniku, wylogowanie, wyjście z programu
    
    
    
    
    












