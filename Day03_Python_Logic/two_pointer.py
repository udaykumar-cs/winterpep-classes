
nums = [2, 7, 11, 15]
target = 9

# Two pointers approach
left = 0                 # start of the list
right = len(nums) - 1    # end of the list

while left < right:      
    s = nums[left] + nums[right]  # sum of two numbers at pointers
    
    if s == target:               # if sum matches target
        print(nums[left], nums[right])  # print the pair
        break                     # stop, as we found the answer
    elif s < target:              # sum too small -> move left pointer right
        left += 1
    else:                         # sum too big -> move right pointer left
        right -= 1
