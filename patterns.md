# Patterns Cheat Sheet

Short reference for the core patterns used across this repo. The goal isn't to memorize problems — it's to recognize which pattern a new problem maps to.

## Arrays & Hashing
Use a hash map/set to trade space for O(1) lookups, turning O(n²) brute-force comparisons into O(n) single passes. Watch for: complements (Two Sum), frequency counts, prefix/suffix products.

## Two Pointers
Two indices moving toward each other (or one fast/one slow) over a sorted or structured sequence, avoiding nested loops. Watch for: sorted array pair sums, palindrome checks, removing duplicates in place.

## Sliding Window
A window of indices that expands/contracts over a sequence to track a running condition (sum, count, distinct chars) without recomputation. Watch for: "longest/shortest substring/subarray with condition X."

## Binary Search (incl. "search on answer")
Not just for sorted arrays — applies whenever a search space is monotonic (if X works, everything above/below X also works). Binary search the *answer value* itself, not just an index. Watch for: "minimize the maximum" / "maximize the minimum" phrasing.

## Linked Lists
Dummy head nodes simplify edge cases (empty list, removing head). Fast/slow pointers detect cycles or find midpoints. Watch for: merging, reversing, cycle detection.

## Trees
DFS (recursive or explicit stack) for path/depth problems; BFS (queue) for level-order problems. Watch for: "level," "depth," "path sum" (BFS/DFS cues respectively).

## Graphs
DFS/BFS flood-fill for connected components (grids = implicit graphs). Union-Find for dynamic connectivity. Watch for: "islands," "regions," "connected components."

## Dynamic Programming
Identify overlapping subproblems + optimal substructure. Start with brute-force recursion, add memoization, then convert to bottom-up/tabulation if needed. Watch for: "count the ways," "min/max cost to reach."

## Greedy
Locally optimal choice at each step leads to a globally optimal solution — but only when the problem has the greedy-choice property (prove it or find a counterexample before trusting it). Watch for: interval scheduling, "minimum number of X."

## Heap / Priority Queue
Maintain a running top-k or a dynamically sorted structure without re-sorting each time. Watch for: "kth largest," "merge k sorted," "top k frequent."

## Backtracking
Explore a decision tree, prune branches that violate constraints, backtrack on dead ends. Watch for: "all possible," "all combinations/permutations/subsets."
