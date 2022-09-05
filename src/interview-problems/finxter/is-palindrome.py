# palindrome meaning: a word or phrase that can be read the same way either forward or backward.
# "Racecar," "radar," "stats," "eye," "Mom" — these are examples of palindromes, 
# and if you reverse the letters, the words will stay the same. 
# Palindrome comes from a Greek word that means “running back again,”

def is_palindrome(phrase):
  reverse = ''.join(list(reversed(phrase)))
  return phrase.lower() == reverse.lower()
  # return True for i, k in phrase, revers: if i == k


# finxter solution will not work for case sensetive strings
def f_is_palindrome(phrase):
  return phrase == phrase[::-1]


some_str = 'some string'
# extended slicing
# the slicing syntax has supported an optional third ``step'' or ``stride'' argument. 
# For example, these are all legal Python syntax: L[1:10:2], L[:-1:1], L[::-1]. 
# This was added to Python at the request of the developers of Numerical Python, 
print(some_str[::-1])
print(''.join(list(reversed('some string'))))
print(some_str[0:]) #whole string
print(some_str[0:4]) #some
print(some_str[0:-6]) #some
print(some_str[0:4:2]) #sm # return even indexes between that slice
print(some_str[0::2]) #sm tig # return even indexes between that slice
print(some_str[::-1]) # return the revere string


print(is_palindrome('Racecar'))
print(f_is_palindrome('stats'))