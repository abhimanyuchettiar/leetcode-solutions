"""
509. Fibonacci Number
https://leetcode.com/problems/fibonacci-number/

Pattern: Dynamic Programming (Memoization / Top-Down)
Time: O(n) | Space: O(n)  (recursion stack + memo dict)

Approach:
Naive recursion recomputes fib(k) exponentially many times because
subproblems overlap (fib(5) needs fib(4) and fib(3), fib(4) needs
fib(3) again, etc). Memoizing each computed fib(k) turns it into
O(n) work — each subproblem solved exactly once.
"""

def fib(n: int, memo: dict = None) -> int:
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n in memo:
        return memo[n]

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    print(fib(2))   # 1
    print(fib(3))   # 2
    print(fib(4))   # 3
    print(fib(10))  # 55
