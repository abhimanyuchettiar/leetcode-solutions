"""
695. Max Area of Island
https://leetcode.com/problems/max-area-of-island/

Pattern: Graphs (DFS flood-fill on an implicit grid graph)
Time: O(rows * cols) | Space: O(rows * cols) worst-case recursion depth

Approach:
Same flood-fill idea as Number of Islands, but instead of just
counting components, DFS returns the size of the connected
component it explores (1 + sum of its 4-directional neighbors).
Track the max area seen across every unvisited land cell.
"""

def maxAreaOfIsland(grid: list[list[int]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])

    def dfs(r: int, c: int) -> int:
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
            return 0
        grid[r][c] = 0  # mark visited
        return (
            1
            + dfs(r + 1, c)
            + dfs(r - 1, c)
            + dfs(r, c + 1)
            + dfs(r, c - 1)
        )

    best = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                best = max(best, dfs(r, c))

    return best


if __name__ == "__main__":
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    print(maxAreaOfIsland(grid))  # 6

    print(maxAreaOfIsland([[0, 0, 0, 0, 0]]))  # 0
