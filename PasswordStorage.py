from Password import Password
import os

#Handles storing, viewing, adding, updating, and deleting passwords
class PasswordStorage(Password):
    def __init__(self):
        self.__passwords={}
    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    def view(self):
        if len(self.__passwords) ==0:
            self.clear_terminal()
            print('You currently have no passwords stored.\n')
        else:
            self.clear_terminal()
            print('--------Stored Passwords--------')
            print('Title    Password')
            print('--------------------------------')
            for title,password in self.__passwords.items():
                print(title,':',password.get_password()) 
            print('\n')
    def add(self,title, password):
        if title in self.__passwords:
            print('Title already exists, please create another one')
        else:
            self.__passwords[title]=Password(title,password)
            self.clear_terminal()
            print("Successfully Added the Password.\n")
    def update(self,title,new_password):
        if title not in self.__passwords:
            self.clear_terminal()
            print("That title and password does not currently exist.\n")
        else:
            self.__passwords[title].set_password(new_password)
            self.clear_terminal()
            print("Successfully Updated the Password.\n")
    def delete(self,title):
        if title in self.__passwords:
            del self.__passwords[title]
            self.clear_terminal()
            print("Successfully Deleted the Password.\n")
        else:
            self.clear_terminal()
            print("That title does not currently exist.\n")