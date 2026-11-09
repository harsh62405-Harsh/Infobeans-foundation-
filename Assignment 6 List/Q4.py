# Q.3 Write a program to reverse the array.
# arr = [5, 2, 8, 1, 9, 3]

# left = 0
# right = len(arr) - 1

# while left < right :
        
#         arr[left] , arr[right] = arr[right] , arr[left]
#         left += 1
#         right +=1

# print(arr)

arr = [5, 2, 8, 1, 9, 3]

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr)