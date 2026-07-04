"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Pattern: Sliding Window
Time: O(n) | Space: O(min(n, charset size))

Approach:
Expand the right edge of the window each step, tracking the last
seen index of each character. If a repeat is found inside the
current window, jump the left edge past its previous occurrence
(never move it backward). Track the max window length throughout.
"""

def lengthOfLongestSubstring(s: str) -> int:
    last_seen = {}
    left = 0
    best = 0

    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1
        last_seen[char] = right
        best = max(best, right - left + 1)

    return best


if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))  # 3
    print(lengthOfLongestSubstring("bbbbb"))       # 1
    print(lengthOfLongestSubstring("pwwkew"))      # 3
