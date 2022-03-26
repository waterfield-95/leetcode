from typing import List
import collections

class Hash:
    # Optimal: use tuple as hash key
    # Time: O(n*k + n*A)
    # Space: O(n*k + n*A)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #key-> tuple(sorted(list("abc"))): [s]
        hash_table = collections.defaultdict(list)
        
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            
            hash_table[tuple(key)].append(s)
            
        
        res = [l for l in hash_table.values()]
        return res
    
