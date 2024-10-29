'''
Runtime 239 ms / Beats 7.15%
Memory 41.39 MB / Beats 16.51%
'''

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()

        for f in folder:
            f = f.replace("/", " ").strip()
            f = f.split(" ")
            trie.insert(f)

        res = set()
        for f in folder:
            f = f.replace("/", " ").strip()
            f = f.split(" ")
            path = trie.search_root_folder(f)
            res.add(path)

        return list(res)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_folder = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            if not char in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_folder = True

    def search_root_folder(self, word):
        node = self.root

        root_folder = ""
        for char in word:
            node = node.children[char]
            root_folder += "/" + char
            if node.is_folder:
                return root_folder
        
        return root_folder