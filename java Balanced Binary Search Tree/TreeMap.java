public class TreeMap {

    public TreeNode node;

    public TreeMap() {
        this.node = null;
    }

    public void display() {
        display(node, 0);
    }

    static void display(TreeNode node, int level) {
        String SPACE = "      ";
        if (node == null) {
            for (int i = 0; i < level; i++) {
                System.out.print(SPACE);
            }
            System.out.println("∅");
            return;
        }
        if (node.left == null && node.right == null) {
            for (int i = 0; i < level; i++) {
                System.out.print(SPACE);
            }
            System.out.println(node.key);
            return;
        }

        display(node.right, level + 1);
        for (int i = 0; i < level; i++) {
            System.out.print(SPACE);
        }
        System.out.println(node.key);
        display(node.left, level + 1);
    }

    public void insert(String key) {
        if (node == null) {
            node = new TreeNode(key);
            return;
        }

        insert(node, key);
    }

    static void insert(TreeNode node, String key) {
        int value = key.compareTo(node.key);

        if (value < 0) {
            node.left = insertLeftOrRight(node.left, key);

        }
        if (value > 0) {
            node.right = insertLeftOrRight(node.right, key);
        }
    }

    static TreeNode insertLeftOrRight(TreeNode node, String key) {
        if (node == null) {
            node = new TreeNode(key);
            return node;
        } else {
            insert(node, key);
            return node;
        }
    }

    // public String[] list_all() {

    // }
}
