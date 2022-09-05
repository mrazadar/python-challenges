# Find pairs of integers in list so that their sum is equal to integer x
# given n number of elements
# find pairs whose sum is equel to x

n = [3, 3, 4, 5, 2, 6, 5, 10, 2, 9, 4, 8, 1, 7, 12]
x = 9

# raza solution
def find_pairs(nums, x):
  pairs = []  
  for i in range(0, (len(nums)-1)): #0, 1, 2, 3....
    for y in range(i+1, (len(nums)-1)): #1, 2, 3...(n-1)
      prev = nums[i]
      current = nums[y]
      if x == (prev+current):
        # add pair
        pair = [prev, current]
        print(x, pair)
        pairs.append(pair)
  return pairs;

print(find_pairs(n, x))
# print(find_pairs(n, 13))
# print(find_pairs(n, 11))


# finxter solution
# enumerate meaning: mention a number of things one by one.. 
def f_find_pairs(l, x):
  pairs = []
  for (i, elm_1) in enumerate(l):
    for (j, elm_2) in enumerate(l[i+1:]):
      if elm_1 + elm_2 == x:
        pairs.append((elm_1, elm_2))
  return pairs
print('----finxter solution------')
print(f_find_pairs(n, x))
