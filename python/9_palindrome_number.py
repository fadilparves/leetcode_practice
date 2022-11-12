""" Given an integer x, return true if x is a palindrome and false otherwise. 
    palindrome -> An integer is a palindrome when it reads the same forward and backward. For example, 121 is a palindrome while 123 is not.
    (Difficulty: Easy)


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
        num = x # Save the original number 
        if x < 0: # If the number is negative then return false
            return False
        
        reversed_num = 0 # Create a variable to store the reversed number
        while x != 0: # While the number is not 0 
            curr_digit = x % 10 # Get the last digit left from the original number

            reversed_num = 10 * reversed_num # Divide the reversed number with 10
            reversed_num = reversed_num + curr_digit # Add the current number that is the number obtained from the mod of 10 that returns the last digit from original number

            x = x // 10 # Remove the last number from the original digit, this repeats until the original number becomes 0

        if reversed_num != num: # Check if the reversed number is not the same as original number, then return False
            return False

        return True # If all is correct then it will return True indicating that the number is Palindrome

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

