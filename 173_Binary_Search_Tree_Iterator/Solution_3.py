# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.node_list = list()
        self.left_traversal(root)

    def next(self) -> int:
        node = self.node_list.pop()
        self.left_traversal(node.right)
        return node.val
            
    def hasNext(self) -> bool:
        return True if self.node_list else False
        
    def left_traversal(self, node):
        while node:
            self.node_list.append(node)
            node = node.left
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()