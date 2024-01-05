import java.io.*;
import java.util.Scanner;

class LibraryNode {
    String ciu;
    String pr;
    LibraryNode left, right;

    public LibraryNode(String ciu, String pr) {
        this.ciu = ciu;
        this.pr = pr;
        this.left = null;
        this.right = null;
    }
}

class BinarySearchTree {
    private LibraryNode root;

    public BinarySearchTree() {
        root = null;
    }

    public void insert(String ciu, String pr) {
        root = insertRec(root, ciu, pr);
    }

    private LibraryNode insertRec(LibraryNode root, String ciu, String pr) {
        if (root == null) {
            root = new LibraryNode(ciu, pr);
            return root;
        }

        if (ciu.compareTo(root.ciu) < 0)
            root.left = insertRec(root.left, ciu, pr);
        else if (ciu.compareTo(root.ciu) > 0)
            root.right = insertRec(root.right, ciu, pr);

        return root;
    }

    public void inorder() {
        inorderRec(root);
    }

    private void inorderRec(LibraryNode root) {
        if (root != null) {
            inorderRec(root.left);
            System.out.println(root.ciu + " " + root.pr);
            inorderRec(root.right);
        }
    }

    public LibraryNode search(String ciu) {
        return searchRec(root, ciu);
    }

    private LibraryNode searchRec(LibraryNode root, String ciu) {
        if (root == null || root.ciu.equals(ciu))
            return root;

        if (ciu.compareTo(root.ciu) < 0)
            return searchRec(root.left, ciu);

        return searchRec(root.right, ciu);
    }

    public void update(String ciu, String newPr) {
        LibraryNode node = search(ciu);
        if (node != null) {
            node.pr = newPr;
        } else {
            System.out.println("CIU not found in the system.");
        }
    }
}

public class Program1_1 {
    public static void main(String[] args) throws FileNotFoundException {
        BinarySearchTree bst = new BinarySearchTree();

        // Read data from file and insert into BST
        String filename = args[0];
        try (Scanner scanner = new Scanner(new File(filename))) {
            while (scanner.hasNextLine()) {
                String[] data = scanner.nextLine().split(" ");
                bst.insert(data[0], data[1]);
            }
        }

        Scanner inputScanner = new Scanner(System.in);
        boolean running = true;
        while (running) {
            System.out.println("\n\n## Program 1.1 ## \nChoose an option:\n1. Search a member by CIU\n2. Change PR value on member by CIU\n3. List all members\n4. Exit");
            int choice = inputScanner.nextInt();
            inputScanner.nextLine(); // Consume newline
            switch (choice) {
                case 1:
                    System.out.println("Enter CIU to search:");
                    String ciu = inputScanner.nextLine();
                    LibraryNode result = bst.search(ciu);
                    if (result != null) {
                        System.out.println("CIU: " + result.ciu + ", PR: " + result.pr);
                    } else {
                        System.out.println("CIU not found.");
                    }
                    break;
                case 2:
                    System.out.println("Enter CIU to change PR:");
                    ciu = inputScanner.nextLine();
                    System.out.println("Enter new PR:");
                    String newPr = inputScanner.nextLine();
                    bst.update(ciu, newPr);
                    break;
                case 3:
                    bst.inorder();
                    break;
                case 4:
                    running = false;
                    break;
                default:
                    System.out.println("Invalid choice.");
            }
        }
        inputScanner.close();
    }
}
