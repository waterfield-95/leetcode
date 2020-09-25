/*
Date: 20200923
Basic idea: 
1. Using set to store deadends and visited pattern.
2. BFS, transform the shortest path problem. 
3. Add root to the queue, and judge by deadends and target, if not, add child-node to the queue when it doesn't exist in visited set.
4. traverse queue if not empty, increase the number of steps each time.
*/

class Solution {
public:

    // 锁的某一位向上拨一位
    string plusOne(string str, int index){
        if(str[index] == '9') str[index] = '0';
        else str[index] += 1;
        return str;
    }

    // 锁向下拨一位
    string minusOne(string str, int index){
        if(str[index] == '0') str[index] = '9';
        else str[index] -= 1;
        return str;
    }

    int openLock(vector<string>& deadends, string target) {
        // 定义deadEnds保存不能使用的数字
        unordered_set<string> deadEnds;
        for(auto& dead: deadends) deadEnds.insert(dead);

        // 定义step记录当前步数，定义visited记录以达到的数字
        int step = 0;
        unordered_set<string> visited;

        // 定义队列，并保存初始值
        queue<string> res;
        res.push("0000");

        while(!res.empty()){
            int size = res.size();

            for(int i=0; i<size; i++){
                string temp = res.front();
                res.pop();

                // 若为死亡数字，抛弃后续路径
                // 若为target，返回当前step
                if(deadEnds.count(temp)) continue;
                if(temp == target) return step;

                // 每个数字有8钟可能的节点。4个号码分别向上/下拨动
                // 已访问过的节点抛弃，避免陷入死循环
                for(int j=0; j<4; j++){
                    string up = plusOne(temp, j);
                    string down = minusOne(temp, j);

                    if(!visited.count(up)){
                        res.push(up);
                        visited.insert(up);
                    }
                    if(!visited.count(down)){
                        res.push(down);
                        visited.insert(down);
                    }
                }
            }
            step++;
        }
        return -1;
    }
};
