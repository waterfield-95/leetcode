from typing import List

class Solution:
    """
    Time complexity: O(max(n, len(trust)))
    Space complexity: O(2n)

    Intuition: Graph -> indegree and outdegree
    """
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # index-0 is always 0 which won't use
        indegree = [0] * (n+1)
        outdegree = [0] * (n+1)
        for (out_, in_) in trust:
            indegree[in_] += 1
            outdegree[out_] += 1
            
        judge = -1
        for i in range(1, n+1):
            if outdegree[i] == 0 and indegree[i] == n-1:
                judge = i
                break
        
        return judge
    