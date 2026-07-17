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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new LinkedList<>();
        Queue<TreeNode> q = new LinkedList<>();
        if(root == null){
            return result;
        }
        q.offer(root);
        while(!q.isEmpty()){
            List<Integer> list = new LinkedList<>();
            int size = q.size();
            for(int i = 0; i < size; i++){
                TreeNode get = q.poll();
                list.add(get.val);
                if(get.left != null){
                    q.offer(get.left);
                }
                if(get.right != null){
                    q.offer(get.right);
                }
            }
            result.add(list);
        }
        return result;
    }
}
