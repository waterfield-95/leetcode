from typing import List

class backtrack:
    """
    Time: O(2^{2N})
    Space: O(2^{2N})
    """
    def generateParenthesis(self, n: int) -> List[str]:
        combination = []
        def backtrack(n_open, n_close, path):
            if len(path) == 2*n:
                combination.append("".join(path))
                return 
            
            if n_open < n:
                path.append("(")
                backtrack(n_open+1, n_close, path)
                path.pop()
            if n_close < n_open:
                path.append(")")
                backtrack(n_open, n_close+1, path)
                path.pop()
            
        backtrack(0, 0, [])
        return combination

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(A=[]):
            if len(A) == 2*n:
                if valid(A):
                    combination.append("".join(A))
            else:
                A.append("(")
                generate(A)
                A.pop()
                
                A.append(")")
                generate(A)
                A.pop()
            
        def valid(A):
            cnt = 0
            for c in A:
                if c == "(": 
                    cnt += 1
                else:
                    cnt -= 1
                
                if cnt < 0:
                    return False
            if cnt == 0:
                return True
            else:
                return False
        
        combination = []
        generate()
        return combination
    
#Time: O(2^{2N} * N) -> N is number of pair of parenthesis
# Space: O(N)
