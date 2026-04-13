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
                start.Manager_Storage_menu()
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
                exit()
            else:
                print("Inavlid Input!")

    def Manager_Storage_menu(self):
        while True:
            print('Please Choose From The Choices')
            print('1.Password Manager Menu')
            print('2.Password Storage Menu')
            print('3.End')
            choice1 = int(input('Choice: '))

            if choice1 == 1:
                self.Password_Manager()

            elif choice1 == 2:
                self.Password_Storage()
                
            elif choice1 == 3:
                print('Terminating Program')
                exit()
            else:
                print("Inavlid Input!")

    def Password_Manager(self):
        while True:
            print('Choose A Function')
            print('1.Generate Strong Password')
            print('2.Analyze Password')
            print('3.Personalized Password Generator')
            print('4.Strengthen Password')
            print('5.Return to menu')

            choice2 = int(input('Choice: '))

            if choice2 == 1:
                print('You Selected Generate Strong Password') #to be changed

            elif choice2 == 2:
                print('You Selected Analyze Password') #to be changed
                
            elif choice2 == 3:
                print('You Selected Personalized Password Generator') #to be changed

            elif choice2 == 4:
                print('You Selected Strengthen Password') #to be changed

            elif choice2 == 5: 
                self.Manager_Storage_menu()
            else:
                print("You Selected an Inavlid Input!")

    def Password_Storage(self):
        while True:
            print('Choose A Function')
            print('1.Display All Passwords')
            print('2.Add a Password')
            print('3.Update a Password')
            print('4.Delete a Password')
            print('5.Return to menu')

            choice2 = int(input('Choice: '))

            if choice2 == 1:
                print('You Selected Choose A Function') #to be changed

            elif choice2 == 2:
                print('You Selected Add a Password') #to be changed
                
            elif choice2 == 3:
                print('You Selected Update a Password') #to be changed

            elif choice2 == 4:
                print('You Selected Delete a Password') #to be changed

            elif choice2 == 5: 
                self.Manager_Storage_menu()
                
            else:
                print("You Selected an Inavlid Input!")
start = Main() 
start.start_menu()
