/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        
        vector<int> v;
        for(auto node : lists){
            while(node != NULL){
                v.push_back(node->val);
                node = node->next; 
            }
        }
        if(v.size()==0)
            return NULL;
        sort(v.begin(), v.end());
        ListNode* head=NULL;
        ListNode* res;
        int f=0;
        for(auto x : v){
            ListNode* node = new ListNode(x);
            if(f==0){
                head = node;
                res = node;
                f = 1;
            }
            else{
                head->next = node;
                head = head->next;
            }
        }
        return res;
    }
};
