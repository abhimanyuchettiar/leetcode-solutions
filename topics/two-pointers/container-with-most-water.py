"""
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/

Pattern: Two Pointers
Time: O(n) | Space: O(1)

Approach:
Start with the widest container (pointers at both ends). Area is
limited by the shorter wall, so moving the taller pointer inward
can only decrease width without any chance of increasing height —
always move the shorter wall inward instead, tracking the max area seen.
"""

def maxArea(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    best = 0

    while left < right:
        width = right - left
        best = max(best, width * min(height[left], height[right]))

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return best


if __name__ == "__main__":
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(maxArea([1, 1]))                        # 1
