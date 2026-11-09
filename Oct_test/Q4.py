'''
Q4. Sets — Common and Unique Elements (5 Marks)

Given two lists, find:
Elements common to both lists.
Elements that appear in either list but not in both.
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 60, 70]
Expected output:
Common elements: {30, 40}
Unique elements: {10, 20, 50, 60, 70}
'''

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 60, 70]

s1 = set(list1)
s2 = set(list2)

print("Union-:", s2.union(s1))
print("Intersection-:",s1.intersection(s2))
