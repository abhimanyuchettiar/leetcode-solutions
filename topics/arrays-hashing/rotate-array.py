"""
189. Rotate Array
https://leetcode.com/problems/rotate-array/

Pattern: Arrays & Hashing (in-place reversal trick)
Time: O(n) | Space: O(1)

Approach:
Rotating right by k is equivalent to reversing the whole array,
then reversing the first k elements, then reversing the remaining
n-k elements. This achieves the rotation in-place without extra
storage. Normalize k with k % n first in case k > n.
"""

def rotate(nums: list[int], k: int) -> None:
    n = len(nums)
    k %= n

    def reverse(lo: int, hi: int) -> None:
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7]
    rotate(a, 3)
    print(a)  # [5, 6, 7, 1, 2, 3, 4]

    b = [-1, -100, 3, 99]
    rotate(b, 2)
    print(b)  # [3, 99, -1, -100]
