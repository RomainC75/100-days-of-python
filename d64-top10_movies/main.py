from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.fields import FloatField
from wtforms.validators import DataRequired, NumberRange
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
api_key="c065bd6a4de63d934a56265a6b8d6409"
api_url="https://api.themoviedb.org/3/search/movie"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-collection-sqlAlchemy.db'
db = SQLAlchemy(app)

class EditMovieForm(FlaskForm):
    ranking = StringField('Rankin', validators=[ DataRequired() ])
    review = StringField('Review', validators=[ DataRequired() ])
    submit = SubmitField(label='Submit')

class AddMovieForm(FlaskForm):
    title = StringField('Title', validators=[ DataRequired() ])
    submit = SubmitField(label='Submit')

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.Float(), nullable=False)
    ranking = db.Column(db.Integer(), nullable=False)
    review = db.Column(db.String(80), nullable=False)
    img_url = db.Column(db.String(80), nullable=False)
    def __repr__(self):
        return '<Book %r>' % self.title

@app.route("/")
def home():
    res = Movie.query.all()
    all_movies = [ {"id":movie.id, "title":movie.title, "year":movie.year, "description":movie.description, "rating":movie.rating, "ranking":movie.ranking, "review":movie.review, "img_url":movie.img_url } for movie in res ]
    print("all_movies : ", all_movies)
    return render_template("index.html", movies=sorted(all_movies, key=lambda movie:movie['rating']))

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    form = EditMovieForm()
    found_movie = Movie.query.filter_by(id=id).first()
    if request.method=="GET":
        return render_template("edit.html",movie=found_movie, form=form)
    elif form.validate_on_submit():
        ranking = form.ranking.data
        review = form.review.data
        found_movie.ranking=ranking
        found_movie.review=review
        db.session.commit()
        return redirect("/")


@app.route("/delete/<int:id>")
def delete(id):
    if request.method=="GET":
        found_movie = Movie.query.filter_by(id=id).first()
        db.session.delete(found_movie)
        db.session.commit()
        return redirect(url_for('home'))


@app.route("/add", methods=['GET','POST'])
def add():
    add_form = AddMovieForm()
    if request.method=="GET":
        return render_template("add.html", form=add_form)
    elif add_form.validate_on_submit():
        params={
            "api_key":api_key,
            "language":"en-US",
            "query":add_form.title.data,
            "page":1,
            "include_adult":"false"
        } 
        raw_ans = requests.get(api_url, params=params)
        if len(raw_ans.json()['results'])==0:
            return f"'{add_form.title.data}' not found :-("
        ans = raw_ans.json()['results'][0]
        new_movie = Movie(
            title = ans['original_title'],
            year=ans['release_date'][:4],
            img_url=f"https://image.tmdb.org/t/p/original/{ ans['poster_path'] }",
            description = ans['overview'],
            rating = ans['vote_average'],
            ranking = 0,
            review = " ... "
        )
        db.session.add(new_movie)
        db.session.commit()
        print(new_movie)
        return redirect(url_for('home'))
    

if __name__ == '__main__':
    app.run(debug=True)

    # new_movie = Movie(
    #     title="Phone Booth",
    #     year=2002,
    #     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    #     rating=7.3,
    #     ranking=10,
    #     review="My favourite character was the caller.",
    #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    # )
    # db.session.add(new_movie)
    # db.session.commit()