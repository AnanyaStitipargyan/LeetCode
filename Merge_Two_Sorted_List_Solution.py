# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Merge_Two_Sorted_List_Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        if l1.val >= l2.val:
            current1 = l2
            current2 = l1
        else:
            current1 = l1
            current2 = l2
            
        r = l1.val >= l2.val
        
        tmp = None
        while current1 and current2:
            if current2.val >= current1.val and (current1.next is None or current2.val<=current1.next.val):
                tmp = current2.next
                current2.next = current1.next
                current1.next = current2
                current1 = current1.next
                current2 = tmp
            else:
                current1 = current1.next
        
        if r:
            return l2
        else:
            return l1
