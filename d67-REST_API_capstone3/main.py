from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from utils import row2dict
from datetime import datetime

## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = StringField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post", )


@app.route('/')
def get_all_posts():
    posts = [ row2dict(post) for post in BlogPost.query.all() ]

    print("posts : " , posts)
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:id>")
def show_post(id):
    requested_post = BlogPost.query.get(id)
    readable_post = row2dict(requested_post)
    print("======>", readable_post)
    return render_template("post.html", post=readable_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/make-post", methods=['GET','POST'])
def make_post():
    form=CreatePostForm()
    if request.method=="GET":
        return render_template("make-post.html", form=form)
    elif form.validate_on_submit():
        try:
            print("form : ", form.title.data)
            new_post=BlogPost(
                title = form.title.data,
                subtitle = form.subtitle.data,
                date = datetime.now().strftime("%B %d, %y"),
                body = form.body.data,
                author = form.author.data,
                img_url = form.img_url.data
            )
            db.session.add(new_post)
            db.session.commit()
            return redirect("/")
        except:
            return jsonify({"error" : 'oops, something went wrong'})

@app.route("/edit-post/", methods=['GET','POST'])
def edit_post():
    id = request.args.get("post_id")
    post = BlogPost.query.get(id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
        )
    if request.method=="GET":
        return render_template("make-post.html", form=edit_form, edit=True)
    elif edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data   
        db.session.commit()
        return redirect(url_for("show_post",id=post.id))

@app.route("/delete/<int:id>")
def delete_post(id):
    post = BlogPost.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)