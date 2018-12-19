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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *prehead = new ListNode(0);
        prehead->next = head;
        ListNode *prev = prehead, *curr = head, *next = head; 
        while(curr && next){
            while(next && curr->val == next->val)
                next = next->next; 
            if(curr->next == next){
                prev = curr; 
                curr = curr->next;
            }
            else{
                prev->next = next; 
                curr = next;
            }
        }
        return prehead->next; 
    }
};
