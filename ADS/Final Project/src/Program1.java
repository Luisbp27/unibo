import java.util.*;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

class Library {
    String name, city, link, code;
    int year;

    public Library(String name, String city, int year, String link, String code) {
        this.name = name;
        this.city = city;
        this.year = year;
        this.link = link;
        this.code = code;
    }

    @Override
    public String toString() {
        return name + " " + city + " " + year + " " + link + " " + code;
    }
}

public class Program1 {

    public static final int ALPHABET_SIZE = 26;
    @SuppressWarnings("unchecked")
    private static List<Library>[] libraries = new List[ALPHABET_SIZE];

    public static void main(String[] args) {
        // Initialize the array of lists
        for (int i = 0; i < ALPHABET_SIZE; i++) {
            libraries[i] = new ArrayList<>();
        }

        // Load the libraries from the file
        loadLibraries(args[0]);

        Scanner scanner = new Scanner(System.in);
        boolean running = true;
        while (running) {
            System.out.println(
                    "\n\n## Program 1 ##\nChoose an option:\n1. Search a member by name\n2. List all members\n3. List members by city\n4. Delete a member\n5. Insert a member\n6. Exit");
            int choice = scanner.nextInt();
            switch (choice) {
                case 1: // Search
                    scanner = new Scanner(System.in);
                    System.out.println("Enter library name to search:");
                    String name = scanner.nextLine();
                    int index = Character.toUpperCase(name.charAt(0)) - 'A';
                    for (Library lib : libraries[index]) {
                        if (lib.name.equalsIgnoreCase(name)) {
                            System.out.println(lib);
                            return;
                        }
                    }
                    System.out.println("Library not found.");
                    break;
                case 2: // List all
                    for (List<Library> list : libraries) {
                        for (Library lib : list) {
                            System.out.println(lib);
                        }
                    }
                    break;
                case 3: // List by city
                    scanner = new Scanner(System.in);
                    System.out.println("Enter city:");
                    String city = scanner.nextLine();
                    for (List<Library> list : libraries) {
                        for (Library lib : list) {
                            if (lib.city.equalsIgnoreCase(city)) {
                                System.out.println(lib);
                            }
                        }
                    }

                    break;
                case 4: // Delete
                    scanner = new Scanner(System.in);
                    System.out.println("Enter library name to delete:");
                    name = scanner.nextLine();
                    index = Character.toUpperCase(name.charAt(0)) - 'A';
                    libraries[index].removeIf(lib -> lib.name.equalsIgnoreCase(name));

                    break;
                case 5: // Insert
                    scanner = new Scanner(System.in);
                    System.out.println("Enter library details (name city year link code):");
                    String[] details = scanner.nextLine().split(" ");
                    name = details[0];
                    city = details[1];
                    int year = Integer.parseInt(details[2]);
                    String link = details[3];
                    String code = details[4];

                    Library newLib = new Library(name, city, year, link, code);
                    index = Character.toUpperCase(name.charAt(0)) - 'A';
                    libraries[index].add(newLib);

                    libraries[index].sort(Comparator.comparing((Library l) -> l.name).thenComparing((Library l) -> l.code));

                    break;
                case 6: // Exit
                    running = false;
                    break;
                default:
                    System.out.println("Invalid choice");
            }
        }
        scanner.close();
    }

    private static void loadLibraries(String filename) {
        try (BufferedReader br = new BufferedReader(new FileReader(filename + ".txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] tokens = line.split(" ");
                String name = tokens[0];
                String city = tokens[1];
                int year = Integer.parseInt(tokens[2]);
                String link = tokens[3];
                String code = tokens[4];

                int index = Character.toUpperCase(name.charAt(0)) - 'A';
                libraries[index].add(new Library(name, city, year, link, code));

                // Sorting
                libraries[index].sort(Comparator.comparing((Library l) -> l.name).thenComparing((Library l) -> l.code));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}