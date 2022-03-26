import collections
from typing import List

class New:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # hashmap: key(complement) -> value(count)
        time_mod = list(map(lambda x: x % 60, time))
        h = dict()
        ans = 0
        for i in range(len(time_mod)):
            key = time_mod[i] if time_mod[i] != 0 else 60
            if key in h:
                ans += h[key]
            complement = 60 - time_mod[i]
            h[complement] = h.get(complement, 0) + 1
        return ans

class Solution3:
    """
    Use directed access array to replace the hash table
        - Indexing from 0 to 59
    """
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = [0] * 60
        n = len(time)
        ans = 0
        for i in range(n):
            remainder = time[i] % 60    # range [0, 59]
            
            if remainder == 0:
                ans += remainders[0]
            else:
                ans += remainders[60 - remainder]
            
            remainders[remainder] += 1
            
        return ans
            

class Solution2:
    # TC: O(n)
    # SC: O(n)
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = collections.defaultdict(int)
        n = len(time)
        ans = 0
        for i in range(n):
            remainder = time[i] % 60    # range [0, 59]
            
            if remainder == 0:
                ans += remainders[0]
            else:
                ans += remainders[60 - remainder]
            
            remainders[remainder] += 1
            
        return ans
            

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # key: 60 - remainder: [current_id]
        hash_table = collections.defaultdict(list)
        cnt = 0
        for i, t in enumerate(time):
            remainder = t % 60
            if remainder in hash_table:
                cnt += len(hash_table[remainder])
            
            hash_table[60 - remainder].append(i)
        
        m = len(hash_table[60])
        if m > 1:
            cnt += int(m*(m-1)/2)
            
        return cnt 
        