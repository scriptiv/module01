# 16.8
# Use SQLAlchemy to connect to the SQLite database books.db
from sqlalchemy import create_engine, MetaData, Table, select

# Connect to the books.db SQLite database
engine = create_engine('sqlite:///books.db')
connection = engine.connect()

# Reflect the database schema
metadata = MetaData()
book_table = Table('book', metadata, autoload_with=engine)

# Select and print the title column in alphabetical order
query = select([book_table.c.title]).order_by(book_table.c.title)
result = connection.execute(query)

print("Titles in alphabetical order:")
for row in result:
    print(row['title'])
