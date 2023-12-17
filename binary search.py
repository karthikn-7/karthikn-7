# binary search algorithm

nums = [11,33,44,55,77,88,91]
# 0123456

target = 55
start = 0
end = len(nums)-1

while start <= end:
    mid = (start+end)//2
    if nums[mid] == target  :
        print(mid)
        break
    elif nums[mid] > target:
        end = mid-1
    elif nums[mid]< target:
        start = mid+1
        


