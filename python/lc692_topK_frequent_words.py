"""
2021.5
idea:
1. hashtable + sort
2. priority queue
    - TopK problem solution, O(logN)insert and delete; O(1)find top element
"""

from typing import List
from collections import Counter
from functools import cmp_to_key
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        def compare(a, b):
            if a[1] > b[1]:
                return -1
            elif a[1] < b[1]:
                return 1
            elif a[0] > b[0]:
                return 1
            elif a[0] < b[0]:
                return -1
            else:
                return 0
            
        counter = Counter(words)
        l = list(counter.items())
        l.sort(key=cmp_to_key(compare))
        return [i[0] for i in l[:k]]

    def topKFrequent_simple(self, words, k):
        counter = Counter(words)
        res = sorted(counter.keys(), key=lambda key: (-counter[key], key))[:k]
        return res

    def topKFrequent_heapq(self, words, k):
        counter = Counter(words)
        heap, ans = [], []
        for word in counter:
            heapq.heappush(heap, (-counter[word], word))
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans


if __name__ == '__main__':
    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is", 'hh', 'hh', 'zz', 'zz']
    k = 4
    S = Solution()
    print(S.topKFrequent(words, k))
    print(S.topKFrequent_simple(words, k))
    print(S.topKFrequent_heapq(words, k))