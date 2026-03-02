from relationship_app.models import Author, Book, Library, Librarian

# Sample data setup (run this once to populate the database)
def setup_sample_data():
    # Create authors
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="J.R.R. Tolkien")

    # Create books
    book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author1)
    book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1)
    book3 = Book.objects.create(title="The Hobbit", author=author2)

    # Create library
    library = Library.objects.create(name="Central Library")
    library.books.add(book1, book2, book3)  # Add books to the many-to-many relationship

    # Create librarian
    Librarian.objects.create(name="Alice Johnson", library=library)

# Run setup if needed (comment out after first run)
setup_sample_data()

# Query 1: All books by a specific author
def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books:
        print(f"- {book.title}")

# Query 2: List all books in a library
def query_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"Books in {library_name}:")
    for book in books:
        print(f"- {book.title}")

# Query 3: Retrieve the librarian for a library
def query_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian for {library_name}: {librarian.name}")

# Execute the queries
query_books_by_author("J.K. Rowling")
query_books_in_library("Central Library")
query_librarian_for_library("Central Library")