/*
Date: 200926
Idea: 
1. two stack, store data and the minimum in the current stack, respectively.
2. one stack stores pair structure <data, minimum>, and use *min* var to store current minimum
*/

class MinStack_1 {
    stack<int> x_stack;
    stack<int> min_stack;
public:
    /** initialize your data structure here. */
    MinStack() {
        min_stack.push(INT_MAX);
    }
    
    void push(int x) {
        x_stack.push(x);
        min_stack.push(min(min_stack.top(), x));
    }
    
    void pop() {
        x_stack.pop();
        min_stack.pop();
    }
    
    int top() {
        return x_stack.top();
    }
    
    int getMin() {
        return min_stack.top();
    }
};

/***************************************************************************************/

class MinStack_2 {
    int min = INT_MAX;
    stack<pair<int, int>> min_stack;
public:

    void push(int x) {
        if(x < min) min = x;
        min_stack.push(make_pair(x, min));
    }
    
    void pop() {
        min_stack.pop();
        if(min_stack.empty()) min = INT_MAX;
        else min = min_stack.top().second;
    }
    
    int top() {
        return min_stack.top().first;
    }
    
    int getMin() {
        return min_stack.top().second;
    }
};
