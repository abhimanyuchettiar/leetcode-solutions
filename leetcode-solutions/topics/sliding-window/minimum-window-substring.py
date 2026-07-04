"""
76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/

Pattern: Sliding Window
Time: O(n + m) | Space: O(m)  (m = size of char set in t)

Approach:
Expand the right edge of the window until it contains all
characters of t (tracked via a frequency counter + a "satisfied
count" of distinct chars matched). Then contract from the left as
far as possible while still valid, recording the shortest valid
window seen.
"""

from collections import Counter

def minWindow(s: str, t: str) -> str:
    if not s or not t:
        return ""

    need = Counter(t)
    missing = len(t)  # total chars still needed (with multiplicity)

    left = 0
    best_left, best_len = 0, float("inf")

    for right, char in enumerate(s):
        if need[char] > 0:
            missing -= 1
        need[char] -= 1

        while missing == 0:
            if right - left + 1 < best_len:
                best_left, best_len = left, right - left + 1

            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1

    return "" if best_len == float("inf") else s[best_left:best_left + best_len]


if __name__ == "__main__":
    print(minWindow("ADOBECODEBANC", "ABC"))  # "BANC"
    print(minWindow("a", "a"))                 # "a"
