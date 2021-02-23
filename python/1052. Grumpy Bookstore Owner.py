"""
2021.2
idea: slide window
- Reduce redundant traverse: slide window, every step -> add new elements and reduce old elements according to regulation
"""

# self: 15min
class Solution:
    def maxSatisfied(self, customers, grumpy, X):
        current_satisfied_people = sum(customers[:X])
        for i in range(X, len(grumpy)):
            if grumpy[i] == 0:
                current_satisfied_people += customers[i]
        max_satisfied_people = current_satisfied_people
        for i in range(X, len(customers)):
            if grumpy[i-X] == 1:
                current_satisfied_people -= customers[i-X]
            if grumpy[i] == 1:
                current_satisfied_people += customers[i]
            if current_satisfied_people > max_satisfied_people:
                max_satisfied_people = current_satisfied_people
        return max_satisfied_people
        
# answer: slower than mine
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        total = sum(c for c,g in zip(customers, grumpy) if g == 0)
        max_increase = increase = sum(c*g for c,g in zip(customers[:X], grumpy[:X]))
        for i in range(X, n):
            increase += customers[i] * grumpy[i] - customers[i-X]*grumpy[i-X]
            max_increase = max(max_increase, increase)
        return total + max_increase
        
