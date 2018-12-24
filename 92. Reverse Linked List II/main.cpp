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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        ListNode *prehead = new ListNode(0);
        prehead->next = head;
        ListNode *p = prehead;
        for(int i=0; i<m-1; i++){
            p = p->next; 
        }
        ListNode *tail = p->next; 
        for(int i=0; i<(n-m); i++){
            ListNode *temp = p->next; 
            p->next = tail->next;
            tail->next = tail->next->next; 
            p->next->next = temp; 
        }
        return prehead->next; 
    }
};
