/*
Runtime 43 ms / Beats 88.28%%
Memory 14.55 MB / Beats 53.58%
*/

type Trie struct {
    nxt [26]*Trie
    is_word bool 
}

func Constructor() Trie {
    return Trie{}
}

func (this *Trie) Insert(word string)  {
    if len(word) == 0 {
        this.is_word = true
        return
    }
    if this.nxt[word[0]-'a'] != nil {
        this.nxt[word[0]-'a'].Insert(word[1:])
    } else {
        nxt_trie := &Trie{}
        nxt_trie.Insert(word[1:])
        this.nxt[word[0]-'a'] = nxt_trie
    }
}


func (this *Trie) Search(word string) bool {
    if len(word) == 0 {
        return this.is_word
    }
    if this.nxt[word[0]-'a'] == nil {
        return false
    }
    return this.nxt[word[0]-'a'].Search(word[1:])
}


func (this *Trie) StartsWith(prefix string) bool {
    if len(prefix) == 0 {
        return true
    }
    if this.nxt[prefix[0]-'a'] == nil {
        return false
    }
    return this.nxt[prefix[0]-'a'].StartsWith(prefix[1:])
}


/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */