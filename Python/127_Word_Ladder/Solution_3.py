class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord in wordList: return 0
        
        word_set = set(wordList)
        all_sequence_dict = defaultdict(list)
        str_length = len(wordList)
        
        for word in wordList:
            for i in range(str_length): all_sequence_dict[word[:i] + "*" + word[i+1:]].append(word) 
                
        forward_sequence = {beginWord}
        backward_sequence = {endWord}
        word_set.remove(endWord)
        level = 0
        
        # bidirectional BFS
        while len(forward_sequence) > 0 and len(backward_sequence) > 0:
            print(forward_sequence)
            print(backward_sequence)
            level += 1
            print(level)
            new_sequence = set()
            if len(forward_sequence) > len(backward_sequence): 
                forward_sequence, backward_sequence = backward_sequence, forward_sequence
            
            new_sequence = set()
            for current_word in forward_sequence:
                for i in range(str_length): 
                    next_words = all_sequence_dict[current_word[:i] + "*" + current_word[i+1:]]
                    for next_word in next_words:
                        # next forword word in backward_sequence means forward_sequence and backward_sequence find shortest connection
                        if next_word in backward_sequence: 
                            return level + 1
                        if next_word in word_set:
                            new_sequence.add(next_word)
                            word_set.remove(next_word)
            forward_sequence = new_sequence
            
        return 0