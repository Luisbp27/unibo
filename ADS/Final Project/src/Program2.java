import java.io.*;
import java.util.*;

/**
 * This class represents an element in the dictionary.
 * It contains a key, info, and hs value.
 * The hs value is used to determine which list in the hash table the element is stored in.
 * The key is used to search for elements in the dictionary.
 * The info value is used to store additional information about the element.
 */
class DictionaryElement {
    String key;
    char info;
    int hs;

    /**
     * Constructor for DictionaryElement
     *
     * @param key Key value
     * @param info Info value
     * @param hs hs value in range [0, K]
     */
    public DictionaryElement(String key, char info, int hs) {
        this.key = key;
        this.info = info;
        this.hs = hs;
    }

    /**
     * Returns a string representation of the DictionaryElement
     *
     * @return String representation of the DictionaryElement
     */
    @Override
    public String toString() {
        return "<" + key + ", " + info + ", " + hs + ">";
    }
}

/**
 * This class implements a dictionary using a hash table.
 * The hash table uses separate chaining to resolve collisions.
 * The hash table is implemented as an array of linked lists.
 * The hash table size is set to K, where K is the number of
 * different hs values in the dictionary.
 */
public class Program2 {
    private static HashMap<Integer, List<DictionaryElement>> dictionary;

    public static void main(String[] args) throws FileNotFoundException {
        String filename = args[0];
        loadDictionary(filename);

        Scanner scanner = new Scanner(System.in);
        boolean running = true;
        while (running) {
            System.out.println("\n\n## Program 2 ##\nChoose an option:\n1. Search by key\n2. Search by hs\n3. Exit");

            // Get user choice
            int choice = scanner.nextInt();
            scanner.nextLine();
            switch (choice) {
                case 1: // Search by key
                    searchByKey(scanner);
                    break;
                case 2: // Search by hs
                    searchByHs(scanner);
                    break;
                case 3: // Exit
                    running = false;
                    break;
                default:
                    System.out.println("Invalid choice.");
            }
        }
        scanner.close();
    }

    /**
     * Loads the dictionary from the given file
     *
     * @param filename Name of the file to load
     * @throws FileNotFoundException If the file is not found
     */
    private static void loadDictionary(String filename) throws FileNotFoundException {
        try (Scanner fileScanner = new Scanner(new File(filename))) {
            // Read M, K from file and initialize dictionary with K value
            int M = fileScanner.nextInt();
            int K = fileScanner.nextInt();
            dictionary = new HashMap<>(K);

            // Read each line and add to dictionary
            for (int i = 0; i < M; i++) {
                String key = fileScanner.next();
                char info = fileScanner.next().charAt(0);
                int hs = fileScanner.nextInt();

                dictionary.putIfAbsent(hs, new ArrayList<>());
                dictionary.get(hs).add(new DictionaryElement(key, info, hs));
            }
        }
    }

    /**
     * Searches the dictionary for the given key
     *
     * @param scanner Scanner to get user input
     */
    private static void searchByKey(Scanner scanner) {
        // Get key from user
        System.out.println("Enter key to search:");
        String key = scanner.nextLine();

        // Search dictionary for key in each list
        for (List<DictionaryElement> elements : dictionary.values()) {
            for (DictionaryElement element : elements) {
                // If key is found, print element and return
                if (element.key.equals(key)) {
                    System.out.println("Element found: " + element);
                    return;
                }
            }
        }

        System.out.println("Element not found.");
    }

    /**
     * Searches the dictionary for the given hs value
     *
     * @param scanner Scanner to get user input
     */
    private static void searchByHs(Scanner scanner) {
        // Get hs value from user
        System.out.println("Enter hs value to search:");
        int hs = scanner.nextInt();

        // Search dictionary for elements with the given hs value
        if (dictionary.containsKey(hs)) {
            // Get elements with the given hs value
            List<DictionaryElement> elements = dictionary.get(hs);
            System.out.println("Elements with hs " + hs + ":");

            // Print each element
            for (DictionaryElement element : elements) {
                System.out.println(element);
            }
        } else {
            System.out.println("No elements found with hs " + hs);
        }
    }
}
