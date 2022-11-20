"""
Question:
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

Problem: Build a program that will find the intersection integers between 2 arrays and the result has to be unique and the order doesn't matter

Constraints:
1) length of array 1 and array 2 is bigger or equal to 1 and smaller or equal to 1000
2) each element in both arrays can't be smaller then 0 and bigger then 1000

That means the return can be empty array if no match is found

Solution 1:

1) Create empty list called out
2) Loop over array 1 and then inner loop array 2
3) Check if the two elements are the same
4) If true and the element is not inside out
5) Add the element in the out array
6) Return the out array

Method: Linear Search
Time Complexity: O(n + m)
Space Complexity: O(1)

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2:
                    if num1 not in out:
                        out.append(num1)
        
        return out

Better Solution:

1) Declare empty array to store intersect integers
2) Sort the two arrays in ascending order
3) Loop the first array
3) Find the middle number based on nums2 array
4) If current nums1 number is equal to nums2 middle value and not added in out array then add that to out array
5) Elif current nums1 number is smaller than nums2 middle value then move to left
6) Else move to right

Method: Binary Search
Time Complexity: O(n log m)
Space Complexity: O(1)

"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        nums1.sort()
        nums2.sort()

        for num1 in nums1:
            start, end = 0, len(nums2) - 1

            while start <= end:
                mid = (start + end) // 2
                if num1 == nums2[mid] and num1 not in out:
                    out.append(num1)
                elif num1 < nums2[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
        
        return out

# Logic:
"""
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

sorted:
nums1 = [4,5,9]
nums2 = [4,4,8,9,9]

loop 0
num1 = 4
start, end = 0, 4
mid = 2 --> value is 8

so it goes into elif and then
start, end = 0, 1
mid = 0 --> value is 4
num1 == nums2[mid] --> 4 is == 4

4 is not in out yet so insert 4 into out

At this point out is = [4]

"""
