/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        Map<Node, Node> map = new HashMap<>();
        map.put(null, null);
        Node cur = head;
        while(cur != null){
            Node placer = new Node(cur.val);
            map.put(cur, placer);
            cur = cur.next;
        }

        cur = head;
        while(cur != null){
            Node use = map.get(cur);
            use.random = map.get(cur.random);
            use.next = map.get(cur.next);
            cur = cur.next;
        }

        return map.get(head);
    }
}
