import User

def UserTest(tag, user, login, password, expected):
    result = user.verifyLogin(login, password)
    if result == expected:
        passed = True
    else:
        passed = False

    if passed:
        return tag+" Passed"
    else:
        return tag+" Failed [E: "+expected+"] [A:"+result+"]"

user = User.User("John", "Password01")

print(UserTest("  No Match", user,"h4x0r","14m1337","Fail"))
print(UserTest("User Match", user,"John","14m1337","Fail"))
print(UserTest("Pass Match", user,"h4x0r","Password01","Fail"))
print(UserTest("Both Match", user,"John","Password01","Pass"))

    


