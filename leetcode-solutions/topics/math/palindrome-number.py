"""
9. Palindrome Number
https://leetcode.com/problems/palindrome-number/

Pattern: Math (reverse half the digits)
Time: O(log n) | Space: O(1)

Approach:
Negative numbers and numbers ending in 0 (except 0 itself) can
never be palindromes. Otherwise, reverse only the second half of
the number and compare it to the remaining first half — avoids
building the full reversed number and risking overflow.
"""

def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    return x == reversed_half or x == reversed_half // 10


if __name__ == "__main__":
    print(isPalindrome(121))   # True
    print(isPalindrome(-121))  # False
    print(isPalindrome(10))    # False
