class App {
    public static void main(String[] args) {
        TreeMap tree = new TreeMap();
        // tree.insert("jadhesh", "1");
        // tree.insert("biraj", "2");
        // tree.insert("aakash", "3");
        // tree.insert("hemanth", "4");
        // tree.insert("sonaksh", "5");
        // tree.insert("siddhant", "6");
        // tree.insert("vishal", "7");

        for (int i = 0; i < 10; i++) {
            String y = "" + i;
            tree.insert(y, y);
        }
        tree.display();

    }
}
