from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select

DATABASE_URL = "sqlite:///books.db"
engine = create_engine(DATABASE_URL, future=True)
metadata = MetaData()

# Define the 'book' table schema
book = Table(
    'book', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String, nullable=False),
    Column('author', String, nullable=False),
    Column('year', Integer, nullable=False)
)

# Ensure the table exists
metadata.create_all(engine)

def list_all_tables():
    metadata.clear()  # Clear metadata before reflecting to avoid stale bindings
    metadata.reflect(bind=engine)
    tables = metadata.tables.keys()
    return tables

def fetch_all_rows(table_name):
    table = Table(table_name, metadata, autoload_with=engine)
    with engine.connect() as connection:
        stmt = select(table)
        result = connection.execute(stmt)
        rows = [row._mapping for row in result]  # Use `_mapping` for Row objects
        print(f"Fetched rows from {table_name}:", rows)  # Debugging output
        return rows

def insert_books():
    books_to_insert = [
        {"title": "The Outsider", "author": "Stephen King", "year": 2018},
        {"title": "If It Bleeds", "author": "Stephen King", "year": 2020},
        {"title": "The Finisher", "author": "David Baldacci", "year": 2014},
        {"title": "11/22/63", "author": "Stephen King", "year": 2011},
        {"title": "The Institute", "author": "Stephen King", "year": 2019}
    ]
    with engine.connect() as connection:
        # Clear existing rows and insert new data
        connection.execute(book.delete())
        connection.execute(book.insert(), books_to_insert)
        connection.commit()  # Force commit
        # Fetch immediately after insert for debugging
        result = connection.execute(select(book))
        rows = [row._mapping for row in result]
        print("Inserted rows:", rows)


if __name__ == "__main__":
    print(f"Using database at: {engine.url.database}")
    
    with engine.connect() as connection:
        # Insert data into the 'book' table
        print("Inserting books into the 'book' table...")
        insert_books()
        print("Insertion complete.")
        
        # Fetch rows immediately after insertion
        stmt = select(book)
        result = connection.execute(stmt)
        rows = [row._mapping for row in result]
        print("Rows immediately after insertion:", rows)

    # List all tables and fetch their rows
    tables = list_all_tables()
    if tables:
        print("Tables in the database:")
        for table in tables:
            print(f"\nTable: {table}")
            rows = fetch_all_rows(table)
            if rows:
                print("Rows:")
                for row in rows:
                    print(row)
            else:
                print("No rows found in this table.")
    else:
        print("No tables found in the database.")
