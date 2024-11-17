from flask import Flask, jsonify
from sqlalchemy import create_engine, Column, String, Integer, Table, MetaData, select, inspect
import os

app = Flask(__name__)

#Initialize SQLAlchemy database with consistent settings
DATABASE_URL = "sqlite:///books.db"
engine = create_engine(DATABASE_URL, future=True)  # Use `future=True` for consistent transaction handling
metadata = MetaData()

#Log the absolute path of the database for debugging
print(f"Using database at: {os.path.abspath(engine.url.database)}")

#Define the 'book' table schema
book = Table(
    'book', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String, nullable=False),
    Column('author', String, nullable=False),
    Column('year', Integer, nullable=False)
)

#Debugging Logs: Check if the table exists and create it if necessary
inspector = inspect(engine)
if not inspector.has_table("book"):
    print("Creating 'book' table and inserting data...")
    metadata.create_all(engine)  #Create the table
    with engine.connect() as connection:
        with connection.begin():  #Explicitly handle transaction
            connection.execute(book.insert(), [
                {"title": "The Outsider", "author": "Stephen King", "year": 2018},
                {"title": "If It Bleeds", "author": "Stephen King", "year": 2020},
                {"title": "The Finisher", "author": "David Baldacci", "year": 2014},
                {"title": "11/22/63", "author": "Stephen King", "year": 2011},
                {"title": "The Institute", "author": "Stephen King", "year": 2019}
            ])
    print("Data successfully inserted.")
else:
    print("'book' table already exists.")

@app.route("/")
def home():
    return "Welcome to the Books API! Use /books to get the list of book titles."

@app.route("/books", methods=["GET"])
def get_books():
    print("Fetching book titles...")
    stmt = select(book.c.title).order_by(book.c.title)
    try:
        with engine.connect() as connection:
            results = connection.execute(stmt)
            books = [row[0] for row in results]
            print(f"Fetched books: {books}")
            return jsonify(books)
    except Exception as e:
        print(f"Error in /books route: {e}")
        return jsonify({"error": "Failed to fetch books"}), 500

if __name__ == "__main__":
    app.run(debug=True)
