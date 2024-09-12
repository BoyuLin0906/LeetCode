/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */
type CopyListStruct struct {
    CopyNode  *Node
    RandomIdx int
}

func copyRandomList(head *Node) *Node {
    random_list := make([]*CopyListStruct, 0, 1000)

    org_head := head
    for head != nil {
        trace_head := org_head
        rand_idx := -1
        if head.Random != nil {
            rand_idx = 0
            for trace_head != head.Random {
                trace_head = trace_head.Next
                rand_idx++
            }
        }
        temp := &Node{Val: head.Val}
        random_list = append(random_list, &CopyListStruct{CopyNode: temp, RandomIdx: rand_idx})
        head = head.Next
    }

    dummy_head := &Node{Val: -1}
    running_head := dummy_head
    for i := 0; i < len(random_list); i++ {
        running_head.Next = random_list[i].CopyNode
        rand_idx := random_list[i].RandomIdx
        if rand_idx != -1 {
            running_head.Next.Random = random_list[rand_idx].CopyNode
        }
        running_head = running_head.Next
    }

    return dummy_head.Next
}