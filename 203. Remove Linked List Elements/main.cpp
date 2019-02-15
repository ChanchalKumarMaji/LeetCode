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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *prehead = new ListNode(0); 
        prehead->next = head;
        ListNode *prev = prehead, *curr = head, *next = NULL;
        while(curr){
            if(curr->val == val){
                curr = curr->next; 
                prev->next = curr; 
            }
            else{
                prev = curr;
                curr = curr->next; 
            }
        }
        return prehead->next; 
    }
};
