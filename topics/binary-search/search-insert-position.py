"""
35. Search Insert Position
https://leetcode.com/problems/search-insert-position/

Pattern: Binary Search (lower bound)
Time: O(log n) | Space: O(1)

Approach:
Standard binary search, but instead of returning -1 on a miss,
`lo` naturally lands on the correct insertion index once the loop
ends — it's the first position where target could be inserted
while keeping the array sorted.
"""

def searchInsert(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return lo


if __name__ == "__main__":
    print(searchInsert([1, 3, 5, 6], 5))  # 2
    print(searchInsert([1, 3, 5, 6], 2))  # 1
    print(searchInsert([1, 3, 5, 6], 7))  # 4
