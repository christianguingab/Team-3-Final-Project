from PasswordStorage import PasswordStorage
from StrongPassword import StrongPassword
from AnalyzePassword import AnalyzePassword
from StrengthenPassword import StrengthenPassword
from sys import exit
import os

class Main:
    def __init__(self):
        self.accounts = {'username':'password'}

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
                self.clear_terminal()
                start.Manager_Storage_menu()
                return
            else:
                attempt -=1
                self.clear_terminal()
                print(f'Invalid Username or Password. You have {attempt} attempts left\n')
       
        print('Access Denied. Exiting program...')
        exit()
         
    
    def start_menu(self):
        while True:
            print('--------Password Generator Manager---------')
            print('1.Login')
            print('2.Create Account')
            print('3.Exit')
            
            try: 
                choice = int(input('Choice: '))
                if choice == 1:
                    self.login()
                elif choice == 2:
                    self.create_account()
                elif choice == 3:
                    exit()
                else:
                    print("Inavlid Input!")
            except ValueError:
                print("Please enter a valid number.")

    def Manager_Storage_menu(self):
        self.clear_terminal()
        while True:
            print('Please Choose From The Choices')
            print('1.Password Manager Menu')
            print('2.Password Storage Menu')
            print('3.End')
            choice1 = int(input('Choice: '))
            try:
                if choice1 == 1:
                    self.Password_Manager()
                    
                elif choice1 == 2:
                    self.clear_terminal()
                    self.Password_Storage()
                
                elif choice1 == 3:
                    print('Terminating Program')
                    exit()
            
                else:
                    print("Inavlid Input!")
           
            except ValueError:
                print("Please enter a valid number")

    def Password_Manager(self):
        Strong = StrongPassword()
        Analyze = AnalyzePassword()
        Strengthen = StrengthenPassword()
        self.clear_terminal()
        while True:
            print(' --- Password Manager Menu ---')
            print('1.Generate Strong Password')
            print('2.Analyze Password')
            print('3.Personalized Password Generator')
            print('4.Strengthen Password')
            print('5.Return to menu')

            choice2 = int(input('Choice: '))

            if choice2 == 1:
                self.clear_terminal()
                print('--------Strong Password--------')
                print('Generated Password: ',Strong.generate())

            elif choice2 == 2:
                self.clear_terminal()
                print('--------Analyze Password--------')
                print(Analyze.generate())
                
            elif choice2 == 3:
                self.clear_terminal()
                print('pesonalize') # change this

            elif choice2 == 4:
                self.clear_terminal()
                print('--------Strengthen Password--------')
                Strengthen.generate()

            elif choice2 == 5: 
                self.Manager_Storage_menu()
            else:
                print("You Selected an Inavlid Input!")

    def Password_Storage(self):
        self.storage = PasswordStorage()
        while True:
            print('--------Password Storage--------')
            print('1.Display All Passwords')
            print('2.Add a Password')
            print('3.Update a Password')
            print('4.Delete a Password')
            print('5.Return to menu')

            choice2 = int(input('Choice: '))

            if choice2 == 1:
                self.storage.view()

            elif choice2 == 2:
                self.clear_terminal()
                print('--------Add a Password--------')
                title = input('Input Title: ')
                password =input('Input Password: ')
                self.storage.add(title,password)
                
            elif choice2 == 3:
                self.clear_terminal()
                print('--------Update a Password--------')
                title = input('Input Title: ')
                new_password = input('Input New Password: ')
                self.storage.update(title,new_password)

            elif choice2 == 4:
                self.clear_terminal()
                print('--------Delete a Password--------')
                title = input('Input Title: ')
                self.storage.delete(title)

            elif choice2 == 5: 
                self.Manager_Storage_menu()
                
            else:
                print("You Selected an Inavlid Input!")

start = Main() 
start.start_menu()