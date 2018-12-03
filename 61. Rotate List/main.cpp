/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
    int length(ListNode* head){
        int l = 0;
        while(head){
            l++;
            head = head->next; 
        }
        return l; 
    }
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if(!head)
            return head; 
        int l = length(head);
        k = k%l;
        if(k == 0)
            return head;
        int shift = l-k-1; 
        ListNode *p = head;
        while(shift--){
            p = p->next; 
        }
        ListNode *new_head = p->next;
        p->next = NULL;
        p = new_head; 
        while(p->next){
            p = p->next;
        }
        p->next = head;
        return new_head; 
    }
};
