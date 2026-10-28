# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        head=dummy
        head1=list1
        head2=list2
        while head1 and head2:
            if head1.val<=head2.val:
                head.next=ListNode(head1.val)
                head=head.next
                head1=head1.next
            else:
                head.next=ListNode(head2.val)
                head=head.next
                head2=head2.next
        while head1:
            head.next=ListNode(head1.val)
            head=head.next
            head1=head1.next
        while head2:
            head.next=ListNode(head2.val)
            head=head.next
            head2=head2.next
        return dummy.next    


    
        