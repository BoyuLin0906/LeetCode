# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.values = list()
        self.traversal(root)

    def next(self) -> int:
        return self.values.pop()
            
    def hasNext(self) -> bool:
        return True if self.values else False
        
    def traversal(self, node):
        if not node: return 
        if node.right: self.traversal(node.right)
        self.values.append(node.val)
        if node.left: self.traversal(node.left)
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()