/**
Date: 200925
Basic Idea: BFS
1. Regarding given value n as root, minus all squares which is less than n;
2. After substration, if new value less than 0, back to queue; if new value equal to 0, return steps; if new value exists in visited set, continue to next new value.
And then the rest of new values push into queue and visited set. Loop
*/

class Solution {
    // 获取所有小于n的平方数
    vector<int> getSquare(int n){
        vector<int> res;
        for(int i=1; i*i<=n; i++){
            res.push_back(i*i);
        }
        return res;
    }
public:
    int numSquares(int n) {
        vector<int> squares = getSquare(n);
        unordered_set<int> visited;
        queue<int> q;
        
        q.push(n);
        int steps = 1;
        visited.insert(n);

        while(!q.empty()){
            int size = q.size();
            for(int i=0; i<size; i++){
                int cur = q.front();
                q.pop();
                
                for(int num: squares){
                    int next = cur - num;
                    if(next < 0) break;
                    if(next == 0) return steps;
                    if(visited.count(next)) continue;

                    visited.insert(next);
                    q.push(next);
                }
            }
            steps++;
        }
        return n;
    }
};
