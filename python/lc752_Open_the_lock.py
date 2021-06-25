"""
2021.6.25
idea: BFS, find the shortest path
- 1. We need find every posibility in every step (modify only one slot)
- 2. create queue to store posibilty status, variable current steps, deadend hash set, visited set
- 3. BFS through queue, pop one element, find next 8 status and add unseen status to queue, repeatly
"""

from typing import List, Generator
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set = set(deadends)
        visited = {'0000'}
        candidate = deque(['0000'])
        step = 0
        while candidate:
            n = len(candidate)
            for i in range(n):
                cur = candidate.popleft()
                if cur in deadends_set:
                    continue
                if cur == target:
                    return step

                l = list(cur)
                # 按字符修改
                for j in range(4):
                    num = l[j]
                    l[j] = '0' if num == '9' else str(int(num)+1)
                    s = ''.join(l)
                    if s not in visited:
                        candidate.append(s)
                        visited.add(s)

                    l[j] = '9' if num == '0' else str(int(num)-1)
                    s = ''.join(l)
                    if s not in visited:
                        candidate.append(s)
                        visited.add(s)
                    
                    l[j] = num
            step += 1
        return -1

    def openLock_official(deadends, target):
        if target == '0000':
            return 0
        
        dead = set(deadends)
        if '0000' in dead:
            return -1
        
        def num_prev(x):
            return '9' if x == '0' else str(int(x) - 1)
        
        def num_succ(x):
            return '0' if x == '9' else str(int(x) + 1)
        
        # enumeration
        def get(status: str) -> Generator[str, None, None]:
            s = list(status)
            for i in range(4):
                num = s[i]
                s[i] = num_prev(num)
                yield ''.join(s)
                s[i] = num_succ(num)
                yield ''.join(s)
                s[i] = num

        q = deque([('0000', 0)])
        seen = {'0000'}
        while q:
            status, step = q.popleft()
            for next_status in get(status):
                if next_status not in seen and next_status not in dead:
                    if next_status == target:
                        return step + 1
                    q.append((next_status, step+1))
                    seen.add(next_status)
        return -1

                


if __name__ == '__main__':
    deadends = ["0201","0101","0102","1212","2002"]
    target = '0202'
    S = Solution()
    print(S.openLock(deadends, target))
