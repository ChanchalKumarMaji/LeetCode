class MinStack {
public:
    /** initialize your data structure here. */
    stack<int> s;
    stack<int> m;
    MinStack() {
        
    }
    
    void push(int x) {
        if(s.empty()){
            s.push(x);
            m.push(x);
        }
        else{
            s.push(x);
            if(x<m.top())
                m.push(x);
            else
                m.push(m.top()); 
        }
    }
    
    void pop() {
        s.pop();
        m.pop();
    }
    
    int top() {
        return s.top();
    }
    
    int getMin() {
        return m.top(); 
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
