class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Time Limit Exceeded
        if not endWord in wordList: return 0
        
        self.shortest_sequence_number = 10000000
        graph_dict = {beginWord: []}
        
        def match(str1, str2):
            count = 0
            for (char1, char2) in zip(str1, str2):
                if char1 != char2: count +=1
                if count > 1: return False 
            return True
        
        def dfs(head_word, words, records, count):
            if head_word == endWord:
                self.shortest_sequence_number = min(self.shortest_sequence_number, count)
            elif self.shortest_sequence_number > count:
                for word in words:
                    if not word in records:
                        dfs(word, graph_dict[word], records+[head_word], count+1)
        
        # begin word
        for next_word in wordList:
            if match(beginWord, next_word): graph_dict[beginWord].append(next_word)
        
        # create graph
        for head_word in wordList:
            graph_dict[head_word] = []
            for next_word in wordList:
                if match(head_word, next_word) and head_word != next_word:
                    graph_dict[head_word].append(next_word)
                    
        # dfs first           
        dfs(beginWord, graph_dict[beginWord], [], 1)
        
        if self.shortest_sequence_number == 10000000: return 0
        return self.shortest_sequence_number