# LeetCode Solutions

Structured problem-solving practice for SDE / quant interview prep — organized by **pattern**, not by problem number, because patterns are what actually transfer to new problems.

Every solution includes the approach, time/space complexity, and a short note on why that pattern applies. See [`patterns.md`](patterns.md) for a cheat-sheet of the core patterns used across this repo.

## Progress

| Topic | Solved | Total |
|---|---|---|
| Arrays & Hashing | 0 | — |
| Two Pointers | 0 | — |
| Sliding Window | 0 | — |
| Binary Search | 0 | — |
| Linked Lists | 0 | — |
| Trees | 0 | — |
| Graphs | 0 | — |
| Dynamic Programming | 0 | — |
| Greedy | 0 | — |
| Heap / Priority Queue | 0 | — |
| Backtracking | 0 | — |

*(Table updated manually — see [`progress.md`](progress.md) for the full running log.)*

## Structure

```
topics/
├── arrays-hashing/
├── two-pointers/
├── sliding-window/
├── binary-search/
├── linked-lists/
├── trees/
├── graphs/
├── dp/
├── greedy/
├── heap-priority-queue/
└── backtracking/
```

Each file is self-contained: problem statement link, pattern tag, complexity, approach comment, solution, and a quick inline test under `if __name__ == "__main__":`.

## Solution format

```python
"""
<number>. <Problem Name>
https://leetcode.com/problems/<slug>/

Pattern: <pattern name>
Time: O(...) | Space: O(...)

Approach:
<2-4 lines explaining the core idea>
"""

def solution(...):
    ...

if __name__ == "__main__":
    # quick sanity check
    ...
```

## About this repo

Built as part of ongoing DSA preparation alongside GATE CS/IT 2027 and systems-level project work ([order-book-engine](https://github.com/abhimanyuchettiar/order-book-engine), Argus). Language: Python.
