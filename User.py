
class User:
    '''Manages the login process by testing against User/Password combination.'''
    #Should never have non private fields
    def __init__(self, login, password):
        self._login = login
        self._password = password

    def verifyLogin(self, login, password):
        '''Takes a login and password pair and returns login status depending on match'''
        if login == self._login:
            if password == self._password:
                self.loginStatus = "Pass"
            else:
                self.loginStatus = "Fail"
        else:
            self.loginStatus = "Fail"

        return self.loginStatus


login = "Something"

user1 = User("Bob", "password01")

print(login)
print(user1._login)


