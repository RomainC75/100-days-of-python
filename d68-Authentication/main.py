from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = "static/files"

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))



#Line below only required once, when creating DB. 
# db.create_all()
@login_manager.user_loader
def load_user(user_id):
    print("===>insidfe")
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method=='GET':
        return render_template("register.html")
    elif request.method=="POST":
        user = User(
            name=request.form.get("name"),
            email=request.form.get("email"),
            password=generate_password_hash(request.form.get("password"),method="pbkdf2:sha256", salt_length=8 )
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("secrets"))


@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")
        found_user = User.query.filter_by(email=email).first()
        if not found_user:
            error="User doesn't exist "
        elif check_password_hash(pwhash=found_user.password, password=password):
            login_user(found_user)
            return redirect(url_for("secrets"))
        else:
            error="Password doesn't match"
        # flash("successfuly logged in")
        # return redirect(url_for("home"))
        
    return render_template("login.html", error=error)


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    pass

@app.route('/download')
@login_required
def download():
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               "cheat_sheet.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
