from glob import glob


globvar = 10
my_dict = {"name": "saleem"};
def read1():
    print(globvar)
def write1():
    my_dict['name'] = "jameel"
    global globvar
    globvar = 5
def write2(num):
    num = 15
    print("inside func", num)


print(read1())
print(write1())
print(read1())
print(write2(globvar))
print(read1())
print(my_dict)
    
# def reciprocal(num):
#     try:
#       if num == 0: raise ZeroDivisionError('cannot divide by zero.')
#       r = 1/num
#     except Exception as e:
#         print('Exception caught:', e)
#         return
#     return r

# print(reciprocal(10))
# print(reciprocal(0))

# a = ['x','y','z']
# del a[a.index('y')]
# print(a)
# import asyncio

# async def asyncFunc():
#   print('hello1')
#   await asyncio.sleep(5)
#   print('hello2')

# asyncio.run(asyncFunc())

# print('+-----------Interview Questions--------------+')
# # check if list contains integer x
# l = [3, 3, 4, 5, 2, 111, 5, 53, 2, 11, 4, 11, 1, 7, 56]
# n = 111
# print(n in l)


# print('+-----------NumPy--------------+')
# import numpy as np 

# print(np.var(np.array([1, 2, 3, 4, 5]))) #varience
# print(np.std(np.array([1, 2, 3, 4, 5]))) #standar deviation, tells the avg marginal difference from the mean
# print(np.max(np.array([1, 2, 3, 4, 5])))
# print(np.argmax(np.array([1, 2, 3, 4, 5])))
# print(np.nonzero(np.array([1, 2, 0, 0, 5])))

# print('+-----------Functions & Tricks--------------+')

# #sequence arguments
# def f(x, y, z): return x + y * z

# print(f(*[1, 3, 4]))
# print(f(**{'x': 3, 'y': 1, 'z':4})) #7

# # extended unpacking / js destructuring
# a, *b = [1, 3, 4, 5, 6]

# print(a, b)

# x = {'alice': 18}
# y = {'bob': 27, 'anna': 23}
# z = {**x, **y, 'bob': 43}
# print(z)

# swapping variables

# a, b = 'Jane', 'Alice'
# a, b = b, a
# print(a, b)
# help(sorted)

# print(list(zip(['Alice', 'Anna'], ['Bob', 'Jon', 'Frank'])))
# print(list(zip(*[('Alice', 'Bob'), ('Anna', 'Jon')])))

# print(list(enumerate(['Alice', 'Bob', 'Anna', 'Jon'])))

# import this



# l = list(map(lambda x: x[0], ['red', 'green', 'yellow']))
# print(l[1])

# l1 = list(map(lambda x, y: str(x) + ' | ' + y, [1,2,3], ['red', 'green', 'yellow']))
# print(l1)

# print(', '.join(['Alice', 'bob', 'timmoty']))

# print(list(filter(lambda x: True if x<=17 else False, [1, 15, 17, 19, 18])))

# print(" \n \t 42 \t ".strip())

# unsortArray = [4,7,34, 2, 5, 23, 21, 12]
# print(sorted(unsortArray, reverse=True))
# print(unsortArray)

# print(sorted(unsortArray, key=lambda x: False if x==34 else x))
# print('+-----------List comprehnsion--------------+')

# l = [('Hi ' + x) for x in ['Alice', 'Bob', 'Pete']]
# print(l)

# l2 = [(x * y) for x in range(3) for y in range(3) if x>y]
# print(l2)

# print('+-----------Set comprehnsion--------------+')
# squares = {x**2 for x in [0,2,4] if x < 4}

# print(squares)

# print('+-----------Set, Dictionary--------------+')

# basket = {'apples', 'bananas', 'oranges', 'eggs'}
# # basket.add('apples') #silently ignore duplicating values
# print(basket)
# sameBasket = (['apples', 'bananas', 'oranges', 'eggs'])
# print(sameBasket)

# # Dictionary

# calories = {'apples': 52,  'bananas': 72, 'choco': 555}

# for k, v in calories.items():
#   print(k, v);

# print(calories['apples'] < calories['choco'])
# calories['cappu'] = 74

# print(calories['bananas'] < calories['cappu'])

# print('apple' in calories.keys())
# print(52 in calories.values())

# for k, v in calories.items():
#   print(k) if v > 100 else None 

# print('eggs' in basket)
# print('mushroom' in basket)

# print('+-----------Stack--------------+')

# stack = [3]
# stack.append(42)

# print(stack)

# stack.pop()

# print(stack)

# print('+-----------List--------------+')

# #List, a container data type that stores a sequence of elements

# class Car:
#   def __init__(self, make, model, color):
#     self.make = make
#     self.model = model
#     self.color = color

#   def printCar(self):
#     print(self.make, self.color, self.model)

#   @staticmethod
#   def printAllCars(carList):
#     for car in carList: 
#       car.printCar()

# carList = [
#   Car('BMW', 2014, 'yellow'),
#   Car('Toyota', 2015, 'white'),
#   Car('Hyndai', 2017, 'orange'),
#   Car('Mercedes', 2006, 'blue'),
#   Car('Honda', 2014, 'gray'),
# ]

# Car.printAllCars(carList)
# # print('------Insert Mercides 2nd index---------')
# # # carList.insert(2, c4)
# # # carList.append(c3)

# # Car.printAllCars(carList)

# print('------reverce the order---------')
# carList.reverse()
# Car.printAllCars(carList)

# print('------Sort the carList---------')

# carList.sort(key=lambda x: x.make)

# Car.printAllCars(carList)

# print(carList.index(carList[3]))
# print('+-----------Classes--------------+')
# from abc import ABC, abstractmethod


# class Animal(ABC):
#   species = ['Canis', 'Lupus']

#   @abstractmethod
#   def bark(self, freq):
#     pass
  
# # animal = Animal()

# class Cat(Animal):
#   def __init__(self, name, color):
#     self.name = name
#     self.state = 'chilling'
#     self.color = color

#   def bark(self, freq):
#     for i in range(freq):
#       print("[ " + str(i) + " " + self.name 
#       + " ]: Meaoo!")


# mao = Cat('Tommy', 'gray')

# print(mao.name)
# print(mao.color)
# print(mao.state)

# mao.bark(2)


# class Dog(Animal):
  
#   def __init__(self, name, color):
#     self.name = name
#     self.state = 'sleeping'
#     self.color = color
  
#   def command(self, x):
#     if x == self.name:
#       self.bark(2)
#     elif x == "sit":
#       self.state = "sit"
#     else:
#       self.state = "wag tail"


#   def bark(self, freq):
#     for i in range(freq):
#       print("[ " + str(i) + " " + self.name 
#       + " ]: woof!")


# bello = Dog('bello', 'black')
# alice = Dog('alice', 'white')

# print(bello.color) 
# print(alice.color) 

# bello.bark(1)

# print(bello.state) 

# bello.command("sit")
# print(bello.state) 

# bello.bark(2)

# bello.command("no")

# print(bello.state) 

# bello.bark(3)
# bello.command("no")

# print(bello.state) 

# bello.command('bello')

# print(len(bello.species))

# print(len(bello.species) == len(alice.species))

# bello.species += ["Wulf"]

# for specie in bello.species:
#   print(specie)





# print('+-----------KeyWords--------------+')

# # False, True data values from the type Boolean
# print(False == (1 > 2))
# print(True == (2 > 1))

# # Logical Operators: 
# x, y = True, False
# print((x or y) == True)
# print((x and y) == False)
# print((not y) == True)

# # break -> Ends loop prematurely
# while(True): 
#   break #no infinite loop
# print("hello world!")

# # continue -> Finishes the current loop iteration
# # while(True): 
# #   continue #infinite loop 
# # print("43") #dead code (control will never reach here)

# # Class & Function

# class Beer: 
#   def __init__(self) -> None:
#     self.content = 1.0
#   def drink(self):
#     self.content = 0.0
#   def beerLevel(self):
#     print(self.content)

# becks = Beer()
# becks.beerLevel()
# becks.drink()
# becks.beerLevel()


# # if elif else
# x = int(input("Your Value: "))
# if x > 3: print("Big")
# elif x == 3: print("Medium")
# else: print("Small")

# for, while loops
# for i in [0, 1, 2, 3, 4, 5]: 
#   print(i)

# j = 1
# while j <= 10:
#   print(j)
#   j = j + 1

# # in, checks whether element is in the sequence
# print(42 in [2, 34, 42])

# # is, checks whether both variables points to the same object
# x = y = 3

# print(x is y)

# print([3] is [3])

# # lambda, function with no name, anonymous function
# print((lambda x: x+3)(3)) # = 6IIEF (immidiately invoked function)

# # return, terminates the execution of the function and returns the proceeding value
# def incrementor(x):
#   return x + 1

# print(incrementor(3))


# # print('+-----------String--------------+')
# s = "The youngest pope was 11 years old"
# print(s[0]) #T
# print(s[1:3]) #he
# print(s[-3:-1]) #start from 4th last index till second last= ol  
# print(s[-3:]) #start from last index = old  

# x = s.split()
# x = s.split(' ')
# print(x)

# ## 5. Most important string methods
# y = " This is lazy \t\n "
# print(y.strip()) #remove the whitespaces
# print("DrDr".lower()) #drdr
# print("attitude".upper()) #ATTITUDE
# print('smartphones'.startswith('smart'))
# print('smartphones'.endswith('phones'))
# print('another'.find('other'))
# print('cheat'.replace('c', 'w'))
# print('cheat'.replace('ch', 'm'))
# print(','.join(["F", "B", "I"]))
# print(len(x))
# print(len('Rumpelstiltskin'))
# print("ear" in "earth")
# print("ear" + " will" + " be teared.")


# print('+-----------Integer / Float--------------+')
# x, y = 2, 3

# print(x + y) 
# print(x - y) 
# print(x * y)
# print(x / y)
# print(x // y)
# print(x % y)
# print(-x)
# print(abs(-x))
# print(int(3.9))
# print(float(3))

# print(x ** y) # pow = 2*2*2 = 8
# print(x * x * x) # pow = 2*2*2 = 8
# print(x ** 4) # pow = 2*2*2*2 = 16

# print('+-----------Truthy Values--------------+')

# x, y = True, False

# print(None and y or x)

# print(None or 0 or 0.0 or '' or {} or [] or set() or 5)

# print(x) #true
# print(y) #false
# print(not x)
# print(x and not y) #true
# print(not x and y or x) #true

# print(not y and 3);