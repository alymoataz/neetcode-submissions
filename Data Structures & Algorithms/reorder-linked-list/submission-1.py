# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return 
        slow,fast=head,head
        while fast and fast.next: #find mid of list
            slow=slow.next
            fast=fast.next.next
        curr=slow.next #start of second half
        slow.next=None #seperating list
        prev=None
        while curr: #reverse second list
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        back=prev
        front=head
        while back:
            t1=front.next
            t2=back.next
            front.next=back
            back.next=t1
            front=t1
            back=t2
        


        

    
        