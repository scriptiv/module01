from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

#Set up Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False, unique=True)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"<Book {self.book_name}>"

#Initialize database
with app.app_context():
    db.create_all()

#Get all books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    all_books = []
    for book in books:
        book_info = {
            'id': book.id,
            'book_name': book.book_name,
            'author': book.author,
            'publisher': book.publisher
        }
        all_books.append(book_info)
    return jsonify({'books': all_books})

#Get one book
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify({
        'id': book.id,
        'book_name': book.book_name,
        'author': book.author,
        'publisher': book.publisher
    })

#Add a book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(
        book_name=data['book_name'],
        author=data['author'],
        publisher=data.get('publisher')
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'New book added successfully!'})

#Update a book
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.get_json()
    book.book_name = data.get('book_name', book.book_name)
    book.author = data.get('author', book.author)
    book.publisher = data.get('publisher', book.publisher)
    db.session.commit()
    return jsonify({'message': 'Book updated successfully!'})

#Delete a book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully!'})

#Run the app
if __name__ == '__main__':
    app.run(debug=True)