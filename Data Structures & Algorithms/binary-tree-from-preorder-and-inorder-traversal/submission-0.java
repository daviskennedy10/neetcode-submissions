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
    private HashMap<Integer, Integer> map;
    private int preOrderIndex;
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if(preorder == null || inorder == null){
            return null;
        }
        map = new HashMap<>();
        preOrderIndex = 0;
        for(int i = 0; i < inorder.length; i++){
            map.put(inorder[i], i);
        }

        return helper(preorder, 0, inorder.length - 1);

    }
    private TreeNode helper(int[] preorder, int left, int right){
        if(left > right){
            return null;
        }
        int rootVal = preorder[preOrderIndex++];
        TreeNode root = new TreeNode(rootVal);

        int inorderIndex = map.get(rootVal);

        root.left = helper(preorder, left, inorderIndex - 1);
        root.right =helper(preorder, inorderIndex + 1, right );

        return root;

    
    }
}
