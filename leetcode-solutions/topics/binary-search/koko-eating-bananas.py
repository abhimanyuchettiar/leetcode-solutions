"""
875. Koko Eating Bananas
https://leetcode.com/problems/koko-eating-bananas/

Pattern: Binary Search on Answer
Time: O(n log m) | Space: O(1)  (m = max pile size)

Approach:
The answer space (possible eating speeds, 1..max(piles)) is
monotonic: if speed k finishes within h hours, every speed > k
also finishes in time. Binary search on k itself rather than on
the array, checking feasibility with a linear scan each time.
"""

import math

def minEatingSpeed(piles: list[int], h: int) -> int:
    def hours_needed(speed: int) -> int:
        return sum(math.ceil(pile / speed) for pile in piles)

    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if hours_needed(mid) <= h:
            hi = mid          # mid works, try slower
        else:
            lo = mid + 1      # too slow, need faster
    return lo


if __name__ == "__main__":
    print(minEatingSpeed([3, 6, 7, 11], 8))       # 4
    print(minEatingSpeed([30, 11, 23, 4, 20], 5)) # 30
