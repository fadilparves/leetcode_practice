"""
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "". 
    (Difficulty: Easy)

    Example:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

    Example:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

    Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.
"""

class ExerciseFourteen:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Get the shortest word in the string array
        shortest = min(strs, key=len) 
        # Loop the shortest word
        for i, ch in enumerate(shortest): 
            # Loop all the words from the string array
            for other in strs:
                # Check if the other words alphabet at the given index i is the same as the shortest at index i
                if other[i] != ch:
                    # If not the same then just return the shortest word to the given index with the same alphabet 
                    return shortest[:i]

        return shortest

case1 = ["flower","flow","flight"] # Answer should be "fl"
case2 = ["dog","racecar","car"] # Answer should be ""
case3 = ["flower","flow","flowed","flowers"] # Answer should be "flow"
case4 = ["flower","car","cart"] # Answer should be ""

E14 = ExerciseFourteen()
out1 = E14.longestCommonPrefix(case1)
out2 = E14.longestCommonPrefix(case2)
out3 = E14.longestCommonPrefix(case3)
out4 = E14.longestCommonPrefix(case4)

print(out1, out2, out3, out4) # fl, "", flow, ""