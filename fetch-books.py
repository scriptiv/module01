from sqlalchemy import create_engine, Table, MetaData, select

DATABASE_URL = "sqlite:///books.db"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Reflect the 'book' table
book = Table('book', metadata, autoload_with=engine)

def fetch_all_books():
    with engine.connect() as connection:
        stmt = select(book)
        result = connection.execute(stmt)
        books = [dict(row) for row in result]
        return books

if __name__ == "__main__":
    books = fetch_all_books()
    if books:
        print("Books in the database:")
        for book in books:
            print(book)
    else:
        print("No books found in the database.")
