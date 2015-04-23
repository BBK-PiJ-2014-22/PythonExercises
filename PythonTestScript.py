import group3 as analyser
import time
import csv

def testCharCount(word, character, result):
    count = analyser.charCount(word, character)
    message = "Testing "+word+" with "+character+": " 

    if count == result:
        return message+"Passed"
    else:
        message += "Failed. Expected: "+str(result) + " Actual:"+str(count)
        return message

def testPalindrome(word, result):
    message = "Testing "+word+" as palindrome: "
    response = analyser.isPalindrome(word)

    if response == result:
        return message + "Passed"
    else:
        message += "Failed. Expected: "+str(result) +" Actual:"+str(response)
        return message

def performanceTest(testdata):
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
               "n","o","p","q","r","s","t","u","v","w","x","y","z"]

    start = time.time()
    for i in testdata:
        for l in letters:
            analyser.charCount(i, l)
    end = time.time()

    charcounttime = end-start

    start = time.time()
    for i in testdata:
        for n in range(30):
            analyser.isPalindrome(i)
    end = time.time()

    palindrometime = end-start

    return "charCount", charcounttime*1000, "isPalindrome", palindrometime*1000,"Total:",(charcounttime+palindrometime)*1000
    
def loadTestData(filename):
    with open(filename, 'r', newline = '', encoding='utf8') as testdatafile:
        reader = csv.reader(testdatafile,delimiter=',')
        testdata =  [row[0] for row in reader]
        return testdata
        
        

testdata = loadTestData('testdata.csv')    
       
#CharCount tests



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



#Palindrome Tests
print("***Palindrome Tests***")
print(testPalindrome("a",       True))
print(testPalindrome("aaa",     True))
print(testPalindrome("racecar", True))
print(testPalindrome("Racecar", True))
print(testPalindrome("denned",  True))
print(testPalindrome("notapal", False))
print(testPalindrome("race car",False))
print(testPalindrome("",        True))


#Time
print()
print("***Time***")
print(performanceTest(testdata))
