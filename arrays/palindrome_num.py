class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num_str = str(x)
        return num_str == num_str[::-1]


my_sol = Solution()
my_sol.isPalindrome(121)
print(my_sol.isPalindrome(-121))

# without converting to string
def is_palindrome_math(n):
    if n < 0:
        return False

    original_num = n
    reversed_num = 0

    while n > 0:
        digit = n % 10
        reversed_num = (reversed_num * 10) + digit
        n = n // 10

    return original_num == reversed_num
print(is_palindrome_math(12321))
