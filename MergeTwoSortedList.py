# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #Step 1 Initialize a new NODE in linked list
        head = ListNode(0)
        ptr=head
        
        #Step 2 Indifitely looping until condition is met
        
        while True:
            if l1 is None and l2 is None:
                break
            elif l1 is None:
                ptr.next = l2  
                break
            elif l2 is None:
                ptr.next = l1
                break
            else:
                # After sanity check move into main code
                smallerVal = 0
                if l1.val < l2.val:
                    smallerVal = l1.val
                    l1 = l1.next
                else:
                    smallerVal = l2.val
                    l2=l2.next
                
                newNode = ListNode(smallerVal)
                ptr.next = newNode
                ptr=ptr.next
        
        return head.next


solution = Solution()
print(solution.mergeTwoLists([1,2,4],[1,3,4]))