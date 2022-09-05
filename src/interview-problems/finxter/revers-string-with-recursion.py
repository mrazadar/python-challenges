# reverse string using recursion 
# so we will reconstruct the list in reverse order from last index i.e. n-1

some_str = 'It will be hard'

# raza & finxter solution
def reverse(s):
  if len(s) <= 1: return s
  return reverse(s[1:]) + s[0]

# Call Stack                      #Call Stack returns
# 1: reverse(t will be hard) + I  #drah eb lliw tI
# 2: reverse( will be hard) + t   #drah eb lliw t
# 3: reverse(will be hard) + ' '  #drah eb lliw 
# 4: reverse(ill be hard) + w     #drah eb lliw 
# ...
# ...
# ...
# ...
# ...
# 13: reverse(rd + a)    #dra 
# 14: reverse(d + r)     #dr
# 14: reverse(d)         #d
