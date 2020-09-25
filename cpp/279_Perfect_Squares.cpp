/**
Date: 200925
Basic Idea: BFS, tree
1. Regarding given value n as root, minus all squares which is less than n;
2. After substration, if new value less than 0, back to queue; if new value equal to 0, return steps; if new value exists in visited set, continue to next new value.
And then the rest of new values push into queue and visited set. Loop
3. If n is prime, return n;
*/

class Solution {
    vector<int> squareList(int n){
        vector<int> sl;
        for(int i=0; pow(i,2)<=n; i++){
            sl.push_back(pow(i,2));
        }
        return sl;
    }
public:
    int numSquares(int n) {
        vector<int> squarelist = squareList(n);
        unordered_set<int> visited;
        queue<int> q;

        q.push(n);
        visited.insert(n);

        int steps = 1;

        while(!q.empty()){
            int size = q.size();

            for(int i=0; i<size; i++){
                int temp = q.front();
                q.pop();

                for(int square: squarelist){
                    int next = temp - square;
                    if(next < 0) break;
                    if(next == 0) return steps;
                    if(visited.count(next)) continue;
                    
                    q.push(next);
                    visited.insert(next);
                }
            }
            steps++;       
        }
        return n;
    }
};
