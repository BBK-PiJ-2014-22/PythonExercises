class User:
    '''Manages the login process by testing against User/Password combination.'''
    #Should never have none private fields
    def __init__(self, login, password):
	self._login = login
	self._password = password

    def verifyLogin(login, password):
        '''Takes a login and password pair and returns login status depending on match'''
	if login = self._login:
	    if password = self._password:
		self.loginStatus = "Pass"
	    else:
		self.loginStatus = "Wrong Password"
	else:
	    self.loginStatus = "Wrong User"

        return self.loginStatus





		

