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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *prehead = new ListNode(0);
        ListNode *p = prehead;
        int extra = 0;
        while(l1 || l2 || extra){
            int sum = (l1?l1->val:0) + (l2?l2->val:0) + extra;
            l1 = l1?l1->next:l1;
            l2 = l2?l2->next:l2; 
            extra = sum/10;
            ListNode *node = new ListNode(sum%10);
            p->next = node;
            p = p->next; 
        }
        return prehead->next; 
    }
};
