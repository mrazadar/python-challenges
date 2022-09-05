# check if two strings are anagrams 
# anagram meaning: a word or phrase made by transposing (re-arrange) the letters of another word.
# phrase meaning: a group of two or more words that express a single idea but do not form a complete sentence


# raza implementation
def checkAnagrams(str1, str2):
  if(len(str1) < len(str2)): False
  isAnagram = True
  for l in str1:
    if(isAnagram and not(l.lower() in str2.lower())):
      isAnagram = False
  
  for w in str2:
    if(isAnagram and not(w.lower() in str1.lower())):
      isAnagram = False
      
  return isAnagram
  # match 


# finxter implementation
def is_anagram(s1, s2):
  return set(s1.lower()) == set(s2.lower())


print("---------testing usage of in----------")
print('o' in 'they ran out the door.') #contains letter
print('ran out the' in 'they ran out the door.') #contains sub-str
print(3 in [2, 54, 6, 8, 4, 3]) #contains number in list
print(3 in {2, 54, 6, 8, 4, 3}) #contains number in set
#print({"name": 'ali'} in {"age": 23, 'name': 'ali'}) #contains item in Dict
for w in list('Ya jo aag ha, teri yado ki'.split()):
  print(w)
print("---------testing anagrams function----------")

print(checkAnagrams('secure', 'rescue'))
print(checkAnagrams('Hamlet', 'amleth'))
print(checkAnagrams('Glen, Duncen', 'Declan. Gunn'))

print(is_anagram('secure', 'rescue'))
print(is_anagram('Hamlet', 'amleth'))
print(is_anagram('Glen, Duncen', 'Declan. Gunn'))