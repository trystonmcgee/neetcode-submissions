# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def max_diameter(root):
            if not root:
                return 0
            
            current_diameter = height(root.left) + height(root.right)

            left_diameter = max_diameter(root.left)
            right_diameter = max_diameter(root.right)
            
            return max(current_diameter, left_diameter, right_diameter)
                
        def height(root):
            if not root:
                return 0
            
            return 1 + max(height(root.left), height(root.right))
        
        return max_diameter(root)