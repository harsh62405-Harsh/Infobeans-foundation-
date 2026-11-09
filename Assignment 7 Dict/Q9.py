# 9. Find the key associated with the largest value in a dictionary.

student = {"Name":33,"Age":21,"Marks":90}
max_key = 0
for key in student:
    for value in student:
       if student[key] > max_key:
        max_key = student[key]
        max_value_key = key
print(max_value_key)


