# use list as stack, array and queue

# as list
l = [3, 4]
l += [5, 6]
print(l) #[3, 4, 5, 6]


# as stack
l.append(10) #[3, 4, 5, 6, 10]
l.pop() #[3, 4, 5, 6]


# as queue
l.insert(0, 5) # [5, 4, 5, 6]
l.pop(0, 5) # [5, 4, 5]