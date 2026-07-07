"""
198. House Robber
https://leetcode.com/problems/house-robber/

Pattern: Dynamic Programming
Time: O(n) | Space: O(1)

Approach:
At each house, the best you can do is either skip it (take the
best result up to the previous house) or rob it (its value + the
best result up to two houses back, since adjacent houses can't
both be robbed). Instead of a separate dp array, track just the
last two states (prev2, prev1) and roll them forward.

Note: first pass used an auxiliary dp array (O(n) space) — beat
100% on runtime but only ~6% on memory (i.e. only 6% of submissions
used less memory). Collapsing the array to two rolling variables
keeps the same O(n) time but drops space from O(n) to O(1),
improving the memory percentile to ~60% while runtime stays at 100%.
"""

def rob(nums: list[int]) -> int:
    prev2, prev1 = 0, 0  # best up to i-2, best up to i-1

    for num in nums:
        curr = max(prev1, prev2 + num)
        prev2 = prev1
        prev1 = curr

    return prev1


if __name__ == "__main__":
    print(rob([1, 2, 3, 1]))         # 4
    print(rob([2, 7, 9, 3, 1]))      # 12
    print(rob([]))                    # 0
