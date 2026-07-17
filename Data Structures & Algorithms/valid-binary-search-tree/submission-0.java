class Solution {
    public boolean isValidBST(TreeNode root) {
        return helper(root, null, null);
    }

    private boolean helper(TreeNode node, Integer lower, Integer upper) {
        if (node == null) return true;

        int val = node.val;
        if (lower != null && val <= lower) return false;
        if (upper != null && val >= upper) return false;

        // Left subtree: upper bound becomes current node's value
        if (!helper(node.left, lower, val)) return false;
        // Right subtree: lower bound becomes current node's value
        if (!helper(node.right, val, upper)) return false;

        return true;
    }
}
