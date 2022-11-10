""" Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    Example:    
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    Example:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    Example:
    Input: nums = [3,3], target = 6
    Output: [0,1]

   Constraints:
   2 <= nums.length <= 104
   -109 <= nums[i] <= 109
   -109 <= target <= 109
   Only one valid answer exists. """

class ExerciseOne:
    def twosum(self, nums: list[int], target: int) -> list[int]:
        # First we will create empty hashmap, in python this is known as dictionaries
        hashmap = {}
        # Then we will iterate over the range of elements in the array nums
        for i in range(len(nums)):
            # We will get the y of the target, that means we take the target and subtract that with the current number from the nums array
            complement = target - nums[i]
            # Check if the complement is already available, if it is there then we take that complement index and current index and return back as the answer
            if complement in hashmap:
                return [i, hashmap[complement]]
            # Else we add that complement as key with the index as value
            hashmap[nums[i]] = i

arr1, target1 = [2,7,11,15], 9 # Output should be [0,1] or [1,0]
arr2, target2 = [3,2,4], 6 # Output should be [1,2] or [2,1]
arr3, target3 = [3,3], 6 # Output should be [0,1] or [1,0]
arr4, target4 = [2,11,7,15], 9 # Output should be [0,2] or [2,0]
arr5, target5 = [2,11,15,7], 9 # Output should be [0,3] or [3,0]

Eone = ExerciseOne()
out1 = Eone.twosum(arr1, target1)
out2 = Eone.twosum(arr2, target2)
out3 = Eone.twosum(arr3, target3)
out4 = Eone.twosum(arr4, target4)
out5 = Eone.twosum(arr5, target5)

print(out1, out2, out3, out4, out5) # Output from run -> [1, 0] [2, 1] [1, 0] [2, 0] [3, 0]