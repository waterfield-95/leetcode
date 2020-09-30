## BFS(breath first search) 广度优先遍历
BFS always use `queue` to achieve.

Goal: 
- traverse all elements
- find the shortest path

## DFS(depth first search) 深度优先遍历
It always use `stack` to achieve the function of traversal or search in tree and graph problem.

## Example
[200. Number of Islands](https://leetcode-cn.com/problems/number-of-islands/) 

[Both BFS and DFS Solution code and basic idea](https://github.com/Fieldwater/leetcode/blob/master/cpp/200_Number_of_Islands.cpp)

What's the biggest difference between them is the order of traveral. BFS traverse all elements in order, while DFS track elements to the deepest one and then back-track others. So DFS is usually implemented by recursion quickly, while BFS is relatively slow due to traversal all possibility through queue.

