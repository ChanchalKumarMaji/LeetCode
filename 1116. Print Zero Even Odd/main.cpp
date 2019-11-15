class ZeroEvenOdd {
private:
    int n, cur;
    mutex m1, m2, m3;
public:
    ZeroEvenOdd(int n) {
        this->n = n;
        cur = 1;
        m2.lock();
        m3.lock();
    }

    // printNumber(x) outputs "x", where x is an integer.
    void zero(function<void(int)> printNumber) {
        for(int i = 0; i < n; i++){
            m1.lock();
            printNumber(0);
            if(cur&1) m2.unlock();
            else m3.unlock();
        }    
    }

    void even(function<void(int)> printNumber) {
        for(int i = 0; i < n/2; i++){
            m3.lock();
            printNumber(cur); cur++;
            m1.unlock();
        }    
    }

    void odd(function<void(int)> printNumber) {
        for(int i = 0; i < (n+1) / 2; i++){
            m2.lock();
            printNumber(cur); cur++;
            m1.unlock();
        }    
    }
};
