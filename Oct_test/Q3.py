'''
Q3. Lists — Second-Largest Distinct Element (5 Marks)

Given a list of integers, find the second-largest distinct element without using sort(), sorted(), or max().

numbers = [12, 45, 7, 45, 30, 22, 30]

Expected output: 30
'''

l = [12, 45, 7, 45, 30, 22, 30]
largest = l[0]
second_largest = l[0]
for i in range(len(l)):
    if len(l) < 2:
        print("List don't have second largest element")
        break
    else:
        current = l[i]
        if current > largest:
            second_largest = largest
            largest = current
        elif current > second_largest and current < largest:
            second_largest = current
print(f"Second largest element is {second_largest}")
