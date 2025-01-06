from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flashing messages

# Database connection
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='cbavithran02102003',
            database='lib_package'
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Route to add new books
@app.route('/add-book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        # Fetching data from the form
        title = request.form['title']
        author = request.form['author']
        isbn = request.form['isbn']
        pub_year = request.form['pub_year']
        category = request.form['category']
        
        conn = get_db_connection()
        if conn is None:
            flash('Database connection failed', 'danger')
            return redirect(url_for('add_book'))

        try:
            cursor = conn.cursor()
            # Insert the book into the appropriate category table
            if category == 'Department Books':
                cursor.execute('INSERT INTO departmentbooks (Title, Author, ISBN, PublicationYear) VALUES (%s, %s, %s, %s)', 
                               (title, author, isbn, pub_year))
            elif category == 'Novels':
                cursor.execute('INSERT INTO novels (Title, Author, ISBN, PublicationYear) VALUES (%s, %s, %s, %s)', 
                               (title, author, isbn, pub_year))
            elif category == 'GATE Books':
                cursor.execute('INSERT INTO gatebooks (Title, Author, ISBN, PublicationYear) VALUES (%s, %s, %s, %s)', 
                               (title, author, isbn, pub_year))
            elif category == 'Story Books':
                cursor.execute('INSERT INTO storybooks (Title, Author, ISBN, PublicationYear) VALUES (%s, %s, %s, %s)', 
                               (title, author, isbn, pub_year))
            elif category == 'Research Books':
                cursor.execute('INSERT INTO researchbooks (Title, Author, ISBN, PublicationYear) VALUES (%s, %s, %s, %s)', 
                               (title, author, isbn, pub_year))

            conn.commit()
            flash(f'Book "{title}" added successfully!', 'success')
        except mysql.connector.Error as err:
            flash(f'Failed to add book: {err}', 'danger')
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('add_book'))

    return render_template('add_book.html')

# Existing book listing routes
@app.route('/department-books')
def department_books():
    conn = get_db_connection()
    if conn is None:
        return "Database connection failed", 500
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM departmentbooks')
        books = cursor.fetchall()
    except mysql.connector.Error as err:
        books = []
    finally:
        cursor.close()
        conn.close()
    return render_template('department_books.html', books=books)

@app.route('/novels')
def novels():
    conn = get_db_connection()
    if conn is None:
        return "Database connection failed", 500
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM novels')
        books = cursor.fetchall()
    except mysql.connector.Error as err:
        books = []
    finally:
        cursor.close()
        conn.close()
    return render_template('novels.html', books=books)

@app.route('/gate-books')
def gate_books():
    conn = get_db_connection()
    if conn is None:
        return "Database connection failed", 500
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM gatebooks')
        books = cursor.fetchall()
    except mysql.connector.Error as err:
        books = []
    finally:
        cursor.close()
        conn.close()
    return render_template('gate_books.html', books=books)

@app.route('/story-books')
def story_books():
    conn = get_db_connection()
    if conn is None:
        return "Database connection failed", 500
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM storybooks')
        books = cursor.fetchall()
    except mysql.connector.Error as err:
        books = []
    finally:
        cursor.close()
        conn.close()
    return render_template('story_books.html', books=books)

@app.route('/research-books')
def research_books():
    conn = get_db_connection()
    if conn is None:
        return "Database connection failed", 500
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM researchbooks')
        books = cursor.fetchall()
    except mysql.connector.Error as err:
        books = []
    finally:
        cursor.close()
        conn.close()
    return render_template('research_books.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
