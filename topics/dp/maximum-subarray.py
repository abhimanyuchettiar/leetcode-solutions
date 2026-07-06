"""
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

Pattern: Dynamic Programming (Kadane's Algorithm)
Time: O(n) | Space: O(1)

Approach:
At each index, decide whether to extend the previous subarray or
start fresh from the current element — whichever gives a larger
sum. Track the best sum seen across the whole pass. This is the
canonical Kadane's algorithm.
"""

def maxSubArray(nums: list[int]) -> int:
    best = curr = nums[0]

    for num in nums[1:]:
        curr = max(num, curr + num)
        best = max(best, curr)

    return best


if __name__ == "__main__":
    print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(maxSubArray([1]))                                # 1
    print(maxSubArray([5, 4, -1, 7, 8]))                   # 23
