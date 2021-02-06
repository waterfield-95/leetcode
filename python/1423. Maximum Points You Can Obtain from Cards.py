"""
idea: slide window
1. Reverse Thinking: calculate the minimum of slide window, and the rest of elements is the answer
"""

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        window_size = n - k
        min_sum = window_sum = sum(cardPoints[:window_size])
        for i in range(window_size, n):
            window_sum += cardPoints[i] - cardPoints[i-window_size]
            min_sum = min(min_sum, window_sum)
        return sum(cardPoints) - min_sum
