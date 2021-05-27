# A simple text-based banking interface that lets you create an account, log in and check account balance, using classes and methods. Based on Hyperskill exercise.

import random
random.seed(0)

class Bank:
    dict_cards = {}

    def __init__(self):
        self.card_number = None
        self.pin = None
        
    def generate_card_number(self):
        self.card_number = "400000" + "".join([str(random.randint(0, 9)) for i in range(10)])

    def generate_pin(self):
        self.pin = "".join([str(random.randint(0, 9)) for i in range(4)])

    def update_dict(self):
        Bank.dict_cards[self.card_number] = {"PIN": self.pin}

    def create_account(self):
        self.generate_card_number()
        self.generate_pin()
        self.update_dict()

    def check(self, card_number, pin_number):
        if card_number not in Bank.dict_cards:
            return False
        else:
            if pin_number == Bank.dict_cards[card_number]["PIN"]:
                return True
            return False

    def start(self):
        while True:
            print("1. Create an account")
            print("2. Log into account")
            print("0. Exit")
            main_input = int(input())
            if main_input == 0:
                print("Bye!")
                break
            elif main_input == 1:
                self.create_account()
                print("Your card has been created.")
                print("Your card number:")
                print(self.card_number)
                print("Your PIN:")
                print(self.pin)
            elif main_input == 2:
                print("Enter your card number:")
                card_number = str(input())
                print("Enter your PIN:")
                pin_number = str(input())
                if self.check(card_number, pin_number):
                    print('You have successfully logged in.')
                    while True:
                        print("1. Balance")
                        print("2. Log out")
                        print("0. Exit")
                        sub_input = int(input())
                        if sub_input == 0:
                            print("Bye!")
                            exit()
                        elif sub_input == 1:
                            print("Balance: 0")
                        elif sub_input == 2:
                            print("You have successfully logged out.")
                            break
                else:
                    print('Wrong card number or PIN.')

bank = Bank()
bank.start()
