nums = [int(x) for x in input().split()]
min_idx = nums.index(min(nums))
max_idx = nums.index(max(nums))
nums[min_idx], nums[max_idx] = nums[max_idx], nums[min_idx]
print(*nums)