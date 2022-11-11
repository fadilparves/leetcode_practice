"""
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M. (Difficulty: Easy)

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000

    For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, 
    which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
    Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
    The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    * I can be placed before V (5) and X (10) to make 4 and 9. 
    * X can be placed before L (50) and C (100) to make 40 and 90. 
    * C can be placed before D (500) and M (1000) to make 400 and 900.

    Given a roman numeral, convert it to an integer.

    Example:
    Input: s = "III"
    Output: 3
    Explanation: III = 3.

    Example:
    Input: s = "LVIII"
    Output: 58
    Explanation: L = 50, V= 5, III = 3.

    Example:
    Input: s = "MCMXCIV"
    Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

    Constraints:

    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].

"""

# Answer 1: Slower

class ExerciseThirteen:
    def romanToInt(self, s: str) -> int:
        # Create dict that can be used to map the roman alphabet with its integer
        mapper = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        # Declare num variable with default value as the last alphabet integer from the roman number
        num = mapper[s[-1]]

        # Define the slow and fast pointer
        left, right = len(s) - 2, len(s) - 1

        # While we havent got to the end of fast pointer
        while left >= 0:
            # Get the integer for the slow and fast pointer from the mapper
            left_num = mapper[s[left]]
            right_num = mapper[s[right]]

            # If the left number is smaller than right number then we want to substract the left number from the num
            if left_num < right_num:
                num -= left_num
            else:
                num += left_num
            
            # Then we move the slow and fast pointer by one back
            left -= 1
            right -= 1

        return num

case1 = "III" # Expected is 3
case2 = "LVIII" # Expected is 58
case3 = "MCMXCIV" # Expected is 1994

E13 = ExerciseThirteen()
out1 = E13.romanToInt(case1)
out2 = E13.romanToInt(case2)
out3 = E13.romanToInt(case3)

print(out1, out2, out3) #3, 58, 1994

# Faster solution
class ExerciseThirteenFast:
    def romanToInt(self, s: str) -> int:
        mapper = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        for i in range(len(s)-1, 0, -1):
            if mapper[s[i-1]] < mapper[s[i]]:
                num -= mapper[s[i-1]]
            else:
                num += mapper[s[i-1]]
            
        return num + mapper[s[-1]]

E13F = ExerciseThirteenFast()
out1 = E13F.romanToInt(case1)
out2 = E13F.romanToInt(case2)
out3 = E13F.romanToInt(case3)

print(out1, out2, out3) #3, 58, 1994