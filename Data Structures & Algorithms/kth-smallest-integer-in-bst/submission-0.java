/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int kthSmallest(TreeNode root, int k) {
        Queue<TreeNode> pq = new LinkedList<>();
        PriorityQueue<Integer> vals = new PriorityQueue<>();
        pq.add(root);
        vals.add(root.val);
        while(!pq.isEmpty()){
            TreeNode placer = pq.poll();
            if(placer.left != null){
                pq.add(placer.left);
                vals.add(placer.left.val);
            }
            if(placer.right != null){
                pq.add(placer.right);
                vals.add(placer.right.val);
            }
        }
        int result = 0;
        for(int i = 1; i < k+1; i++){
            result = vals.poll();
        }
        return result;
    }
}
