# 8. Remove all spaces from a string.

s = "My Name is Harshit Shrimali"
l = list(s)

for i in l:
  if i == " ":
    l.remove(i)

s = "".join(l)
print(s)