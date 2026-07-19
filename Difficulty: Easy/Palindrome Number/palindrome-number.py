class Solution:
    def isPalindrome(self, n):
        n = abs(n)          # Ignore negative sign

        original = n
        reverse = 0

        while n != 0:
            digit = n % 10
            reverse = reverse * 10 + digit
            n = n // 10

        return original == reverse