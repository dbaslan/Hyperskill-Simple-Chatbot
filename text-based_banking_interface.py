# A simple text-based banking interface that lets you create an account, log in and check account balance. Based on Hyperskill exercise.

import random
random.seed(1)
cards = {}
cardlist = []
pinlist = []

def main_menu():
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")
    main_input = int(input())
    if main_input == 1:
        create_card() 
    elif main_input == 2:
        login() 
    elif main_input == 0:
        print("Bye!")

def create_card():
    print("Your card has been created")
    print("Your card number:")
    y = "400000"
    for i in range(10):
        x = str(random.randint(0, 9))
        y += x
    print(y)
    print("Your card PIN:")
    b = ""
    for i in range(4):
        a = str(random.randint(0, 9))
        b += a
    print(b)
    cards[y] = b
    cardlist.append(y)
    pinlist.append(b)
    main_menu()

def login():
    print("Enter your card number:")
    card = str(input())
    print("Enter your PIN:")
    PIN = str(input())
    if card in cardlist:
        if cards[card] == PIN:
            print("You have successfully logged in!")
            loggedin()
        elif cards[card] != PIN:
            print("Wrong card number or PIN!")
            main_menu()
    else:
        print("Wrong card number or PIN!")
        main_menu()
        
def loggedin():
    print("1. Balance")
    print("2. Log out")
    print("0. Exit")
    sub_input = int(input())
    if sub_input == 1:
        print("Balance: 0")
        loggedin()
    elif sub_input == 2:
        print("You have successfully logged out!")
        mainmenu()
    elif sub_input == 0:
        print("Bye!")
        
main_menu()
