# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# initial solution: 
# def getCountDict(str):
#   str_dict = {}
#   for i in str:
#     if str_dict.get(i) != None:
#       str_dict[i] = str_dict[i] + 1
#     else:
#       str_dict[i] = 1
#   return str_dict
        
# def canConstruct(ransomNote, magazine):
#   can_construct = True    
#   str1_dict = getCountDict(ransomNote.lower())
#   str2_dict = getCountDict(magazine.lower())
#   print(str1_dict)
#   print(str2_dict)
#   for k, v in str1_dict.items():      
#       if not str2_dict.get(k) or not (str2_dict.get(k) >= v):
#           can_construct = False
#           break
#   return can_construct
#initial solution end


#conclusion initial solution is better than second one, just create only initial dict and while looping second string decrease the count 

def canConstruct(ransomNote, magazine):
  temp = magazine  
  for i in ransomNote:  #a remove a from str2 
    index = temp.find(i)
    if index == -1: return False
    temp = temp[:index] + temp[(index+1):]    
  return True



# time complexity O(n * (m))
# space complexity O(m)

print('a', 'b')
print(canConstruct('a', 'b'))
print('a', 'ab')
print(canConstruct('a', 'ab'))
print('aa', 'ab')
print(canConstruct('aa', 'ab'))