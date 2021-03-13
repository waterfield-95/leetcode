"""
idea: 
1. Dijkstra
- find the lowest cost node
- deal with neighbors of each node to find lowest cost
"""

class SolutionSelf1:
    def find_lowest_cost_node(self, node_costs, processed):
        candidate_node = None
        candidate_node_cost = float('inf')
        for node in node_costs.keys():
            if node not in processed and node_costs[node] < candidate_node_cost:
                candidate_node = node
                candidate_node_cost = node_costs[node]
        return candidate_node
        
    def networkDelayTime(self, times, n, k):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        costs = {node: float('inf') for node in range(1, n+1)}
        costs[k] = 0
        processed = set()
        lowest_node = self.find_lowest_cost_node(costs, processed)
        while lowest_node:
            for neighbor, weight in graph[lowest_node]:
                costs[neighbor] = min(costs[neighbor], costs[lowest_node]+weight)
                # new_cost = weight + costs[node]
                # if new_cost < costs[neighbor]:
                #     costs[neighbor] = new_cost
            processed.add(lowest_node)
            lowest_node = self.find_lowest_cost_node(costs, processed)
        ans = max(costs.values())
        return ans if ans < float('inf') else -1

class Solution:
    def networkDelayTime(self, times, n, k):
        # 定义图
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # 定义边的开销 -> 时间
        costs = {node: float('inf') for node in range(1, n+1)}
        # 定义处理过的节点，只使用index为1-n的值，表示节点，index=0不使用
        seen = [False] * (n+1)
        # 初始化, 第一个节点的开销是0
        costs[k] = 0

        # 处理每个节点，直到没有下一个节点
        while True:
            candidate_node = -1
            candidate_cost = float('inf')
            # 遍历所有节点，找到没有处理过的，并且当前开销最小的node（开销表示从起点到该节点）
            for i in range(1, n+1):
                if not seen[i] and costs[i] < candidate_cost:
                    candidate_node = i
                    candidate_cost = costs[i]
            
            # 如果没有可用节点，break
            if candidate_node < 0: break
            # 如果有效节点记录True，表示已经处理过
            seen[candidate_node] = True
            # 遍历该节点的所有直连的节点，找到邻居节点的最小值（从起始点到该点开销）
            for neighbor, cost in graph[candidate_node]:
                costs[neighbor] = min(costs[neighbor], costs[candidate_node]+cost)
            
        # costs记录从起始点到每个节点的最短开销，如果最大开销不是inf，则说明遍历所有节点，并且是遍历所有点的时间
        ans = max(costs.values())
        return ans if ans < float('inf') else -1
 
