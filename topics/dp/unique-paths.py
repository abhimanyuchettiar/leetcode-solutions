"""
62. Unique Paths
https://leetcode.com/problems/unique-paths/

Pattern: Dynamic Programming (Memoization / Top-Down)
Time: O(m * n) | Space: O(m * n)  (memo dict + recursion stack)

Approach:
From cell (r, c), the number of paths to the bottom-right corner is
the sum of paths from moving right and paths from moving down.
Overlapping subproblems (many routes pass through the same cell)
make this a natural memoization candidate — cache paths(r, c) the
first time it's computed.
"""

def uniquePaths(m: int, n: int, memo: dict = None) -> int:
    if memo is None:
        memo = {}

    def paths(r: int, c: int) -> int:
        if r == m - 1 or c == n - 1:
            return 1
        if (r, c) in memo:
            return memo[(r, c)]

        memo[(r, c)] = paths(r + 1, c) + paths(r, c + 1)
        return memo[(r, c)]

    return paths(0, 0)


if __name__ == "__main__":
    print(uniquePaths(3, 7))  # 28
    print(uniquePaths(3, 2))  # 3
