# given n integer elements find duplicate values 
n = [3, 3, 4, 5, 2, 111, 5, 53, 2, 11, 4, 11, 1, 7, 56]

# solution Raza
def find_duplicate(elements):
  duplicates, seen = set(), set()
  for elm in elements: 
    if elm in seen:
      duplicates.add(elm)
    seen.add(elm)
  return list(duplicates)

# solution Finxter
# help([])
# find duplicate numbers in integer list
def findDuplicates(elements):
  temp = []
  duplicate = []
  for elm in elements:
    if(elm in temp):
      duplicate.append(elm)
    else:
      temp.append(elm)
  return duplicate

print(find_duplicate(n))
print(findDuplicates(n))

# remove duplicates
# raza implementation
def remove_duplicates(elements):
  uniq = []
  for elm in elements:
    if(elm not in uniq):
      uniq.append(elm)
  return uniq

print(remove_duplicates(n))

# Finxter implementation
def f_remove_duplicates(elements):
  return set(elements)

print(f_remove_duplicates(n))
