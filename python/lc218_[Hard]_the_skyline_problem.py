"""
2021.7
idea: Given the location and height of building list, return the skyline list (left point of horizontal line)
    - skyline: key point list, left endpoint cordinate and termination which is the rightmost endpoint(y=0)

"""

from typing import List
from sortedcontainers import SortedList


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ans = []
        ps = []
        # left height: negative
        for l, r, h in buildings:
            ps.append((l, -h))
            ps.append((r, h))
        # sort priority: x -> height (negative first)
        ps.sort()

        prev = 0
        q = SortedList([prev])
        for point, height in ps:
            if height < 0:
                # left startpoint
                q.add(-height)
            else:
                # right endpoint
                q.remove(height)
            
            # get the current highest height
            cur = q[-1]
            if cur != prev:
                ans.append([point, cur])
                prev = cur

        return ans



if __name__ == '__main__':
    buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    S = Solution()
    print(S.getSkyline(buildings))