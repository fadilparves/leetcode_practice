"""
Question:
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

Solutions:

Problem statement: Write a program that can find the square root of a given integer

Inputs: x -> target number that we want to get the square root value
Output: int -> the square root of the given x

Constraint: 
1) Number can be from 0 to 2 to the power of 31 - 1
2) Number is always positive (no complex number)

Brute Force Solution:

1) Loop through all the possible integers from 0 to x
2) Check if the current element * current elemnt is bigger than x
3) If true then last element was the answer
4) If the x is 0 then just return 0

class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 0:
            return 0

        for i in range(0, x+1):
            if i * i > x:
                return i - 1

Method: Linear Search
Time Complexity: O(n)
Space Complexity: O(1)

Better Solution:

1) Take the middle number from range of 0 to x
2) If the middle number * middle number is equal to x then return middle number
3) If the middle number * middle number is larger then x then move to left
4) If the middle number * middle number is smaller then x then move to right
5) If it didn't return any match, then take the nearest match which is last start index - 1

Method: Binary Search
Time Complexity: O(log n)
Space Complexity: O(1)

"""

class ExerciseSixtyNine:
    def mySqrt(self, x: int) -> int:
        nums = range(0, x + 1)
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] * nums[mid] == x:
                return nums[mid]
            elif nums[mid] * nums[mid] > x:
                end = mid - 1
            else:
                start = mid + 1
        
        return nums[start] - 1

case1 = 4 # Answer is 2
case2 = 8 # Answer is 2
case3 = 150 # Answer is 12
case4 = 0 # Answer is 0
case5 = 12632173 # Answer is 3554

E69 = ExerciseSixtyNine()

