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
    ListNode *detectCycle(ListNode *head) {
        if(!head || !head->next)
            return NULL; 
        ListNode *slow = head, *fast = head;
        do{
            if(!fast || !fast->next)
                return NULL; 
            slow = slow->next;
            fast = fast->next->next; 
        }while(slow != fast);
        slow = head;
        while(slow != fast){
            slow = slow->next;
            fast = fast->next;
        }
        return slow; 
    }
};
