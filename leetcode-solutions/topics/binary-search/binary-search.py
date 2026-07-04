"""
704. Binary Search
https://leetcode.com/problems/binary-search/

Pattern: Binary Search
Time: O(log n) | Space: O(1)

Approach:
Classic binary search on a sorted array. Narrow the [lo, hi] range
by comparing the middle element to the target each step, halving
the search space until found or the range is empty.
"""

def search(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


if __name__ == "__main__":
    print(search([-1, 0, 3, 5, 9, 12], 9))  # 4
    print(search([-1, 0, 3, 5, 9, 12], 2))  # -1
