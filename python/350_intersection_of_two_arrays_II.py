"""
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
(Easy)

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

Method: Binary Search
Time Complexity: O(n log m)
Space Complexity: O(m)

"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = [] # 

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        nums1.sort()
        nums2.sort()

        for num1 in nums1:
            start, end = 0, len(nums2) - 1

            while start <= end:
                mid = (start + end) // 2
                if num1 == nums2[mid]:
                    out.append(num1)
                    nums2.pop(mid)
                    break
                elif num1 < nums2[mid] :
                    end = mid - 1
                else:
                    start = mid + 1

        return out

    # Q1: What if the given array is already sorted? How would you optimize your algorithm?
    # A1: Binary Search as it will not require the sorting and it can be done in time complexity of O(n log m)

    # Q2: What if nums1's size is small compared to nums2's size? Which algorithm is better?
    # A2: Binary Search as we will only loop the smaller array and use binary search on the bigger array which will reduce the time complexity for the bigger array by reducing the number of iteration to search for the same number which reduces the time complexity to O(n log m)

    # Q3: What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
    # A3: For this I would prefer to use hash maps as this will allow to keep track of the number the numbers occured when we use the subset of the data to process each chunk by loading a chunk from the disk to memory.
