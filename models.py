from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the MySQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://your_username:your_password@localhost/your_database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Department Books Model
class DepartmentBook(db.Model):
    __tablename__ = 'DepartmentBooks'
    BookID = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(255), nullable=False)
    Author = db.Column(db.String(255), nullable=False)
    ISBN = db.Column(db.String(13), unique=True, nullable=False)
    PublicationYear = db.Column(db.Integer)
    Department = db.Column(db.String(100))
    CourseCode = db.Column(db.String(50))
    Availability = db.Column(db.Boolean, default=True)

# Novels Model
class Novel(db.Model):
    __tablename__ = 'Novels'
    BookID = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(255), nullable=False)
    Author = db.Column(db.String(255), nullable=False)
    ISBN = db.Column(db.String(13), unique=True, nullable=False)
    PublicationYear = db.Column(db.Integer)
    Availability = db.Column(db.Boolean, default=True)

# GATE Books Model
class GATEBook(db.Model):
    __tablename__ = 'GATEBooks'
    BookID = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(255), nullable=False)
    Author = db.Column(db.String(255), nullable=False)
    ISBN = db.Column(db.String(13), unique=True, nullable=False)
    PublicationYear = db.Column(db.Integer)
    Availability = db.Column(db.Boolean, default=True)

# Story Books Model
class StoryBook(db.Model):
    __tablename__ = 'StoryBooks'
    BookID = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(255), nullable=False)
    Author = db.Column(db.String(255), nullable=False)
    ISBN = db.Column(db.String(13), unique=True, nullable=False)
    PublicationYear = db.Column(db.Integer)
    Availability = db.Column(db.Boolean, default=True)

@app.route('/')
def index():
    return "Welcome to the Book Database!"

@app.route('/department-books')
def department_books():
    books = DepartmentBook.query.all()
    return render_template('department_books.html', books=books)

@app.route('/novels')
def novels():
    books = Novel.query.all()
    return render_template('novels.html', books=books)

@app.route('/gate-books')
def gate_books():
    books = GATEBook.query.all()
    return render_template('gate_books.html', books=books)

@app.route('/story-books')
def story_books():
    books = StoryBook.query.all()
    return render_template('story_books.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
