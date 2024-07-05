class Atm:
    def __init__(self):
        self.__pin = ""
        self.__balance = 0
        self.__menu()

     # __var to make it private (access modifier)   
    def get_pin(self):
        print(f"current pin - {self.__pin}")
    
    def set_pin(self):
        temp = int(input("enter the pin that you want to set up"))
        self.__pin = temp
        print("Pin Changed Successfully")

    def __menu(self):
        choice = input("""Selct the desired Action
        1. Press 1 to create pin
        2. Press 2 to Deposit 
        3. Press 3 to withdraw
        4. press 4 to check balance
        5. press 5 to exit
        """)

        if choice == "1":
            self.create_pin()
 
        elif choice == "2":
            self.cash_deposit()
        elif choice == "3":
            self.withdraw_cash()
        elif choice == "4":
            self.check_balance()
        else:
            print("Bye")
    
    def create_pin(self):
        self.__pin = input("Enter the pin - ")
        print("Pin Create Sucessfully")
        self.__menu()
    
    def cash_deposit(self):
        temp = input("Enter the pin")
        if temp == self.__pin:
            amount = int(input("Enter the amount you want to deposit - "))
            self.__balance = self.__balance + amount
            print("Amount deposited successfully")
        self.__menu()

    def withdraw_cash(self):
        temp = input("Enter the pin")
        if temp == self.__pin:
            amount = int(input("Enter the amount you want to withdraw - "))
            if amount < self.__balance:
                self.__balance = self.__balance - amount
                print(f"Cash withdraw successful. Available amount = {self.__balance}")
            
            else:
                print("Insufficent Funds.")
        else:
            print("Incorrect Pin. please try again!")
        self.__menu()
    
    def check_balance(self):
        print(f"Current Balance is {self.__balance}")
        self.__menu()

            

 

            



