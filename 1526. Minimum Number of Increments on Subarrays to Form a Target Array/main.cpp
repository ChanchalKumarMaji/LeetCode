class Solution {
public:
    
    vector<int> segmentTree;
    vector<int> arr;
    int n;

    // O(n)
    int build(int node, int left, int right) {
        if(left == right) {
            return segmentTree[node] = left;
        }
        int leftNode = node << 1;
        int rightNode = leftNode | 1;
        int mid = left + (right - left) / 2;
        int leftIdx = build(leftNode, left, mid);
        int rightIdx = build(rightNode, mid + 1, right);
        return segmentTree[node] = (arr[leftIdx] <= arr[rightIdx]) ? leftIdx : rightIdx;
    }

    int query(int node, int left, int right, int x, int y) {
        if(x > right or y < left) return -1;
        if(left >= x and right <= y) return segmentTree[node];
        int leftNode = node << 1;
        int rightNode = leftNode | 1;
        int mid = left + (right - left) / 2;
        int leftIdx = query(leftNode, left, mid, x, y);
        int rightIdx = query(rightNode, mid + 1, right, x, y);
        if(leftIdx == -1) return rightIdx;
        if(rightIdx == -1) return leftIdx;
        return (arr[leftIdx] <= arr[rightIdx]) ? leftIdx : rightIdx;
    }

    int query(int x, int y) {
        return query(1, 0, n - 1, x, y);
    }

    int convertUtil(int left, int right, int dx) {
        if(left > right) return 0;
        int mid = query(left, right);
        int minElement = arr[mid];

        int cnt = 0; // the number of operation

        // dx is the amount that has been already decremented from this range
        // So you have to treat every element X as (X - dx)
        cnt += (minElement - dx);

        cnt += convertUtil(left, mid - 1, minElement) + convertUtil(mid + 1, right, minElement);

        return cnt;
    }

    int convert(vector<int>& arr) {
        this->arr = arr;
        this->n = arr.size();
        segmentTree.clear();
        const int SIZE  = 1000000;
        segmentTree.resize(SIZE, 0);
        build(1, 0, n - 1);
        return convertUtil(0, n - 1, 0);
    }
    
    int minNumberOperations(vector<int>& target) {
        return convert(target);
    }
};
