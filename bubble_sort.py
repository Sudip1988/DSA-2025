# Sort an Array
# You are given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

# Example 1:

# Input: nums = [10,9,1,1,1,2,3,1]

# Output: [1,1,1,1,2,3,9,10]
# Example 2:

# Input: nums = [5,10,2,1,3]

# Output: [1,2,3,5,10]
# Constraints:

# 1 <= nums.length <= 50,000.
# -50,000 <= nums[i] <= 50,000
def bubble(nums : List[int]) -> List[int] :
    for i in range(nums) :
        j = 1
        while j < len(nums):
            if nums[i] > nums[j] :
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                



