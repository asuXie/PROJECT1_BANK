import random
from datetime import datetime
from currency_converter import CurrencyConverter
import os
import glob
c = CurrencyConverter()

dtNow = datetime.now()
dtNowString = dtNow.strftime("%d/%m/%Y %H:%M:%S")

class Currency:
    pass
class User:
    def __init__(self, id):
        
        name = str(input("Podaj imię: ")) 
        surname = str(input("Podaj nazwisko: "))
        self.id = id
        self._name = name.upper()
        self._surname = surname.upper()
        self._balance = {
            "USD":0,
            "EUR":0,
            "JPY":0,
            "GBP":0,
            "AUD":0,
            "PLN":0
                        }
        self._cardNumber =f"000{random.randrange(100000, 999999)}" #numer karty
        self._currienciesNum = 0
        self._currency = {
            "USD":False,
            "EUR":False,
            "JPY":False,
            "GBP":False,
            "AUD":False,
            "PLN":False
                        }
        self.history = []

        self._inHistoryFile("Account created")



        print("Twój numer karty", self._cardNumber)
        
    
    

    def typeShow(self):
        for variety in self.history:
            print(variety)

    def withdraw(self): #wypłata
        variety = "Withdrawal"
        currency = str(input("Wybierz rodzaj waluty: "))
        currency = currency.upper()
        withdrawal = float(input("Kwota do wypłacenia: "))
        withdrawal = round(withdrawal, 2)
        for key in self._currency:
            if key == currency:
                if withdrawal <= self._balance[currency]:
                    self._balance[currency] -= withdrawal
                    print("Operacja zakończona pomyślnie")   
                    self._inHistoryFile(variety, currency, withdrawal)
                    if self._balance[currency] == 0:
                        self._currency[currency] = False
                        
                        

    def deposit(self): #wpłata
        variety = "Deposit"
        currency = str(input("Wybierz rodzaj waluty: "))
        currency = currency.upper()
        deposit = float(input("Kwota do wpłacenia: "))
        deposit = round(deposit, 2)
        for key in self._currency:
            if key == currency:
                self._balance[currency] += deposit
                self._currency[currency] = True
                print("Operacja zakończona pomyślnie")  
                self._inHistoryFile(variety, currency, deposit) 
                   

    def userInfo(self): #info o użytkowniku
        print("Imię: ", self._name) 
        print("Nazwisko: ", self._surname)
        print("Numer karty: ", self._cardNumber)
        print(" ")
        print("Waluty: ")
        for keys in self._balance:
            print(keys, "Kwota: ", self._balance[keys])
   
    def _currenciesAvailable(self, current): #dostępne waluty
        current.upper()
        currencyAvailability = False
        if self._currency[current] == True:
            currencyAvailability = True
        return currencyAvailability
    
    def validation(self, cardNumber, surname): #walidacja użytkownika
        if self._cardNumber == cardNumber and self._surname == surname:
            return True
        else:
            return False
        
    def currencyTransfer(self): #przewalutowanie
        variety = "Currency transfer"
        fromCurrency = str(input("Podaj walutę do przewalutowania: "))
        toCurrency = str(input("Podaj walutę docelową: "))
        fromCurrency = fromCurrency.upper()
        toCurrency = toCurrency.upper()
        amount = float(input("Podaj kwotę: "))
        if self._currenciesAvailable(fromCurrency) == True:
            tempMoney = c.convert(amount, fromCurrency, toCurrency)
            
            tempMoney = round(tempMoney, 2)
            self._balance[fromCurrency] -= amount
            self._balance[toCurrency] += tempMoney
            print("Operacja zakończona pomyślnie")
            self._inHistoryFile(variety, fromCurrency, amount, toCurrency)
        
        else:
            print("Operacja nieudana")
        
    def _inHistoryFile(self, *args): #zapis do pliku
        match len(args):
            case 1:
                self.file = open(f"transactions/{str(self._cardNumber)}", "a", encoding="utf-8") ##KWARGS i ARGS do dodania #0 - typ operacji, 1 - waluta, 2 - kwota, 3 - waluta docelowa
                self.file.write(f"{dtNowString} -> {args[0]}\n") 
                self.file.close()   
            case 3: 
                self.file = open(f"transactions/{str(self._cardNumber)}", "a", encoding="utf-8")
                self.file.write(f"{dtNowString} -> {args[0]}: {args[1]} -> {args[2]}\n") 
                self.file.close()
            case 4:
                self.file = open(f"transactions/{str(self._cardNumber)}", "a", encoding="utf-8")
                self.file.write(f"{dtNowString} -> {args[0]}: {args[1]} -> {args[3]}: {args[2]}\n") 
                self.file.close()


        
    
    @staticmethod
    def cleanTransactions():
        for file in glob.glob("transactions/*"):
            os.remove(file)
        
   

accountsNum = int(input("Podaj liczbę użytkowników: ")) #ilość użytkowników
account = []

for id in range(0, accountsNum):
    
    account.append(User(id)) ##Powoływanie obiektu User


term = 1
while term != 0:
    print("1. Zaloguj się")
    print("0. Wyjdź")
    
    term = int(input("Wybierz: "))
    match term:
        case 1:
            cardNumber = str(input("Podaj nr karty: "))
            surname = str(input("Podaj nazwisko: "))
            surname = surname.upper()
            
            
    

            for id in range(0, accountsNum):
                if account[id].validation(cardNumber, surname) == True:
                   termInside = 1
                   while termInside != 0:
                        print("1. Wyświetl dane konta")    
                        print("2. Wpłać") 
                        print("3. Wypłać") 
                        print("4. Historia transakcji")
                        print("5. Transfer walut") 
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
                                account[id].currencyTransfer()
            
            else:
                print("Brak użytkownika: ", surname)

print("Do widzenia!")   
User.cleanTransactions()                  

            #Program do obsługi bankomatu, należy wykonać historię transakcji, wypłatę, wpłatę, przewalutowanie, wyświetlenie informacji o użytkowniku, wylogowanie, wyjście z programu
    
    
    
    
    












