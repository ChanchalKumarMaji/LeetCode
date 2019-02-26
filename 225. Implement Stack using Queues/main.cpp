class MyStack {
    queue<int> q1;
    queue<int> q2;
public:
    /** Initialize your data structure here. */
    MyStack() {
        
    }
    
    /** Push element x onto stack. */
    void push(int x) {
        int a = q1.size();
        q1.push(x);
        while(a--){
            int e = q1.front();
            q1.pop();
            q1.push(e); 
        }
    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        int res = q1.front();
        q1.pop();
        return res;
    }
    
    /** Get the top element. */
    int top() {
        return q1.front();
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
        return q1.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * bool param_4 = obj.empty();
 */
