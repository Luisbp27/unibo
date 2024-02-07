import java.io.*;
import java.util.Scanner;

/**
 * This class represents a node in the binary search tree.
 * Each node contains a CIU and PR value, and pointers to the left and right child nodes.
 * The CIU is used as the key for the binary search tree.
 */
class LibraryNode {
    String ciu;
    String pr;
    LibraryNode left, right;

    /**
     * Constructor for LibraryNode
     *
     * @param ciu CIU value
     * @param pr PR value
     */
    public LibraryNode(String ciu, String pr) {
        this.ciu = ciu;
        this.pr = pr;
        this.left = null;
        this.right = null;
    }
}

/**
 * This class represents a binary search tree.
 * It contains a root node, and methods to insert, search, and update nodes.
 */
class BinarySearchTree {
    private LibraryNode root;

    /**
     * Constructor for BinarySearchTree
     * Initializes root node to null
     *
     */
    public BinarySearchTree() {
        root = null;
    }

    /**
     * Inserts a new node into the binary search tree
     *
     * @param ciu CIU value
     * @param pr PR value
     */
    public void insert(String ciu, String pr) {
        root = insertRec(root, ciu, pr);
    }

    /**
     * Recursive helper function for insert()
     *
     * @param root Root node of the tree
     * @param ciu CIU value
     * @param pr PR value
     * @return Root node of the tree
     */
    private LibraryNode insertRec(LibraryNode root, String ciu, String pr) {

        // If the tree is empty, return a new node
        if (root == null) {
            root = new LibraryNode(ciu, pr);
            return root;
        }

        // Otherwise, recur down the tree
        int comparison = ciu.compareTo(root.ciu);
        if (comparison < 0)
            root.left = insertRec(root.left, ciu, pr);
        else if (comparison > 0)
            root.right = insertRec(root.right, ciu, pr);

        return root;
    }

    /**
     * Prints the contents of the binary search tree in order
     *
     */
    public void inorder() {
        inorderRec(root);
    }

    /**
     * Recursive helper function for inorder()
     *
     * @param root Root node of the tree
     */
    private void inorderRec(LibraryNode root) {

        // If the tree is empty, return
        if (root != null) {
            inorderRec(root.left);
            System.out.println(root.ciu + " " + root.pr);
            inorderRec(root.right);
        }
    }

    /**
     * Searches for a node with the given CIU value
     *
     * @param ciu CIU value
     * @return Node with the given CIU value, or null if not found
     */
    public LibraryNode search(String ciu) {
        return searchRec(root, ciu);
    }

    /**
     * Recursive helper function for search()
     *
     * @param root Root node of the tree
     * @param ciu CIU value
     * @return Node with the given CIU value, or null if not found
     */
    private LibraryNode searchRec(LibraryNode root, String ciu) {

        // If the tree is empty or the root node is the node we're looking for, return the root node
        if (root == null || root.ciu.equals(ciu))
            return root;

        // Otherwise, recur down the tree
        if (ciu.compareTo(root.ciu) < 0)
            return searchRec(root.left, ciu);

        return searchRec(root.right, ciu);
    }

    /**
     * Updates the PR value of a node with the given CIU value
     *
     * @param ciu CIU value
     * @param newPr New PR value
     */
    public void update(String ciu, String newPr) {
        LibraryNode node = search(ciu);

        // If the node is found, update the PR value
        if (node != null) {
            node.pr = newPr;
        } else {
            System.out.println("CIU not found in the system.");
        }
    }
}

/**
 * This class contains the main method for Program 1.1
 * It reads data from a file and inserts it into a binary search tree.
 * It then allows the user to search for a node, update a node, or list all nodes.
 */
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

        // Scan for user input
        Scanner inputScanner = new Scanner(System.in);
        boolean running = true;

        while (running) {
            System.out.println("\n\n## Program 1.1 ## \nChoose an option:\n1. Search a member by CIU\n2. Change PR value on member by CIU\n3. List all members\n4. Exit");

            // Handle the choice of the user
            int choice = inputScanner.nextInt();
            inputScanner.nextLine();
            switch (choice) {
                case 1: // Search
                    // Take CIU input from user
                    System.out.println("Enter CIU to search:");
                    String ciu = inputScanner.nextLine();

                    // Search for the CIU in the BST
                    LibraryNode result = bst.search(ciu);

                    // Print result if found, otherwise print error message
                    System.out.println(result != null ? "CIU: " + result.ciu + ", PR: " + result.pr : "CIU not found.");

                    break;
                case 2: // Update
                    // Take CIU and new PR input from user
                    System.out.println("Enter CIU to change PR:");
                    ciu = inputScanner.nextLine();
                    System.out.println("Enter new PR:");
                    String newPr = inputScanner.nextLine();

                    // Update PR value
                    bst.update(ciu, newPr);

                    break;
                case 3: // List all
                    // Print all nodes in the BST
                    bst.inorder();

                    break;
                case 4: // Exit
                    running = false;

                    break;
                default:
                    System.out.println("Invalid choice.");
            }
        }
        inputScanner.close();
    }
}
