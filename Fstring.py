# F STRINGS


# raw string is a absolute String

# but in normal string if you use backslash n then it will try to interpret

# method1  this is one way

import math

me = "vaibhav"
a1 = 3
a = "this is %s %s" % (me, a1)
print(a)

# method2 other way is using .format

a = "This is  {1} {0}"
b = a.format(me, a1)
print(b)

# output This is  3 vaibhav

# method 3 fstrings

a = f"this is {me} {a1} {math.cos(65)}"
print(a)


# fstrings has good readability
