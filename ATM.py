import random


class ATM():
    def __init__(self):
        print("Welcome to ATM!")
        self.cardNO = int(input("Please enter your card number: "))
        self.pinNO = int(input("Please enter your pin number: "))

    def Ask(self):

        def menu():
            print("\nWhat do you want to do?")
            print("[1] Withdraw Cash")
            print("[2] Check Balance")
            print("[3] Take Loan")
            print("[0] Exit the progam")

        menu()
        option = input("Please Select your Option - ")

        while option != "0":
            if option == "1":
                print("Cash has been withdrawn")
            elif option == "2":
                balance = random.randrange(100000, 900000)
                print("Your balance is ₹20000")
            elif option == "3":
                print("Your loan has been issued")
            else:
                print("▲ Invalid Option ▲")

            menu()
            option = input("Enter your option : ")

        print("Thank you for using our ATM. ")


User = ATM()
User.Ask()