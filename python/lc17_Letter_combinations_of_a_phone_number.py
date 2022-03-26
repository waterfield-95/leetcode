from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        combination = []
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        def backtrack(index, path):
            # base case
            if len(path) == len(digits):
                combination.append("".join(path))
                return
            
            letters = mapping[digits[index]]
            for letter in letters:
                path.append(letter)
                backtrack(index+1, path)
                path.pop(-1)
            
        backtrack(0, [])
        return combination
    
    # Time: O(N*4^N)
    # Space: O(N)