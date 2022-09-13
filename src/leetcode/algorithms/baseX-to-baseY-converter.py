# given a number in baseX convert that number to baseY
# e.g. given base16 (Hexadecimal) number 3D(16) convert it to base(10) 61 and vice verca.
# e.g. given base8 (Octal) number 47 convert it to base(10) 39 and vice versa.
# e.g. given base2 (Binary) binary number 1011002 convert it to base(10) 44 and vice verca.

from functools import reduce

HEX_LIST = {
  '0': 0,
  '1': 1,
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,
  '8': 8,
  '9': 9,
  'A': 10,
  'B': 11,
  'C': 12,
  'D': 13,
  'E': 14,
  'F': 15,
}

BASE_SET = {
  "Binary": 2,
  "Octal": 8,
  "Decimal": 10,
  "Hexadecimal": 16
}

# print(3 and 0)
def convertBase(num, baseX, baseY):
  
  #converting any other base to base10
  if baseY == BASE_SET["Decimal"]:    
    multiplier_values = []
    
    #reversed num array 531 [1, 3, 5]      
    num_list = [HEX_LIST.get(x) for x in str(num)][::-1]    
    for index, n in enumerate(num_list):        
      base_pow = baseX**index      
      multiplier_values.insert(0, (n * base_pow ))
    result = reduce(lambda x, y: x+y, multiplier_values)

  # converting base10 to any other base
  else: #aseX == BASE_SET["Decimal"]:
    # get base
    num = int(num)
    max_pow_value = 0
    n = 0    
    while n < num:
      n = baseY ** max_pow_value
      if n > num: 
        break      
      max_pow_value += 1
    
    max_multiplier = 0
    quotient_array = []
    reminder = num 
    # print('max_pow_value', max_pow_value, list(range(0, max_pow_value)))
    for pow in range(0, max_pow_value)[::-1]:
      max_multiplier = baseY ** pow;      
      # print(reminder, max_multiplier)
      quotient = int(reminder / max_multiplier)
      reminder = reminder - (max_multiplier * quotient)
      quotient_array.append(quotient)            
    result = ''.join(map(lambda x: list(HEX_LIST.keys())[list(HEX_LIST.values()).index(x)], quotient_array))
  return f'Result of converting Base({baseX}) to Base({baseY}) is {result}'

# print(list(HEX_LIST.values()).index(2))
print()

print(convertBase(47, BASE_SET["Octal"], BASE_SET["Decimal"])) #39
print(convertBase(101100, BASE_SET["Binary"], BASE_SET["Decimal"])) #44
print(convertBase("3D", BASE_SET["Hexadecimal"], BASE_SET["Decimal"])) #61
print(convertBase(150, BASE_SET["Decimal"], BASE_SET["Octal"])) #226
print(convertBase(39, BASE_SET["Decimal"], BASE_SET["Octal"])) #226
print(convertBase(61, BASE_SET["Octal"], BASE_SET["Binary"])) #3D
print(convertBase(61, BASE_SET["Decimal"], BASE_SET["Hexadecimal"])) #3D
print(convertBase(40, BASE_SET["Decimal"], BASE_SET["Binary"])) #3D

