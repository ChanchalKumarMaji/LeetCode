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
        ListNode *curr = head, *next = head; 
        while(curr && next){
            while(next && curr->val == next->val) 
                next = next->next; 
            curr->next = next;
            curr = next; 
        }
        return head; 
    }
};
