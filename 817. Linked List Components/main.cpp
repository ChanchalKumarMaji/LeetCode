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
    int numComponents(ListNode* head, vector<int>& G) {
        if(head==NULL or G.size()==0)
            return G.size();
        
        ListNode *temp=head;
        while(temp->next!=NULL)
            temp=temp->next;
        struct ListNode* node=(ListNode*)malloc(sizeof(ListNode));
        node->val=-1;
        node->next=NULL;
        temp->next=node;
        
        int count=0;
        while(head!=NULL and head->next!=NULL){
            int v1=head->val;
            int v2=head->next->val;
            int f1=0,f2=0;
            
            for(int i=0;i<G.size();i++){
                if(G[i]==v1)
                    f1=1;
                if(G[i]==v2)
                    f2=1; 
            }
            if(f1==1 and f2==0)
                count++;
            head=head->next;
        }
        return count;
    }
};
