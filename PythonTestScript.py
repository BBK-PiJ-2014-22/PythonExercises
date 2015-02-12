from word_recursion import Word
import time

def testCharCount(word, character, result):
    word = Word(word)
    count = word.charCount(character)
    message = "Testing "+word.value+" with "+character+": " 

    if count == result:
        return message+"Passed"
    else:
        message += "Failed. Expected: "+str(result) + " Actual:"+str(count)
        return message

def testPalindrome(word, result):
    word = Word(word)
    message = "Testing "+word.value+" as palindrome: "
    response = word.isPalindrome()

    if response == result:
        return message + "Passed"
    else:
        message += "Failed. Expected: "+str(result) +" Actual:"+str(response)
        return message

        
#CharCount tests

start = time.time()

print("***Char Count Tests***")
print(testCharCount("apple", "a", 1))
print(testCharCount("apple", "p", 2))
print(testCharCount("apple", "d", 0))
print(testCharCount("apple", "A", 1))
print(testCharCount("apple", "pp", 0))
print(testCharCount("apple", "", 0))
print(testCharCount("apple", "e", 1))
print(testCharCount("apple", "apple", 0))
print(testCharCount("aaaaa", "a", 5))
print(testCharCount("", "a", 0))

end = time.time()
duration1 = end - start

print()


#Palindrome Tests
start = time.time()
print("***Palindrome Tests***")
print(testPalindrome("a",       True))
print(testPalindrome("aaa",     True))
print(testPalindrome("racecar", True))
print(testPalindrome("Racecar", True))
print(testPalindrome("denned",  True))
print(testPalindrome("notapal", False))
print(testPalindrome("race car",False))
print(testPalindrome("",        True))
end = time.time()
duration2 = end - start

#Time
print()
print("***Time***")
print("Char Count:", duration1)
print("Palindrome:", duration2)
print("Total time:", duration1+duration2)





