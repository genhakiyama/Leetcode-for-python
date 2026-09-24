from typing import Optional

class Listnode :
    def __init__(self , val = 0 , next = None):
        self.val = val
        self.next = next

def create_linked_list(arr : list) -> Optional[Listnode] :
    if not arr :
        return None 

    head = Listnode(arr[0])
    current = head 

    for val in arr[1:] :
        current.next = Listnode(val)
        current = current.next 

    return head 

def print_linked_list(ptr : Optional[Listnode]) :
    elements = []
    current = ptr 

    while current :
        elements.append(str(current.val))
        current = current.next

    print("->".join(elements) if elements else "Empty")

class Solution :
    def mergeTwolists(self , list1 : Optional[Listnode] , list2 : Optional[Listnode]) -> Optional[Listnode]:
        head = Listnode(-1)
        current = head

        while list1 and list2 :
            if (list1.val <= list2.val) :
                current.next = list1
                list1 = list1.next 
            else :
                current.next = list2
                list2 = list2.next

        current.next = list1 if list1 else list2 

        return head

raw_input_1 = input()
raw_input_2 = input()
list1 = list(map(int , raw_input_1.split()))
list2 = list(map(int , raw_input_2.split()))
head1 = create_linked_list(list1)
head2 = create_linked_list(list2)

print_linked_list(Solution().mergeTwolists(head1,head2))

        