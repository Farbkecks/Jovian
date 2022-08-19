class App {
    public static void main(String[] args) {
        TreeMap tree = new TreeMap();

        tree.insert("aakash", "3");
        tree.insert("biraj", "2");
        tree.insert("hemanth", "4");
        tree.insert("jadhesh", "1");
        tree.insert("siddhant", "6");
        tree.insert("sonaksh", "5");
        tree.insert("vishal", "7");
        tree.insert("soa", "7");
        tree.insert("soaa", "7");
        tree.insert("soaz", "7");
        // tree.insert("soz", "7");
        tree.insert("soza", "7");
        tree.insert("sozz", "7");

        tree.balance();
        tree.display();
        System.out.println("------------------------------------------------------------");
        tree.delete("soa");
        tree.display();

        // System.out.println(tree.get("aakash"));
        // tree.update("aakash", "sjdkfl");
        // System.out.println(tree.get("aakash"));
    }
}