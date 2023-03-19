class WordDictionary:
    """
    Runtime 1397 ms / Beats 98.79%
    Memory 22.1 MB / Beats 97.41%
    """
    def __init__(self):
        self.dictionary = collections.defaultdict(set)

    def addWord(self, word: str) -> None:
        self.dictionary[len(word)].add(word)

    def search(self, word: str) -> bool:
        if "." not in word:
            return word in self.dictionary[len(word)]

        for dict_word in self.dictionary[len(word)]:
            is_break = False
            for idx, char in enumerate(word):
                if char != dict_word[idx] and char != '.':
                    is_break = True
                    break
            if not is_break:
                return True

        return False
