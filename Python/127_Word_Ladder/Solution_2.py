class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # beginWord: "hit"
        # endWord: "cog"
        # wordList: ["hot","dot","dog","lot","log","cog"]
        # 
        # [1]
        # hashmap = {
        #     "*ot": ["hot", "dot", "lot"],
        #     "h*t": ["hot"],
        #     "ho*": ["hot"],
        #     ...
        # }
        #
        # [2]
        #                       hit- 1
        #                        |
        #                       h*t [hot-2]
        #                     /  |  \
        #                  *ot  h*t  ho*
        #      [hot, dot, lot]  [hot]  [hot]
        #            ...

        if not endWord in wordList: return 0
        
        str_length = len(beginWord)  
        all_sequence_dict = defaultdict(list)
        
        for word in wordList:
            for i in range(str_length): all_sequence_dict[word[:i] + "*" + word[i+1:]].append(word) 
                
        queue = deque([(beginWord, 1)])
        visited_words = set([beginWord])
        # BFS
        while queue:
            word, level = queue.popleft()
            for i in range(str_length): 
                contain_words = all_sequence_dict[word[:i] + "*" + word[i+1:]]
                for contain_word in contain_words:
                    if contain_word == endWord: 
                        return level + 1
                    elif not contain_word in visited_words: 
                        visited_words.add(contain_word)
                        queue.append((contain_word, level + 1))
        return 0