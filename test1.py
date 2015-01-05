def palindromeFor(word):
    for i in range(len(word)):
        if word[i] != word[len(word)-1-i]:
            return False
    return True

print(palindromeFor("ofo"))
print(palindromeFor("ofb"))
      






"""
Constraints:

1) Assuming we have a sensible user (i.e. they only put in strs)
"""

