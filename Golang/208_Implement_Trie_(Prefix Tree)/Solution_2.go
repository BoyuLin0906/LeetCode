/*
Runtime 117 ms / Beats 5.02%
Memory 14.55 MB / Beats 96.35%
*/

type Trie struct {
    words []string
}


func Constructor() Trie {
    return Trie{words: []string{}}
}


func (this *Trie) Insert(word string)  {
    if slices.Contains(this.words, word) {
        return
    }
    this.words = append(this.words, word)
}


func (this *Trie) Search(word string) bool {
    if slices.Contains(this.words, word) {
        return true
    }
    return false
}


func (this *Trie) StartsWith(prefix string) bool {
    for _, word := range this.words {
        if strings.HasPrefix(word, prefix) {
            return true
        }
    }
    return false
}


/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */