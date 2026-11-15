nums = [int(x) for x in input().split()]
stop_val = int(input())

for num in nums:
    if num == stop_val or num == 0:
        break
    if num % 2 == 0:
        print(num)