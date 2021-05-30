#python code to stringify linked list
def linked_list_str(l):
	if l is None:
		return '';
	return str(l.val)+'->'+linked_list_str(l.next)
	
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1=l1;
        p2=l2;
        carry=0;
        cur=ListNode(0)
        head=cur
        
        
        while p1 or p2 or carry:
            print(p1.val, p2.val, carry)
            sum = carry;
            sum=sum+(0 if p1 is None else p1.val)
            print("sum = "+str(sum))
            sum=sum+(0 if p2 is None else p2.val)
            print("Final sum = "+str(sum))

            if sum >= 10:
                sum = sum-10;
                carry = 1;
                
            else: 
                carry =0;
            print(sum,carry)
            
            cur.next = ListNode(sum)
            cur = cur.next
            if p1 is None and p2 is None:
                break;
            elif p1 is None:
                p2 = p2.next;
            elif p2 is None:
                p1 = p1.next
            else:
                p1=p1.next
                p2=p2.next
            
        return head.next
                
