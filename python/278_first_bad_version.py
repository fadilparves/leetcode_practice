"""

Problem: Build a program that can identify the first bad version in a list of version (basically array of int) and also replicate the action of minimizing the number of calls to API.

Constraints:
1) Bad version is either smaller or equal to n and bigger or equal to 1
2) N is bigger or equal to bad version and smaller or equal to 2 power of 31 - 1

Brute Force Solution:
1) Define a bad_index var and initiate it as 0
2) Loop through sorted array from 1 to n
3) Check if the current number is bad then return the number

Method: Linear Search
Time Complexity: O(n)
Space Complexity: O(1)

class Solution:
    def firstBadVersion(self, n: int) -> int:
        bad_index = 0
        for num in range(1, n+1):
            if isBadVersion(num) == True:
                return num

Issue: For each version, we need to hit the isBadVersion API and check if it is true or false

Better Solution:

1) Find the middle number from the sorted array of 1 to n
2) If the middle number is bad version then move the searching space to left
3) If not then move the searching space to right
4) Return the start index from search space

Method: Binary Search
Time Complexity: O(log n)
Space Complexity: O(1)

"""