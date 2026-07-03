"""
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/

Pattern: Two Pointers (read/write)
Time: O(n) | Space: O(1)

Approach:
Slow pointer marks the next position for a nonzero element, fast
pointer scans the array. Swap whenever a nonzero is found, which
naturally pushes all zeroes to the end while preserving order.
"""

def moveZeroes(nums: list[int]) -> None:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


if __name__ == "__main__":
    a = [0, 1, 0, 3, 12]
    moveZeroes(a)
    print(a)  # [1, 3, 12, 0, 0]
