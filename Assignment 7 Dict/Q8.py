# 8. Calculate the sum of all numeric values in a dictionary.

student = {"Name":"Harshit","Age":21,"Marks":90}
total = 0 
for integer in student:
#     if isinstance(student[integer], (int, float)):
#         total += student[integer]
# print(f'Sum of all numeric values in the dictionary is: {total}')

      if type(student[integer]) in (int, float):
            total += student[integer]
print(f"Sum of all the Numeric Values in the Dictionary is :{total}")