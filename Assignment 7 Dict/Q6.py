# 6. Remove a key from a dictionary using pop(). Handle the case where the
#    key does not exist.
student = {"Name":"Harshit","Age":21,"Marks":90}
# student.pop("Age")
print(f"Before Pop -: ", student)
if "City" in student:
        student.pop("City")
        print(f"Key Removed Successfullly ")
        print(student)
else:
    print(f"Key  is not Available in the Dictionary")
        # print(student.pop)
print(f"After Pop -: {student}")