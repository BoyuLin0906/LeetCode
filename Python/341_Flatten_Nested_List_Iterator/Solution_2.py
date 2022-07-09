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
    def __init__(self, nestedList: [NestedInteger]):
        """
        Runtime: 64 ms, faster than 94.14% of Python3 online submissions for Flatten Nested List Iterator.
        Memory Usage: 17.8 MB, less than 41.16% of Python3 online submissions for Flatten Nested List Iterator.
        """
        self.result = []
        self.len = 0
        self.index = 0
        for nested_obj in nestedList: self.DFS(nested_obj)
    
    def next(self) -> int:
        result = self.result[self.index]
        self.index += 1
        return result
    
    def hasNext(self) -> bool:
        return True if self.len > self.index else False
         
    def DFS(self, nest_int):
        if nest_int.isInteger():
            self.result.append(nest_int.getInteger())
            self.len += 1
        else:
            for n in nest_int.getList(): self.DFS(n)
            
            
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())