""" Given an integer x, return true if x is a palindrome and false otherwise. 
    palindrome -> An integer is a palindrome when it reads the same forward and backward. For example, 121 is a palindrome while 123 is not.
    
    Example:
    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.
    
    Example:
    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

    Example:
    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

    Constraints:

    -231 <= x <= 231 - 1
    """

class ExerciseNine:
    def isPalindrome(self, x: int) -> bool:
        num = x # Save the 
        if x < 0:
            return False
        
        reversed_num = 0
        while x != 0:
            curr_digit = x % 10

            reversed_num = 10 * reversed_num
            reversed_num = reversed_num + curr_digit

            x = x // 10

        if reversed_num != x:
            return False

        return True

case1 = 121 # True is expected
case2 = -121 # False is expected
case3 = 10 # False is expected
case4 = -10 # False is expected
case5 = 55 # True is expected

Enine = ExerciseNine()
out1 = Enine.isPalindrome(case1)
out2 = Enine.isPalindrome(case2)
out3 = Enine.isPalindrome(case3)
out4 = Enine.isPalindrome(case4)
out5 = Enine.isPalindrome(case5)

print(out1, out2, out3, out4, out5)

