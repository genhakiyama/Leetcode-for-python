from typing import Optional
import ast 

class ListNode :
    def __init__(self , val , next = None) :
        self.val = val
        self.next = next 

class Solution :
    def hasCycle(self , head : Optional[ListNode]) -> bool :
        appeared = dict()

        while head :
            if head in appeared :
                return True 

            appeared[head] = 1
            head = head.next 

        return False 

def created_linked_list(arr : int , pos : int) -> Optional[ListNode] : 
    root = ListNode(arr[0]) 
    current = root
    cycle_target = root if pos == 0 else None 

    for index,x in enumerate(arr[1:] , 1):
        current.next = ListNode(x)    
        current = current.next 
        if (index == pos) :
            cycle_target = current 

    if pos != -1 and cycle_target :
        current.next = cycle_target

    return root

user_input = input()
pos = int(input())
arr = ast.literal_eval(user_input)

print(Solution().hasCycle(created_linked_list(arr , pos)))