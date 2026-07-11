"""
75. Sort Colors
https://leetcode.com/problems/sort-colors/

Pattern: Two Pointers (Dutch National Flag)
Time: O(n) | Space: O(1)

Approach:
Three pointers partition the array in a single pass: `low` marks
the boundary after which all 0s are placed, `high` marks the
boundary before which all 2s are placed, and `mid` scans through.
- nums[mid] == 0 -> swap with low, advance both low and mid
- nums[mid] == 1 -> already in place, just advance mid
- nums[mid] == 2 -> swap with high, shrink high (don't advance mid,
  since the swapped-in value from high hasn't been checked yet)
"""

def sortColors(nums: list[int]) -> None:
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


if __name__ == "__main__":
    a = [2, 0, 2, 1, 1, 0]
    sortColors(a)
    print(a)  # [0, 0, 1, 1, 2, 2]

    b = [2, 0, 1]
    sortColors(b)
    print(b)  # [0, 1, 2]
