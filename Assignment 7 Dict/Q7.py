# 7. Find the number of key-value pairs in a dictionary without using len().

student = {"Name":"Harshit","Age":21,"Marks":90}
count = 0
for key in student:
    count +=1
print(f'Number of Key pair in the dictionary is : {count}')