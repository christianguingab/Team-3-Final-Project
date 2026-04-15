from PasswordStorage import PasswordStorage
from PasswordGenerator import PasswordGenerator 
from sys import exit
import os
import random

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
                self.clear_terminal()
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
        self.clear_terminal()
        while True:
            print('Please Choose From The Choices')
            print('1.Password Manager Menu')
            print('2.Password Storage Menu')
            print('3.End')
            choice1 = int(input('Choice: '))

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
                self.Strengthen_Manager()

            elif choice2 == 5: 
                self.Manager_Storage_menu()
            else:
                print("You Selected an Inavlid Input!")



    def Strengthen_Manager(self):
        print('Enter a password that will be strengthened')
        password = input('Password: ')
        while len(password) < 12 or not any(char.isdigit() for char in password) or not any(char in '!@#$%^&*()' for char in password) or not any(char.isalpha() for char in password):  
            password = password.capitalize() + str(random.randint(50,599)) + str(random.choice('!@#$%^&*()')) + random.choice('abcdefghijklmnopqrstuvwxyz')
        else:
            print('New password created: ' + password)
   
    def Password_Storage(self):
        self.storage = PasswordStorage()
        while True:
            print('Choose A Function')
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

def PasswordGenerator ():
    manager = PasswordGenerator()

    # 1. Generate Strong Password
    print(f"Generated: {manager.generate_strong_password()}")

    # 2. Analyze Password
    print(f"Strength: {manager.analyze_password('123abcABC!')}")

    # 3. Personalized Generator
    print(f"Personalized: {manager.personalized_generator(['Summer', '2024'])}")

    # 4. Strengthen Password
    print(f"Strengthened: {manager.strengthen_password('qwerty')}")

if __name__ == "__main__":
    main()
        
        

start = Main() 
start.start_menu()
