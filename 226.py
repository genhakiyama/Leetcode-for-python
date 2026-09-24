from typing import Optional

class TreeNode:
    def __init__(self , val = 0 , left = None , right = None) :
        self.val = val
        self.left = left 
        self.right = right 

def build_tree(index : int , nums : list[int]) -> Optional[TreeNode]:
    if index >= len(nums) :
        return None 

    root = TreeNode()
    root.val = nums[index]
    root.left = build_tree(index * 2 + 1 , nums)
    root.right = build_tree(index * 2 + 2 , nums)

    return root

class Solution:
    def invertTree(self , root : Optional[TreeNode]) -> Optional[TreeNode] :
        if root == None :
            return root

        left = root.left
        right = root.right 
        root.right = self.invertTree(left)
        root.left = self.invertTree(right)

        return root 

def dfs(root : Optional[TreeNode]) :
    print(root.val)

    if root.left :
        dfs(root.left)
    if root.right :
        dfs(root.right) 


raw_input = input()
tree = list(map(int , raw_input.split())) if raw_input.strip() else [] 
root = build_tree(0 , tree)
root = Solution().invertTree(root)
dfs(root)