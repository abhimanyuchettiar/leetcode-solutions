"""
15. 3Sum
https://leetcode.com/problems/3sum/

Pattern: Two Pointers (sort + fix one, two-pointer the rest)
Time: O(n^2) | Space: O(1) excluding output

Approach:
Sort the array. Fix the smallest element of each triplet, then use
two pointers on the remaining subarray to find pairs that sum to
its negation. Skip duplicate values at every position to avoid
duplicate triplets in the output.
"""

def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    res = []

    for i in range(n - 2):
        if nums[i] > 0:
            break  # smallest element positive -> no triplet can sum to 0
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # skip duplicate anchors

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return res


if __name__ == "__main__":
    print(threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
    print(threeSum([0, 1, 1]))               # []
    print(threeSum([0, 0, 0]))               # [[0, 0, 0]]
