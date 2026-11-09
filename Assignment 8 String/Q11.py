# 11. Count how many times a particular character occurs.

s = "My Name is Harshit Shrimali"
d = {}

for i in s:
  d[i] = d.get(i,0)+1

print(d)