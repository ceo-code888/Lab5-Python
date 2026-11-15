nums = [int(x) for x in input().split()]
non_zero_pos = 0

for i in range(len(nums)):
    if nums[i] != 0:
        nums[non_zero_pos], nums[i] = nums[i], nums[non_zero_pos]
        non_zero_pos += 1

print(*nums)