"""
387. First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string/

Pattern: Arrays & Hashing
Time: O(n) | Space: O(1)  (at most 26 lowercase letters)

Approach:
Count the frequency of every character in one pass, then scan the
string again in order and return the index of the first character
whose count is exactly 1.
"""

from collections import Counter

def firstUniqChar(s: str) -> int:
    counts = Counter(s)

    for i, char in enumerate(s):
        if counts[char] == 1:
            return i

    return -1


if __name__ == "__main__":
    print(firstUniqChar("leetcode"))     # 0
    print(firstUniqChar("loveleetcode")) # 2
    print(firstUniqChar("aabb"))         # -1
