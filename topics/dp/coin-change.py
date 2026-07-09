"""
322. Coin Change
https://leetcode.com/problems/coin-change/

Pattern: Dynamic Programming (Memoization / Top-Down)
Time: O(amount * len(coins)) | Space: O(amount)

Approach:
minCoins(remaining) = 1 + min(minCoins(remaining - coin) for each
usable coin). Memoize on the remaining amount since the same
remaining value can be reached through many different coin
combinations. Base cases: 0 remaining needs 0 coins; a negative
remaining is invalid (return infinity so it's never chosen as min).
"""

def coinChange(coins: list[int], amount: int, memo: dict = None) -> int:
    if memo is None:
        memo = {}

    def minCoins(remaining: int) -> float:
        if remaining == 0:
            return 0
        if remaining < 0:
            return float("inf")
        if remaining in memo:
            return memo[remaining]

        best = min(
            (1 + minCoins(remaining - coin) for coin in coins),
            default=float("inf"),
        )
        memo[remaining] = best
        return best

    result = minCoins(amount)
    return result if result != float("inf") else -1


if __name__ == "__main__":
    print(coinChange([1, 2, 5], 11))  # 3
    print(coinChange([2], 3))          # -1
    print(coinChange([1], 0))          # 0
