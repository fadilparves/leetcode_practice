"""
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