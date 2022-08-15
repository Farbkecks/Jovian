class App {
    public static void main(String[] args) {
        TreeMap tree = new TreeMap("Hans");
        tree.node.left = new TreeNode("Abc");
        tree.node.right = new TreeNode("Zab");
        tree.node.right.left = new TreeNode("sdjfklsdf");
        tree.display();
    }
}
