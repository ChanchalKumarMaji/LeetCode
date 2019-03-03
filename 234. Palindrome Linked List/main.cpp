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
    int length(ListNode* head){
        int l=0;
        while(head){
            l++;
            head = head->next; 
        }
        return l; 
    }
public:
    bool isPalindrome(ListNode* head) {
        if(!head || !head->next)  
            return true; 
        int l = length(head);  
 
        int forward;
        if(l%2==0)
            forward = l/2;
        else
            forward = (l-1)/2;
        ListNode *mid = head;
        forward--; 

        while(forward--){  
            mid = mid->next; 
        }
        ListNode* mid_next = mid->next;
        mid->next = NULL; 
        ListNode *p = reverseList(head), *q = mid_next; 
        if(l%2==1)
            q = q->next; 
        while(p && q){
            if(p->val != q->val)
                return false;
            p = p->next;
            q = q->next;
        }
        return true; 
    }
};
