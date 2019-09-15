# -*- coding: utf-8 -*-
"""
Created on Saturday September 02 2019
Raymond Jing
"""
import pandas as pd
import pandas_datareader as pdr
from time import sleep

# Creating a list for the default company
symbols = ['AAPL', 'AMZN', 'GOOG', 'MSFT', 'FB', 'NFLX','CRM', 'BKNG', 'PYPL', 'UBER', 'EBAY', 'LKI.DU']

# create list to store operrational options
options = " Track Default Stock, Show Default List, \
Add Stock to Default List, Edit Default List, Add New Stock, Quit".split(",")

def show_default(symbols):
    symbols.sort()
    return symbols

def add_to_default(symbols):
    print("Enter symbol to add: ")
    symbol = input()
    while symbol != '':
        symbols.append(symbol)
        symbol = input("Enter symbol to add: Hit enter to quit")
    return symbols.sort()    

# function code 
# read each symbol and output in numbered list  
def edit_default(symbols):
    print("Select symbol to delete:")
    for i in range(1,len(symbols) + 1):
        print("{} - {}".format(i, symbols[i-1]))
    remove = symbols.pop(int(input()) - 1)    
    print("{} removed".format(remove))

# Define functions 
# add new list --> prompt for symbols until empty string 
def add_list():
    new_list = []
    print("Enter symbol to add: ")
    symbol = input().upper()
    while symbol != '':
        new_list.append(symbol)
        symbol = input("Enter symbol to add, or enter to quit: ")
        symbol = symbol.upper()
    return new_list

def get_prices(symbols):
    symbols.sort()
    return pdr.get_quote_yahoo(symbols)['price']

#Define main()
def main(): 
    run_program = True
    while run_program:
        print("Choose option:")
        for i in range(1, len(options)+1):
            print("{:} - {}".format(i,options[i-1]))
        choice = int(input())    
        # contine to implement defined functions 
        if choice == 1:
            print("Getting quotes")
            while True:
                print(get_prices(symbols))
                print("Ctrl + C to quit")
                sleep(5)

        elif choice == 2:
            print("Current default list:")
            print(show_default(symbols))
            print()

        elif choice == 3:
            add_to_default(symbols)

        elif choice == 4:
            edit_default(symbols)

        elif choice == 5:
            new_list = add_list()
            print("Getting quotes")
            while True:
                print(get_prices(new_list))
                print("Ctrl + C to quit")
                sleep(5)

        elif choice == 6:
            run_program = False        

if __name__ == "__main__":
    main()    


