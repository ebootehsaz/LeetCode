import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
time complexity: O(N log k)
N = the total number of nodes in all the linked lists 
k = the number of linked lists.
"""
def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """

    head = curr = ListNode()
    if lists == []:
        return None
    
    heap = []
    heapq.heapify(heap)

    for nodePtr in lists: # place elements in min heap - sorted by first element
        if nodePtr:
            heapq.heappush(heap, (nodePtr.val, id(nodePtr), nodePtr))


    while len(heap) != 0:
        (myMin, _, nodePtr) = heapq.heappop(heap)
        curr.next = nodePtr
        curr = curr.next

        nodePtr = nodePtr.next
        if nodePtr:
            heapq.heappush(heap, (nodePtr.val, id(nodePtr), nodePtr))


    return head.next


def list_to_linked_list(lst):
    if not lst:
        return None
    
    head = ListNode(lst[0])
    current = head
    
    for i in range(1, len(lst)):
        current.next = ListNode(lst[i])
        current = current.next
    
    return head

# tests
l = [list_to_linked_list([1,5]), list_to_linked_list([1,3,4]), list_to_linked_list([2,6])]
res = mergeKLists(l)
while res:
    print(res.val, end=",")
    res = res.next

l = [list_to_linked_list([0,2,5])]
res = mergeKLists(l)
print()
while res:
    print(res.val, end=",")
    res = res.next

l = [list_to_linked_list([0]),list_to_linked_list([1])]
res = mergeKLists(l)
print()
while res:
    print(res.val, end=",")
    res = res.next
print()