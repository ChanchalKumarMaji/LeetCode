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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* p=head;
        if(head->next==NULL)
            return NULL;
        int l=0;
        while(p!=NULL){
            l++;
            p=p->next;
        }
        p=head;
        int pos=l-n-1;
        if(pos==-1){
            head=head->next;
            return head;
        }
        while(pos>0){
            p=p->next;
            pos--;
        }
        p->next=p->next->next;      
       
        return head;
    }
    
};
