"""
Question: 
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example:
Input: nums = [1,3,5,6], target = 7
Output: 4

Problem: Need a program that can find the target number index in a array given, 
         and if the target number is not found then we need to return the index that it could have been at in the array.

Constraints:
1) Length of the nums array is 1 -> 10 power of 4, which means there is no empty array provided
2) Number at a given index can be negative and positive up to 10 power of 4
3) Numbers inside the nums array are always distinct and the array is always sorted in ascending order
4) The target number has the same range as constraint no 2

Input 
nums = An array containing range of number in ascending order E.g [1,3,5,6]
target = A number, whose index is to be obtained from the nums array

Output
position = index of the target number in the nums array

Brute Force Solution:
1) Create a var pos with initial val 0
2) Check if the number at pos in the array is equal to target or if the number is bigger than target
3) If True then that is the answer and return that index as pos
4) If reached end of the array then add 1 to the pos indicating the target number is supposed to be last in the array

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pos = 0

        while pos < len(nums):
            if nums[pos] == target or nums[pos] > target:
                return pos
            
            pos += 1

        return pos

Method: Linear Search
Time Complexity: O(n) -> Time of run will increase as the number of input increase
Space Complexity: O(1) -> Constant space complexity as the only space taken is the pos variable

Better Solution with O(log n) time complexity:

1) Find the middle number from the list
2) If it matched the target number then return the mid index
3) If the middle number is bigger than target, then search the left side
4) If the middle number is smaller than target, then search the right side

Method: Binary Search
Time Complexity: O(log n) -> Time of run will increase as the number of input increase but as the array reduces to half by each iteration
Space Complexity: O(1) -> Constant space complexity as the only space taken is the start and end and mid_index variable

"""

class ExerciseThirteeFive:
    def searchInsert(self, nums: list[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid_index = (start + end) // 2
            if nums[mid_index] == target:
                return mid_index
            elif nums[mid_index] > target:
                end = mid_index - 1
            else:
                start = mid_index + 1
        
        return start

case1, target1 = [1,3,5,6], 5 # Output has to be 2
case2, target2 = [1,3,5,6], 2 # Output has to be 1
case3, target3 = [-2,-1,0,1,3,5,6], -1 # Output has to be 1
case4, target4 = [0], 5 # Output has to be 1
case5, target5 = [1,3,5,7,9], 9 # Output has to be 4

E35 = ExerciseThirteeFive()
out1 = E35.searchInsert(case1, target1)
out2 = E35.searchInsert(case2, target2)
out3 = E35.searchInsert(case3, target3)
out4 = E35.searchInsert(case4, target4)
out5 = E35.searchInsert(case5, target5)

print(out1, out2, out3, out4, out5) # 2, 1, 1, 1, 4