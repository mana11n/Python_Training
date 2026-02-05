nums = [5, 4, -1, 7, 8]

current_sum = 0
max_value = nums[0]

for v in nums:
    current_sum += v
    max_value = max(max_value, current_sum)
    if current_sum < 0:
        current_sum = 0

print(max_value)
