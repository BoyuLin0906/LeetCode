class Trie:

    def __init__(self):
        self.words = defaultdict(int)

    def insert(self, word: str) -> None:
        temp_word = ""
        self.words[word] = 2
        for char in word:
            temp_word += char
            if not self.words[temp_word]: self.words[temp_word] = 1
        

    def search(self, word: str) -> bool:
        return True if self.words[word] == 2 else False

    def startsWith(self, prefix: str) -> bool:
        return True if self.words[prefix] else False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)