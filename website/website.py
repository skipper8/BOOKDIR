from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

#@app.route('/library')
#def library():
    #return render_template('library.html')

#@app.route('/wishlist')
#def wishlist():
    #return render_template('wishlist.html')
