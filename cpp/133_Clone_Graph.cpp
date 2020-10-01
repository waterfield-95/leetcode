/*
date: 201001
idea: DFS

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
*/

class Solution {
public:
    unordered_map<Node*, Node*> visited;
    Node* cloneGraph(Node* node) {
        if(node == nullptr){
            return node;
        }

        // 如果node存在与visited中，直接返回对应的克隆节点
        if(visited.find(node) != visited.end()){
            return visited[node];
        }

        // 新建克隆节点
        Node* cloneNode = new Node(node->val);
        visited[node] = cloneNode;

        for(auto& neighbor: node->neighbors){
            cloneNode->neighbors.emplace_back(cloneGraph(neighbor));
        }
        return cloneNode;
    }
};
