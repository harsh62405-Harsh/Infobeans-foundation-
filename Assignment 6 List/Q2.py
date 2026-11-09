# Array: [5, 2, 8, 1, 9, 3]
arr = [5, 2, 8, 1, 9, 3]
max_value = arr[0]
min_value = arr[0]  
for i in range(len(arr)-1):
    # for j in range(i+1,i-2):
        if arr[i] > max_value:
         max_value = arr[i]
        else :
          min_value = arr[i]
print(f"Max : {max_value},Min :{min_value}")

      