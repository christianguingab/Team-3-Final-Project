from sys import exit
import os

class Main:
    def __init__(self):
        self.accounts = {'username':'password'}
        self.storage = {}

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def create_account(self):
        while True:
            print('--------Create Account--------')
            username = input("Input Username: ")
            
            if username in self.accounts:
                self.clear_terminal()
                print('Username already exist. Try another one\n')
            else:
                break
        password = input('Input Password: ')
        self.accounts[username] = password

        self.clear_terminal()
        print('Successfully created an account!\n')

    def login(self):
        attempt = 3
        self.clear_terminal()
        while attempt != 0:
            print('--------Login--------')
            username = input("Input Username: ")
            password = input('Input Password: ')

            if username in self.accounts and self.accounts[username]==password:
                return # change this
            else:
                attempt -=1
                self.clear_terminal()
                print('Invalid Username or Password.\n')
        print('Access Denied. Exiting program...')
        exit()
         
    
    def start_menu(self):
        while True:
            print('--------Password Generator Manager---------')
            print('1.Login')
            print('2.Create Account')
            print('3.Exit')
            choice = int(input('Choice: '))

            if choice == 1:
                self.login()
            elif choice == 2:
                self.create_account()
            elif choice == 3:
                break
            else:
                print("Inavlid Input!")

start = Main() 
start.start_menu()