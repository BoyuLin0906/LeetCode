/*
Runtime 433 ms / Beats 78.99%
Memory 78.21 MB / Beats 52.26%
*/


type Node struct {
    Key  int
    Val  int
    Prev *Node
    Next *Node
}

type DoubleLinkedList struct {
    Head *Node
    Tail *Node
}

func CreateDoubleLinkedList() *DoubleLinkedList {
    head := &Node{Key: -1}
    tail := &Node{Key: -1}
    head.Next = tail
    tail.Prev = head
    return &DoubleLinkedList{Head: head, Tail: tail}
}

func (this *DoubleLinkedList) AddToHead(node *Node) {
    node.Prev = this.Head
    node.Next = this.Head.Next
    this.Head.Next.Prev = node
    this.Head.Next = node
}

func (this *DoubleLinkedList) Remove(node *Node) {
    node.Prev.Next = node.Next
    node.Next.Prev = node.Prev
    node.Next = nil
    node.Prev = nil
}

func (this *DoubleLinkedList) GetLastNode() *Node {
    node := this.Tail.Prev
    return node
}

type LRUCache struct {
    Capacity   int
    DoubleList *DoubleLinkedList
    Table      map[int]*Node
}

func Constructor(capacity int) LRUCache {
    doubleLinkedList := CreateDoubleLinkedList()
    return LRUCache{Capacity: capacity, 
                    DoubleList: doubleLinkedList, 
                    Table: make(map[int]*Node, capacity)}
}

func (this *LRUCache) Get(key int) int {
    if node, ok := this.Table[key]; ok {
        this.DoubleList.Remove(node)
        this.DoubleList.AddToHead(node)
        return node.Val
    }
    return -1
}

func (this *LRUCache) Put(key int, value int)  {
    if node, ok := this.Table[key]; ok {
        node.Val = value
        this.DoubleList.Remove(node)
        this.DoubleList.AddToHead(node)
    } else {
        if len(this.Table) >= this.Capacity {
            last_node := this.DoubleList.GetLastNode()
            delete(this.Table, last_node.Key)
            this.DoubleList.Remove(last_node)
        }
        new_node := &Node{Key: key, Val: value}
        this.DoubleList.AddToHead(new_node)
        this.Table[key] = new_node
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */