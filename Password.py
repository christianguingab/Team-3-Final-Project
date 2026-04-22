#Handles creating the private variable password and provide methods to get and update passwords
class Password:
    def __init__(self,title,password):
        self.title = title
        self.__password = password   
        pass
    def get_password(self):
        return self.__password
    def set_password(self,new_pass):
        self.__password = new_pass