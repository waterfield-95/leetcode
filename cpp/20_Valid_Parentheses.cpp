/*
date: 200926
idea: stack, push ([{, if encounter the corresponding character, stack pop. Finally, if stack is empty, return true, otherwise return flase.
*/

class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, int> m{{'(', 1}, {'[', 2}, {'{', 3}, {')', 4}, {']',5}, {'}', 6}};
        stack<char> st;
        bool isture = true;

        for(char c: s){
            int flag = m[c];
            if(flag>=1 && flag<=3) st.push(c);
            else if(!st.empty() && m[st.top()] == flag-3) st.pop();
            else return false;
        }
        if(st.empty()) return true;
        else return false;
    }
};
