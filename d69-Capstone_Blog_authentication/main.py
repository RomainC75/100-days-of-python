from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user, logout_user
from forms import CreatePostForm
from flask_gravatar import Gravatar
from forms import CreatePostForm, UserRegisterForm, UserLoginForm, CommentForm
from datetime import datetime
from utils import admin_only, row2dict



app = Flask(__name__)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

login_manager = LoginManager()
login_manager.init_app(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

gravatar = Gravatar(app,
                size=100,
                rating='g',
                default='retro',
                force_default=False,
                force_lower=False,
                use_ssl=False,
                base_url=None)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

##CONFIGURE TABLES
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="author")

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = relationship( "User", back_populates = "posts" )
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    comments = relationship("Comment", back_populates="post")
    

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = relationship( "User", back_populates = "comments" )

    post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    post = relationship( "BlogPost", back_populates = "comments" )

    date = db.Column(db.String(250), nullable=False)
    comment = db.Column(db.String(500), unique=True, nullable=False)
# db.create_all()


@app.route('/')
def get_all_posts():
    is_authenticated = current_user.is_authenticated
    try:
        is_admin = True if current_user.id==1 else False
    except:
        is_admin = False
    
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts, is_logged_in=is_authenticated, is_admin=is_admin)


@app.route('/register', methods=['GET','POST'])
def register():
    form = UserRegisterForm()
    if form.validate_on_submit():
        found_user = User.query.filter_by(email=request.form.get("email")).first()
        if found_user:
            flash("email already used !", "text-danger")
            return redirect(url_for("login"))

        new_user = User(
            name=request.form.get("name"),
            email=request.form.get("email"),
            password = generate_password_hash(request.form.get("password"),method="pbkdf2:sha256", salt_length=8 )
        )
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('get_all_posts'))
    return render_template("register.html", form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    form = UserLoginForm()
    error = None
    if form.validate_on_submit():
        email=request.form.get("email")
        password=request.form.get("password")
        found_user = User.query.filter_by(email=email).first()
        if not found_user:
            # error="User doesn't exist"
            flash("user doesn't exist !", "text-danger")
        elif check_password_hash(pwhash=found_user.password, password=password):
            login_user(found_user)
            return redirect(url_for("get_all_posts"))
        else:
            # error="wrong password"
            flash("wrong password !", "text-danger")
    return render_template("login.html", form=form, error=error)


@app.route('/logout')
def logout():
    logout_user()
    print("==>log out ! ")
    return redirect(url_for('get_all_posts'))


@app.route("/post/<int:post_id>", methods=['GET','POST'])
def show_post(post_id):
    commentForm = CommentForm()
    if commentForm.validate_on_submit():
        print("==>comment Forml ", commentForm.body.data)
        comment = Comment(
            author_id=current_user.id,
            comment=commentForm.body.data,
            post_id=post_id,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(comment)
        db.session.commit()


    user = login_user if current_user.is_authenticated else None
    try:
        is_admin = True if current_user.id==1 else False
    except:
        is_admin = False
    requested_post = BlogPost.query.get(post_id)
    comments = [ row2dict(comment) for comment in Comment.query.filter(post_id==post_id).all()]
    print("comments : ", comments)
    print("user : ", user)
    #if not connected 
    #>flash
    return render_template("post.html", post = requested_post, is_admin = is_admin, user = user, commentForm=commentForm, comments=comments, gravatar=gravatar)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/new-post", methods=['GET','POST'])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y"),
            author_id=current_user.id
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>")
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form)


@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
