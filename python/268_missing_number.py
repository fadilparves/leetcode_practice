"""
Problem: Write a program that can take a list of num and then find the missing number in the range
         of the nums.

Constraint:
1) So n is the length of nums array
2) n can be more or equal to 1 and less or equal to 10 power of 4
3) element at a given index can never be smaller than 0 and bigger than n

Solution:
1) Sort the nums in ascending order
2) Take the middle index
3) Check if the middle number is the same value as middle index
4) If it is true then move right by taking the middle index - 1
5) Else move the left by taking middle index + 1
6) Finally return the left value

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > mid:
                right = mid - 1
            else:
                left = mid + 1
        
        return left

Method: Binary Search
Time Complexity: O(n log n) -> Because of sorting
Space Complexity: O(1)

Better Solution:
Use bitwise operation
Reference: https://leetcode.com/problems/missing-number/solutions/1585333/python-the-best-explanation-bitwise-and-sum/

"""

class ExerciseTwoHundredSixtyEight:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0 

        #XOR result with complete number sequence
        for number in range(len(nums) + 1 ) : # 0, 1, 2 ,3
                result ^= number
                
        # Essentially now result = ( 0 ^ 0 ^ 1 ^ 2 ^ 3)

        #XOR result with values in nums
        for num in nums : # 3,0,1
                result ^= num
                
        # result = ( 0 ^ 0 ^ 1 ^ 2 ^ 3) ^ ( 3 ^ 0 ^ 1)

        # XOR of same values cancel each other out 

        # result = (0) ^ (0 ^ 0)  ^ (1^1) ^ (2) ^ (3^3)
        # result =  0 ^ 0 ^ 0 ^ 2 ^ 0
        # result = 2

        return result # 2


