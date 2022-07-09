# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    # Morris Traversal
    def __init__(self, root: Optional[TreeNode]):
        self.curr_node = root
        self.left_traversal()

    def next(self) -> int:
        value = self.curr_node.val
        self.curr_node = self.curr_node.right
        self.left_traversal()
        return value
            
    def hasNext(self) -> bool:
        return True if self.curr_node else False
        
    def left_traversal(self):
        while self.curr_node:
            if self.curr_node.left:
                temp = self.curr_node.left
                while temp.right and temp.right != self.curr_node: temp = temp.right
                    
                if not temp.right:
                    temp.right = self.curr_node
                    self.curr_node = self.curr_node.left
                else:
                    temp.right = None
                    break
            else:
                break
                
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()