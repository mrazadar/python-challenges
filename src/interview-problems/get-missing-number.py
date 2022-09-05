# given n integers array, find the missing numbers between 1-n

# raza solution
def get_missing_numbers(nums, start, end):
  missing_nums = []
  for n in list(range(start, end+1)):
    print(n)
    if n not in nums:
      missing_nums.append(n)
  return missing_nums

# finxter solution
def f_get_missing_numbers(lst):
  return set(range(lst[len(lst)-1])[1:]) - set(l)



_min = 1
_max = 100
l = list(range(_min, (_max+1)));
print(max(l))
l.remove(50)
l.remove(99)
l.remove(77)
l.remove(17)
l.remove(100)
print(get_missing_numbers(l, _min, _max)) # [17, 50, 77, 99, 100]
print(f_get_missing_numbers(l)) # {17, 50, 77} #finxter solution doesn't tackle full-range and have exclusive last value i.e. 100 
print(set(range(60)))
# help(range)