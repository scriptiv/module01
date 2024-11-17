# 11.1
# File: zoo.py
def hours():
    print("Open 9-5 daily")

# Save the file and in the interactive interpreter:
# >>> import zoo
# >>> zoo.hours()

#11.2
#In the interactive interpreter:
#>>> import zoo as menagerie
#>>> menagerie.hours()

#16.8
from sqlalchemy import create_engine, Column, String, Integer, Table, MetaData, select, inspect  # Correct inspect import

#Connect to the database
engine = create_engine("sqlite:///books.db")
connection = engine.connect()

#Reflect or create the database schema
metadata = MetaData()

#Check if the 'book' table exists, and create it if necessary
inspector = inspect(engine)
if not inspector.has_table("book"):
    book = Table(
        'book', metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('title', String, nullable=False),
        Column('author', String, nullable=False),
        Column('year', Integer, nullable=False)
    )
    metadata.create_all(engine)  # Create the table

    #Insert sample data
    connection.execute(book.insert(), [
        {"title": "Book A", "author": "Author A", "year": 2000},
        {"title": "Book B", "author": "Author B", "year": 1999},
        {"title": "Book C", "author": "Author C", "year": 2021}
    ])
else:
    book = Table('book', metadata, autoload_with=engine)

#Query to select and print the 'title' column in alphabetical order
stmt = select(book.c.title).order_by(book.c.title)
results = connection.execute(stmt)

print("Book titles in alphabetical order:")
for row in results:
    print(row.title)

#Close the connection
connection.close()