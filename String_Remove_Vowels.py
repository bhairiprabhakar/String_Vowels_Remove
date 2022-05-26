#Method 1: Using regular method

class Solution(object):
    def remove_vowels(self,s):
        s=s.lower().replace("a","")
        s=s.lower().replace("e","")
        s=s.lower().replace("i","")
        s=s.lower().replace("o","")
        s=s.lower().replace("u","")
        return s
obj=Solution()
print(obj.remove_vowels('I am Python Programming Code'))

#Method 2: Using list comprehension method
def rem_vowels(string):
    vowels=['a','e','i','o','u']
    result=[letter for letter in string  if letter.lower() not in vowels]
    result=''.join(result)
    print(result)
string='I am Python Programming Code'
rem_vowels(string)

#Method 3: Using regular expression method
import re
def rem_vowels(string):
    return(re.sub("[aeiouAEIOU]","",string))
string="I am Python Programming Code"
print(rem_vowels(string))

