# compute the intersection of two lists
# intersection Ω of two sets A and B is the set of all those elements which are common to both A and B. 
# The union of two sets is a set containing all elements that are in A or in B (possibly both). For example, {1,2}∪{2,3}={1,2,3}.

l1, l2 = [1, 2, 4, 6, 8, 11], [1, 2, 5, 9, 8, 11]

# raza solution
def intersect(lst1, lst2):
  intersect_list = []
  for n in lst1:
    if n in lst2:
      intersect_list.append(n)
  return intersect_list


# fixter solution
def f_intersect(lst1, lst2):
  res, lst2_copy = [], lst2[:]
  for el in lst1:
    if el in lst2_copy:
      res.append(el)
      lst2_copy.remove(el)
  return res


print(intersect(l1, l2))
print(f_intersect(l1, l2))
