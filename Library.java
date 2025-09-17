import java.util.ArrayList;
import java.util.Scanner;

class Book {
    private String title;
    private String author;

    Book(String title, String author) {
        this.title = title;
        this.author = author;
    }

    public String getTitle() {
        return title;
    }

    public String toString() {
        return "\"" + title + "\" by " + author;
    }
}

public class Library {
    private ArrayList<Book> books = new ArrayList<>();
    private Scanner sc = new Scanner(System.in);

    public void addBook() {
        System.out.print("Enter book title: ");
        String title = sc.nextLine();
        System.out.print("Enter author name: ");
        String author = sc.nextLine();
        books.add(new Book(title, author));
        System.out.println("Book added successfully!");
    }

    public void removeBook() {
        System.out.print("Enter title of book to remove: ");
        String title = sc.nextLine();
        boolean removed = books.removeIf(b -> b.getTitle().equalsIgnoreCase(title));
        if (removed) {
            System.out.println("Book removed successfully!");
        } else {
            System.out.println("Book not found.");
        }
    }

    public void displayBooks() {
        if (books.isEmpty()) {
            System.out.println("Library is empty.");
        } else {
            System.out.println("\nBooks in library:");
            for (Book b : books) {
                System.out.println("- " + b);
            }
        }
    }

    public void start() {
        while (true) {
            System.out.println("\n--- Library Menu ---");
            System.out.println("1. Add Book");
            System.out.println("2. Remove Book");
            System.out.println("3. Display Books");
            System.out.println("4. Exit");
            System.out.print("Choose an option: ");
            int choice = Integer.parseInt(sc.nextLine());

            switch (choice) {
                case 1 -> addBook();
                case 2 -> removeBook();
                case 3 -> displayBooks();
                case 4 -> {
                    System.out.println("Exiting Library. Goodbye!");
                    return;
                }
                default -> System.out.println("Invalid choice. Try again.");
            }
        }
    }

    public static void main(String[] args) {
        Library lib = new Library();
        lib.start();
    }
}
