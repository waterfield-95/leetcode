/*
date: 201001
idea: deep copy: copy the structure and value.
S1. DFS: recursion
- create a hash-map<original node: cloned node> to store visited node
- recursive boundary condition: if node has already been in visited map, return cloned node.
- initialization: create new node. and recursion: each call returns the cloned copy of corresponding neighbor.

S2. BFS: 
- queue to store original node and traveres all neighbors to add them to queue
- visited hash-map <original node: new node>
- for each neighbor, we need to determine if it is visited. If not, we should add to queue and visited hash map. And then complete the cloned neighbors.
*/


// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

class Solution {
public:
    // create a hash-map to store visited node
    unordered_map<Node*, Node*> visited;
    Node* cloneGraph(Node* node) {
        if(node == nullptr){
            return node;
        }

        // avoid repeated operation
        if(visited.find(node) != visited.end()){
            return visited[node];
        }

        // create clone node
        Node* cloneNode = new Node(node->val);
        visited[node] = cloneNode;

        for(auto& neighbor: node->neighbors){
            cloneNode->neighbors.emplace_back(cloneGraph(neighbor));
        }
        return cloneNode;
    }
};


class Solution2 {
public:
    Node* cloneGraph(Node* node) {
        if(!node) return node;

        unordered_map<Node*, Node*> visited;
        queue<Node*> q;
        q.push(node);
        visited[node] = new Node(node->val);  

        while(!q.empty()){
            auto n = q.front();
            q.pop();

            for(auto& neighbor: n->neighbors){
                // when the neighbor didn't visit, add to queue and visited map.
                if(visited.find(neighbor) == visited.end()){
                    q.push(neighbor);
                    visited[neighbor] = new Node(neighbor->val);
                }
                visited[n]->neighbors.emplace_back(visited[neighbor]);
            }
        }
        return visited[node];
    }
};
