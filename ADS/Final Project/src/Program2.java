import java.io.*;
import java.util.*;

class DictionaryElement {
    String key;
    char info;
    int hs;

    public DictionaryElement(String key, char info, int hs) {
        this.key = key;
        this.info = info;
        this.hs = hs;
    }

    @Override
    public String toString() {
        return "<" + key + ", " + info + ", " + hs + ">";
    }
}

public class Program2 {
    private static HashMap<Integer, List<DictionaryElement>> dictionary;

    public static void main(String[] args) throws FileNotFoundException {
        String filename = args[0];
        loadDictionary(filename);

        Scanner scanner = new Scanner(System.in);
        boolean running = true;
        while (running) {
            System.out.println("Choose an option:\n1. Search by key\n2. Search by hs\n3. Exit");
            int choice = scanner.nextInt();
            scanner.nextLine();  // Consume newline left-over
            switch (choice) {
                case 1:
                    searchByKey(scanner);
                    break;
                case 2:
                    searchByHs(scanner);
                    break;
                case 3:
                    running = false;
                    break;
                default:
                    System.out.println("Invalid choice.");
            }
        }
        scanner.close();
    }

    private static void loadDictionary(String filename) throws FileNotFoundException {
        dictionary = new HashMap<>();
        try (Scanner fileScanner = new Scanner(new File(filename))) {
            int M = fileScanner.nextInt();
            for (int i = 0; i < M; i++) {
                String key = fileScanner.next();
                char info = fileScanner.next().charAt(0);
                int hs = fileScanner.nextInt();

                dictionary.putIfAbsent(hs, new ArrayList<>());
                dictionary.get(hs).add(new DictionaryElement(key, info, hs));
            }
        }
    }

    private static void searchByKey(Scanner scanner) {
        System.out.println("Enter key to search:");
        String key = scanner.nextLine();
        for (List<DictionaryElement> elements : dictionary.values()) {
            for (DictionaryElement element : elements) {
                if (element.key.equals(key)) {
                    System.out.println("Element found: " + element);
                    return;
                }
            }
        }
        System.out.println("Element not found.");
    }

    private static void searchByHs(Scanner scanner) {
        System.out.println("Enter hs value to search:");
        int hs = scanner.nextInt();
        if (dictionary.containsKey(hs)) {
            List<DictionaryElement> elements = dictionary.get(hs);
            System.out.println("Elements with hs " + hs + ":");
            for (DictionaryElement element : elements) {
                System.out.println(element);
            }
        } else {
            System.out.println("No elements found with hs " + hs);
        }
    }
}
