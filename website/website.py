from flask import Flask, render_template, request
from access import access 

app = Flask(__name__)
db = Access()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/library')
def library():
    return render_template('library.html')

@app.route('/library/books')
def books():
    info = db.gather_all(books)
    return render_template('books.html', info)

@app.route('/library/books/title')
def books_title():
    return render_template('title_books.html')

@app.route('/library/books/author')
def author_books():
    return render_template('author_books.html')

@app.route('/library/books/isbn')
def ibsn():
    return render_template('IBSN.html')

@app.route('/library/music')
def music():
    return render_template('music.html')

@app.route('/library/games')
def games():
    return render_template('games.html')

@app.route('/library/movies')
def movies():
    return render_template('movies.html')

@app.route('/library/search')
def search():
    return render_template('search.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/papers')
def papers():
    return render_template('papers.html')
