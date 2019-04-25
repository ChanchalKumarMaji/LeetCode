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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        l1 = reverseList(l1);
        l2 = reverseList(l2);
        ListNode *prehead = new ListNode(0);
        ListNode *p = prehead;
        int extra = 0;
        while(l1 || l2 || extra){
            int sum = (l1?l1->val:0) + (l2?l2->val:0) + extra; 
            extra = sum/10;
            ListNode *node = new ListNode(sum%10); 
            p->next = node;
            p = p->next; 
            l1 = l1?l1->next:l1;
            l2 = l2?l2->next:l2;
        }
        
        return reverseList(prehead->next); 
        
    }
};
