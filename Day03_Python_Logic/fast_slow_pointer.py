nums = [10, 20, 30, 40, 50]

slow = 0   # slow pointer starts at index 0
fast = 0   # fast pointer also starts at index 0

# Move through the list
while fast < len(nums) and fast + 1 < len(nums):
    slow += 1   # slow moves 1 step
    fast += 2   # fast moves 2 steps

# After loop, slow points to the "middle" element
print(nums[slow])  # Output: 30
