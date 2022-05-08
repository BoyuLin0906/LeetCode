# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    """
    Runtime: 89 ms, faster than 48.24% of Python3 online submissions for Flatten Nested List Iterator.
    Memory Usage: 17.7 MB, less than 87.28% of Python3 online submissions for Flatten Nested List Iterator.
    """
    def __init__(self, nestedList: [NestedInteger]):
        self.result = []
        for nested_obj in nestedList: self.DFS(nested_obj)
        self.result = self.result[::-1]
    
    def next(self) -> int:
        return self.result.pop()
    
    def hasNext(self) -> bool:
        return True if self.result else False
         
    def DFS(self, nest_int):
        if nest_int.isInteger():
            self.result.append(nest_int.getInteger())
        else:
            for n in nest_int.getList(): self.DFS(n)
            
            
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())