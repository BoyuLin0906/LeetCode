class TrieNode:
    def __init__(self):
        self.next = dict()
        self.is_word = False

class WordDictionary:
    """
    Runtime 8817 ms / Beats 76.70%
    Memory 78 MB / Beats 51.50%
    """
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        trie_dict = self.trie
        for idx in range(len(word)):
            char = word[idx]
            if not char in trie_dict:
                trie_dict[char] = TrieNode()
            if len(word) == idx+1:
                trie_dict[char].is_word = True
            
            trie_dict = trie_dict[char].next

    def search(self, word: str) -> bool:
        self.is_exist = False
        self.dfs(word, self.trie, 0)
        return self.is_exist

    def dfs(self, word, node_dict, idx):
        if self.is_exist or idx >= len(word): 
            return

        char = word[idx]
        if char == "." and node_dict:
            if len(word) == idx+1:
                for char, _ in node_dict.items():
                    if node_dict[char].is_word:
                        self.is_exist = True
            else:
                for _, next_node in node_dict.items():
                    self.dfs(word, next_node.next, idx+1)
        elif char in node_dict:
            if len(word) == idx+1 and node_dict[char].is_word:
                self.is_exist = True
            else:
                self.dfs(word, node_dict[char].next, idx+1)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)