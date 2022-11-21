"""
Given a positive integer num, write a function which returns True if num is a perfect square else False. (Easy)

Follow up: Do not use any built-in library function such as sqrt. 

Example 1:
Input: num = 16
Output: true

Example 2:
Input: num = 14
Output: false

Constraints:

1 <= num <= 2^31 - 1

"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        nums = range(1, num + 1)

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] * nums[mid] == num:
                return True
            elif nums[mid] * nums[mid] < num:
                start = mid + 1
            else:
                end = mid - 1
        
        return False