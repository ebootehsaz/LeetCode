# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        index = []
        if head.next == None: return None 
        
        ptr = head 

        while ptr != None:
            index.append(ptr)
            ptr = ptr.next 

        if abs((-n)-1) > len(index):
            return head.next
            
        skipper = index[(-n)-1]
        if n != 1:
            skipper.next = skipper.next.next
        else:
            skipper.next = None


        return head



"""
# very good solution
        dummyHead = ListNode(None, head)
        slow, fast = dummyHead, head

        while fast and n > 0:
            fast = fast.next
            n -= 1
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummyHead.next
        """

