# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        Determines whether a linked list has a cycle.

        :type head: ListNode
        :rtype: bool
        """
        # If the head of the list is None, there is no cycle
        if head is None:
            return False
        
        # If the head's next pointer is None, there is no cycle (single node)
        elif head.next is None:
            return False
        
        # Marking the current node as checked
        head.val = "checked"
        # Moving to the next node
        head = head.next
        
        # Traverse through the linked list until reaching the end
        while head.next is not None:
            # If the current node is marked as checked, there is a cycle
            if head.val == "checked":
                return True
            else:
                # Mark the current node as checked
                head.val = "checked"
                
            # Move to the next node
            head = head.next
        
        # If reached the end without finding a cycle, return False
        return False
