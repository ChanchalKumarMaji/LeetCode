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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
     
        ListNode* p;
        int c1=0;
        int c2=0;
        p=headA;
        while(p!=NULL){
            c1++;
            p=p->next;
        }
        p=headB;
        while(p!=NULL){
            c2++;
            p=p->next;
        }
        if(c1>c2){
            for(int i=0;i<(c1-c2);i++)
                headA=headA->next;
        }
        else if(c1<c2){
            for(int i=0;i<(c2-c1);i++)
                headB=headB->next;
        }
        while(headA!=headB){
            headA=headA->next;
            headB=headB->next;
        }
        if(headA==NULL and headB==NULL)
            return NULL;
        return headA;
    }
};
