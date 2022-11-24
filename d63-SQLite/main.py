from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, FloatField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import sqlite3

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'xxxyyyzzz'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection-sqlAlchemy.db'
db = SQLAlchemy(app)

class BookForm(FlaskForm):
    title=StringField('Title', validators=[ DataRequired() ])
    author=StringField('Autho', validators=[ DataRequired() ])
    rating=FloatField('Rating', validators=[ DataRequired() ])
    submit = SubmitField(label='Submit')

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Float(), nullable=False)
    def __repr__(self):
        return '<Book %r>' % self.title


@app.route('/')
def home():
    res = Book.query.all()
    all_books = [ {"id":book.id, "title":book.title, "author":book.author, "rating":book.rating } for book in res ]
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['GET','POST'])
def add():
    book_form=BookForm()
    if request.method=="GET":
        return render_template("add.html", form=book_form)
    elif book_form.validate_on_submit():
        new_book = {
            "title":book_form.title.data,
            "author":book_form.author.data,
            "rating":book_form.rating.data
        }
        new_book_obj = Book( **new_book )
        db.session.add(new_book_obj)
        db.session.commit()
        return redirect(url_for('home'))


@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    book_form = BookForm()
    if request.method == "GET":
        book = Book.query.filter_by(id=id).first()
        return render_template("edit.html", book = book)
    elif request.method == "POST":
        new_rating = float(dict(request.form)['rating'])
        print("request . data : ", new_rating)
        book_to_update = Book.query.filter_by(id=id).first()
        book_to_update.rating=new_rating
        db.session.commit()
        return redirect(url_for('home'))


@app.route("/delete/<int:id>", methods=['GET','POST'])
def delete(id):
    book_to_delete = Book.query.get(id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))    

if __name__ == "__main__":
    app.run(debug=True)

