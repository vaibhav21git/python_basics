import re

# by using compile function pattern not need to be mentioned everytime
# pattern = "\\\\@[w./]+\.[w]+@[w..]\/"
# text = "\\@vaibhav.sachdeva/@elililly.com@21../"

# pattern = "\\\\[@][\w./]+@[\w.]+[\w@]+[\w.]+"
# text = "\\@vaibhav.sachdeva/@elililly.com@21.."

# x = re.findall(pattern, text)
# print(x)


# starts with ^[THE]
# ends with  [END]$

# match and search works like the same
# but match starts from the starting important point

# \s for spaces

# pattern = "^[\w]+[\w]+[\w]$"
# text = "VAibhAV"

# x = re.match(pattern, text)
# print(x)

# q1)

# 3 lowercase letters
# 3-5 digits
# one symbol
# up to two uppercase characters(optional)

# pattern = "^[a-z]{3}[0-9]{3,5}[^a-zA-Z0-9]{1}[A-Z]{0,2}$"
# text = "vai21031@Q"

# x = re.findall(pattern, text)
# print(x)

# if you want to print  whatever character 10 times then
# you will  do

# pattern = "^.{10}$"
# text = "baaaaaaaaaa"
# x = re.match(pattern, text)
# print(x)


# for email id

text = "vaibhav21nitrkl@gmail.com"
pattern = "^[\w]+@{1}[\w.]+"
x = re.findall(pattern, text)
print(x)
