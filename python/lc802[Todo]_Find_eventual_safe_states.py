"""
2021.8
Given a graph, find safe starting node which could terminate in less than k step (no circle)
"""


from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        pass

if __name__ == '__main__':
    """
    graph[i] is a list of labels j such that (i,j) is a directed edge of the graph
    going from node i to node j
    """
    graph = [[1,2],[2,3],[5],[0],[5],[],[]]