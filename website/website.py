from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/library')
def library():
    return render_template('library.html')

@app.route('/library/books')
def books():
    return render_template('books.html')

@app.route('/library/music')
def music():
    return render_template('music.html')

@app.route('/library/games')
def games():
    return render_template('games.html')

@app.route('/library/movies')
def movies():
    return render_template('movies.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/papers')
def papers():
    return render_template('papers.html')
