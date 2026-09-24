from collections import deque
from typing import Optional

class ListNode :
    def __init__(self , val = 0 , next = None) :
        self.val = val
        self.next = next 

class Solution :
    def reversed(self , head : Optional[ListNode]) -> Optional[ListNode] :
        q = deque()

        while head :
            q.append(head)
            head = head.next 

        reversed_head = ListNode(-1)
        current = reversed_head
        
        while q : 
            node = q.pop()
            node.next = None
            current.next = node 
            current = current.next 

        return reversed_head.next

def created_linked_list(arr : list[int]) -> Optional[ListNode] :
    if not arr :
        return None 
    
    root = ListNode(arr[0])
    current = root 
    for x in arr[1:]:
        current.next = ListNode(x)
        current = current.next

    return root

def print_linked_list(root : Optional[ListNode]) :
    element = []
    while root :
        element.append(str(root.val))
        root = root.next 

    print("->".join(element) if element else "")

raw_input = input()
arr = list(map(int , raw_input.split())) if raw_input.strip() else [] 
root = created_linked_list(arr)
print_linked_list(Solution().reversed(root))
        
