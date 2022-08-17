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
            node = new TreeNode(key, value, null);
            return;
        }

        insertLeftOrRight(node, key, value);
    }

    static void insertLeftOrRight(TreeNode node, String key, String value) {
        int order = key.compareTo(node.key);

        if (order < 0) {
            node.left = insertLeafOrNot(node.left, key, value, node.key);

        }
        if (order > 0) {
            node.right = insertLeafOrNot(node.right, key, value, node.key);
        }
    }

    static TreeNode insertLeafOrNot(TreeNode node, String key, String value, String parent) {
        if (node == null) {
            node = new TreeNode(key, value, parent);
            return node;
        } else {
            insertLeftOrRight(node, key, value);
            return node;
        }
    }

    public TreeNode[] listAll() {
        ArrayList<TreeNode> arraylist = listAll(node);
        TreeNode[] list = new TreeNode[arraylist.size()];
        list = arraylist.toArray(list);
        return list;
    }

    static ArrayList<TreeNode> listAll(TreeNode node) {
        ArrayList<TreeNode> list = new ArrayList<TreeNode>();
        if (node.left != null) {
            list.addAll(listAll(node.left));
        }
        list.add(node);
        if (node.right != null) {
            list.addAll(listAll(node.right));
        }
        return list;
    }

    public void update(String key, String value) {
        findNode(node, key).value = value;
    }

    public void balance() {
        TreeNode[] list = listAll();
        this.node = balance(0, list.length - 1, null, list, null);
    }

    static TreeNode balance(int lo, int hi, TreeNode node, TreeNode[] list, String parent) {
        int mid = (lo + hi) / 2;
        if (lo > hi) {
            return node;
        }
        if (node == null) {
            node = new TreeNode(list[mid].key, list[mid].value, parent);
        }
        node.left = balance(lo, mid - 1, node.left, list, list[mid].key);
        node.right = balance(mid + 1, hi, node.right, list, list[mid].key);
        return node;
    }

    public void delete(String key) {
        TreeNode treenode = findNode(node, key);
        TreeNode parendnode = findNode(node, treenode.parent);
        if (treenode.right == null && treenode.left == null) {
            if (parendnode.left.key == key) {
                parendnode.left = null;
            }
            if (parendnode.right.key == key) {
                parendnode.right = null;
            }
        }
        // int order = treenode.left.key.compareTo(treenode.right.key);
        // if (order < 0) {
        // parendnode.left = treenode.right;
        // }

    }
}