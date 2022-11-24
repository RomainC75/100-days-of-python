from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import sqlite3

db = sqlite3.connect("books-collection.db")
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'xxxyyyzzz'

class BookForm(FlaskForm):
    title=StringField('Title', validators=[ DataRequired() ])
    author=StringField('Autho', validators=[ DataRequired() ])
    rating=StringField('Rating', validators=[ DataRequired() ])
    submit = SubmitField(label='Submit')

all_books = []

@app.route('/')
def home():
    db = sqlite3.connect("books-collection.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM books" )
    res = cursor.fetchall()
    all_books = [ {"title":book[1], "author":book[2], "rating":book[3] } for book in res ]
    return render_template("index.html", books=all_books)

@app.route("/add", methods=['GET','POST'])
def add():
    book_form=BookForm()
    if request.method=="GET":
        return render_template("add.html", form=book_form)
    elif book_form.validate_on_submit():
        db = sqlite3.connect("books-collection.db")
        cursor = db.cursor()
        cursor.execute("INSERT INTO books (`title`,`author`,`rating`) VALUES (?, ?, ?)",(book_form.title.data, book_form.author.data, book_form.rating.data) )
        db.commit()
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

