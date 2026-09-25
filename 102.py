import json 
from typing import Optional
from collections import deque

class TreeNode :
    def __init__(self , val = 0 , left = None , right = None) :
        self.val = val
        self.left = left 
        self.right = right 


def build_tree(index : int , nums : list[int]) -> Optional[TreeNode]:
    if  index >= len(nums) or nums[index] is None :
        return None 

    root = TreeNode()
    root.val = nums[index]
    root.left = build_tree(index * 2 + 1 , nums)
    root.right = build_tree(index * 2 + 2 , nums)

    return root


class Solution :
    def levelOrder(self , root : TreeNode | None) -> list[list[int]] :
        if not root :
            return []

        q = deque([root])
        result = []

        while q :
            level_size = len(q)
            current_level = []

            for i in range(level_size) :
                cur_node = q.popleft()
                current_level.append(cur_node.val)

                if cur_node.left :
                    q.append(cur_node.left)
                if cur_node.right :
                    q.append(cur_node.right)

            result.append(current_level)

        return result 

data = [3,9,20,None,None,15,7]
root = build_tree(0 , data)
print(Solution().levelOrder(root))
