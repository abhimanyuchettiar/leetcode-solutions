"""
7. Reverse Integer
https://leetcode.com/problems/reverse-integer/

Pattern: Math (digit extraction with overflow check)
Time: O(log n) | Space: O(1)

Approach:
Repeatedly pop the last digit off with % 10 and // 10, building the
reversed number digit by digit. Must guard against 32-bit signed
overflow (LeetCode's constraint) before returning.
"""

def reverse(x: int) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1

    sign = -1 if x < 0 else 1
    x = abs(x)
    result = 0

    while x:
        digit = x % 10
        x //= 10
        result = result * 10 + digit

    result *= sign
    return result if INT_MIN <= result <= INT_MAX else 0


if __name__ == "__main__":
    print(reverse(123))    # 321
    print(reverse(-123))   # -321
    print(reverse(120))    # 21
    print(reverse(1534236469))  # 0 (overflow)
