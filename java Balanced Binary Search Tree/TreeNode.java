public class TreeNode {
    public String key;
    public TreeNode left;
    public TreeNode right;
    public String value;
    public String parent;

    public TreeNode(String key, String value, String parent) {
        this.key = key;
        this.value = value;
        this.parent = parent;
    }
}
