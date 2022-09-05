# Find max and min in unsorted list

lst = [33, 3, 5, 66, 43, 2, 325, 4, 6, 56, 2]

# raza solution 1
def max_min(lst):
  return {'max': max(lst), 'min': min(lst)}

# raza solution 2
# def max_min(lst):
  #sort the list and return first and last index elements

print(max_min(lst))

#fixter solution
print(max(lst))
print(min(lst))
