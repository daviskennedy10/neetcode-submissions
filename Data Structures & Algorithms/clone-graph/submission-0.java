/*
Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        HashMap<Node, Node> mapping = new HashMap<>();
        return dfs(node, mapping);
    }

    private Node dfs(Node node, HashMap<Node, Node> mapping){
        if(node == null){
            return null;
        }
        if(mapping.containsKey(node)){
            return mapping.get(node);
        }
        Node copy = new Node(node.val);
        mapping.put(node, copy);
        for(Node nei : node.neighbors){
            copy.neighbors.add(dfs(nei, mapping));
        }
        return copy;
    }
}