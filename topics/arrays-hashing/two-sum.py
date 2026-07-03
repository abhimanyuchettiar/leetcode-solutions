"""
1. Two Sum
https://leetcode.com/problems/two-sum/

Pattern: Arrays & Hashing
Time: O(n) | Space: O(n)

Approach:
Single pass with a hash map storing value -> index seen so far.
For each number, check if its complement (target - num) already
exists in the map before inserting the current number.
"""

def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))  # [0, 1]
    print(twoSum([3, 2, 4], 6))       # [1, 2]
