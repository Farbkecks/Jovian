import java.util.ArrayList;

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

    public String get(String key) {
        return findNode(node, key).value;
    }

    static TreeNode findNode(TreeNode node, String key) {
        int order = key.compareTo(node.key);
        if (order == 0) {
            return node;
        }
        if (order < 0) {
            return findNode(node.left, key);
        } else {
            return findNode(node.right, key);
        }
    }

    public void insert(String key, String value) {
        if (node == null) {
            node = new TreeNode(key, value);
            return;
        }

        insertLeftOrRight(node, key, value);
    }

    static void insertLeftOrRight(TreeNode node, String key, String value) {
        int order = key.compareTo(node.key);

        if (order < 0) {
            node.left = insertLeafOrNot(node.left, key, value);

        }
        if (order > 0) {
            node.right = insertLeafOrNot(node.right, key, value);
        }
    }

    static TreeNode insertLeafOrNot(TreeNode node, String key, String value) {
        if (node == null) {
            node = new TreeNode(key, value);
            return node;
        } else {
            insertLeftOrRight(node, key, value);
            return node;
        }
    }

    public String[] listAll() {
        ArrayList<String> arraylist = listAll(node);
        String[] list = new String[arraylist.size()];
        list = arraylist.toArray(list);
        return list;
    }

    static ArrayList<String> listAll(TreeNode node) {
        ArrayList<String> list = new ArrayList<String>();
        if (node.left != null) {
            list.addAll(listAll(node.left));
        }
        list.add(node.key);
        if (node.right != null) {
            list.addAll(listAll(node.right));
        }
        return list;
    }

    public void update(String key, String value) {
        findNode(node, key).value = value;
    }

    public void balance() {
        String[] list = listAll();
        this.node = balance(0, list.length - 1, null, list);
    }

    static TreeNode balance(int lo, int hi, TreeNode node, String[] list) {
        int mid = (lo + hi) / 2;
        if(node == null) {
            node = new TreeNode()
        }

    }
}
