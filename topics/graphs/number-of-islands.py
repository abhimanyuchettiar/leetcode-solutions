"""
200. Number of Islands
https://leetcode.com/problems/number-of-islands/

Pattern: Graphs (DFS flood-fill on an implicit grid graph)
Time: O(rows * cols) | Space: O(rows * cols) worst-case recursion depth

Approach:
Treat the grid as a graph where each land cell ('1') connects to
its 4-directional neighbors. Scan every cell; on an unvisited land
cell, increment the island count and flood-fill (DFS) to sink the
entire connected component so it isn't counted again.
"""

def numIslands(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "0"  # mark visited
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands += 1
                dfs(r, c)

    return islands


if __name__ == "__main__":
    grid = [
        list("11110"),
        list("11010"),
        list("11000"),
        list("00000"),
    ]
    print(numIslands(grid))  # 1
