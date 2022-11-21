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
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        out = [] # Declare empty array to store the output

        if len(nums2) < len(nums1): # If the nums2 array is smaller then nums1 then we switch the two arrays
            nums1, nums2 = nums2, nums1

        nums1.sort() # Sort array nums1 in ascending order
        nums2.sort() # Sort array nums2 in ascending order

        for num1 in nums1: # Loop each element in nums1
            start, end = 0, len(nums2) - 1 # Start and end for the binary search

            while start <= end: # While the start is not overflown the end
                mid = (start + end) // 2 # Find the middle point of the search space
                if num1 == nums2[mid]: # If the middle number of the search space is equal to current lopped number from nums1
                    out.append(num1) # Append to the out array
                    nums2.pop(mid) # Remove the matched element from future search space
                    break # Break the while loop and go for the next num in nums1
                elif num1 < nums2[mid] : # If the num1 is smaller than current mid point of search space then move the end toward lefts
                    end = mid - 1 
                else: # Else move the start to the right
                    start = mid + 1

        return out # Return the output

c_1_nums1, c_1_nums2 = [1,2,2,1], [2,2]
c_2_nums1, c_2_nums2 = [4,9,5], [9,4,9,8,4]
c_3_nums1, c_3_nums2 = [1], [2]
c_4_nums1, c_4_nums2 = [4,4,4,3,2,1,1], [4,4,4,1,1]
c_5_nums1, c_5_nums2 = [3,1,2], [1,1]

E350 = Solution()
out1 = E350.intersect(c_1_nums1, c_1_nums2)
out2 = E350.intersect(c_2_nums1, c_2_nums2)
out3 = E350.intersect(c_3_nums1, c_3_nums2)
out4 = E350.intersect(c_4_nums1, c_4_nums2)
out5 = E350.intersect(c_5_nums1, c_5_nums2)

print(out1, out2, out3, out4, out5) # [2, 2] [4, 9] [] [1, 1, 4, 4, 4] [1]g


# Q1: What if the given array is already sorted? How would you optimize your algorithm?
# A1: Binary Search as it will not require the sorting and it can be done in time complexity of O(n log m)

# Q2: What if nums1's size is small compared to nums2's size? Which algorithm is better?
# A2: Binary Search as we will only loop the smaller array and use binary search on the bigger array which will reduce the time complexity for the bigger array by reducing the number of iteration to search for the same number which reduces the time complexity to O(n log m)

# Q3: What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
# A3: For this I would prefer to use hash maps as this will allow to keep track of the number the numbers occured when we use the subset of the data to process each chunk by loading a chunk from the disk to memory.
