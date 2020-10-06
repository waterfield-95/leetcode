/*
date: 201006
idea: iteration or recursion of swap in place
*/

class Solution {
public:
    void recursion(vector<char>& s, int left, int right){
        if(left >= right) return;
        swap(s[left], s[right]);
        recursion(s, left+1, right-1);
    }

    void reverseString(vector<char>& s) {
        int size = s.size();
        helper(s, 0, size-1);
    }
};

class Solution2 {
    int idx = 0;
public:
    void reverseString(vector<char>& s) {
        int size = s.size();
        for(int i=0; i<size; i++){
            s.insert(s.begin()+i, s.back());
            s.pop_back();
        }

    }
};
