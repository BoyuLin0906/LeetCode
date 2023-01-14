class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # init
        ds = DisjointSet(s1 + s2) 
        # union
        for c1, c2 in zip(s1, s2):
            ds.union(c1, c2)
        # find
        res = ''
        for base_c in baseStr:
            res += ds.find(base_c)

        return res


class DisjointSet:
    def __init__(self, elements):
        self.parents = {char:char for char in elements}

    def find(self, element):
        if element in self.parents:
            n = self.parents[element]
            while self.parents[n] != n:
                n = self.parents[n]
            return n
        return element
            
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            if u > v:
                self.parents[u] = v
            else:
                self.parents[v] = u