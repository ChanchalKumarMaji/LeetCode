/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
    ListNode* reverseList(ListNode* head){
        ListNode *prev = NULL, *curr = head, *next = NULL;
        while(curr){
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next; 
        }
        return prev;   
    }
public:
    void reorderList(ListNode* head) {
        if(!head || !head->next)
            return;
        
        ListNode *slow = head, *fast = head->next;
        while(fast->next && fast->next->next){ 
            slow = slow->next;
            fast = fast->next->next; 
        }
        
        ListNode *h = slow->next; 
        slow->next = NULL;
        
        ListNode *rev = reverseList(h);
        
        ListNode *p = head, *q = rev; 
        
        int flag = 0;
        ListNode *curr = p; 
        while(p && q){
            if(flag == 0){
                p = p->next;
                curr->next = q;
                curr = q;
                flag = 1;
            }
            else if(flag == 1){
                q = q->next;
                curr->next = p;
                curr = p;
                flag = 0;
            }
        }
        
        
        
    }
};
