# selection sort

arr = [2,4,5,1,3]
ind = [0,1,2,3,4]
for pos in range(len(arr)-1):
    min = pos
    for i in range(pos+1,len(arr)):
        if arr[i] < arr[min]:
            min = i
    arr[pos],arr[min] = arr[min],arr[pos]

print(arr)
