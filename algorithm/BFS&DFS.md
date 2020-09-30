## BFS(breath first search) 广度优先遍历
BFS always use `queue` to achieve.

Goal: 
- traverse all elements
- find the shortest path

```cpp
/*
BFS Template:
Return the length of the shortest path between root and target node.
*/

int BFS(Node* root, Node* target) {

    // store all nodes which are waiting to be processed
    Queue<Node> queue;
    
    // number of steps neeeded from root to current node
    int step = 0;   
    
    // initialize
    add root to queue;
    
    // BFS
    while (queue is not empty) {
        step++;
        // iterate the nodes which are already in the queue
        int size = queue.size();
        for (int i = 0; i < size; ++i) {
            Node* cur = the first node in queue;
            return step if cur is target;
            for (Node* next : the neighbors of cur) {
                add next to queue;
            }
            remove the first node from queue;
        }
    }
    return -1;          // there is no path from root to target
}
```

## DFS(depth first search) 深度优先遍历
It always use `queue` to achieve the function of traversal or search in tree and graph problem.

## Example
### [200. Number of Islands](https://leetcode-cn.com/problems/number-of-islands/) 

[Both BFS and DFS Solution code and basic idea](https://github.com/Fieldwater/leetcode/blob/master/cpp/200_Number_of_Islands.cpp)

What's the biggest difference between them is the order of traveral. BFS traverse all elements in order, while DFS track elements to the deepest one and then back-track others. So DFS is usually implemented by recursion quickly, while BFS is relatively slow due to traversal all possibility through queue.

