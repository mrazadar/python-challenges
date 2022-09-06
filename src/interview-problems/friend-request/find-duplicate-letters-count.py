# Given a string find all duplicate letters in given phrase\
str = "aaabbccccdeeff"
output = "3a2b4c1d2e2f"

# raza solution
def find_duplicate_letters(s):
  _dict = {}  
  for i in s:
    if _dict.get(i) == None: 
      _dict[i] = 1
    else:
      _dict[i] += 1
  return ''.join(f'{value}{key}' for key, value in _dict.items())  

  #time complexity = 3n = O(n)
  #space complexity = O(1) 
print(find_duplicate_letters(str))



#mobeen solution
def letter_frequency(random_str):
  output = ''
  for letter in random_str:
    if letter in output:
      continue
    frequency = random_str.count(letter)
    output += f'{frequency}{letter}'
  return output

#time complexity = O(logn) * n = n(logn)
#space complexity = O(1)

print(find_duplicate_letters(str))
