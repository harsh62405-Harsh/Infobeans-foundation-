arr = [1,5,3,7,2,8,4]
for i in range(len(arr)):
    if arr[i] > arr[i-1] and  arr[i] > arr[i+1]:
        print(f"{arr[i]} , 1 - Element is peak at index {i}")
        
    else :
        print(f"{arr[i]} , 0 - Element is not peak at index{i}")
