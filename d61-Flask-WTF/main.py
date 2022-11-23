from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Email
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap

class LoginForm(FlaskForm):
    # email = StringField('email', [validators.Length(min=6, max=35)])
    email = StringField(label='email', validators=[DataRequired(), Email()])
    password = PasswordField(label='password', validators=[DataRequired(), validators.Length(min=6, max=35)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
Bootstrap(app)
csrf = CSRFProtect(app)
app.secret_key = 'xxxyyyzzz'


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if request.method=="GET":
        login_form.validate_on_submit()
        return render_template("contact.html", form=login_form)

    elif login_form.validate_on_submit():
        if login_form.email.data=="admin@email.com" and login_form.password.data=="12345678":
            return render_template("login_success.html")
        else:
            return render_template("login_error.html")
        
        
    
        


if __name__ == "__main__":
    app.run(debug=True)