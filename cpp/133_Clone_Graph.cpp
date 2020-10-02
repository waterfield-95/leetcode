/*
date: 201001
idea: deep copy: copy the structure and value.
S1. DFS: recursion
- create a hash-map<original node: cloned node> to store visited node
- recursive boundary condition: if node has already been in visited map, return cloned node.
- initialization: create new node. and recursion: each call returns the cloned copy of corresponding neighbor.
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
