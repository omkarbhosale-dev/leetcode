nums = [0,1,0,3,12]

n = len(nums)
left = 0
for i in range(0,n):
    if nums[i] != 0:
        print(i," ", left)
        nums[i], nums[left] = nums[left], nums[i]
        left += 1
print(nums)