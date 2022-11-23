from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
csrf = CSRFProtect(app)
app.secret_key = 'xxxyyyzzz'

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[ DataRequired() ])
    location = StringField('Location', validators=[ DataRequired() ])
    open = StringField('Open', validators=[ DataRequired() ])
    close = StringField('Close', validators=[ DataRequired() ])
    coffe = SelectField('Coffe', choices=[(0, '✘'), (1, '☕️'), (2, '☕️☕️'), (3, '☕️☕️☕️'), (4, '☕️☕️☕️☕️'), (5, '☕️☕️☕️☕️☕️')])
    wifi = SelectField('Wifi', choices=[(0, '✘'), (1, '💪'), (2, '💪💪'), (3, '💪💪💪'), (4, '💪💪💪💪'), (5, '💪💪💪💪💪')])
    power = SelectField('Power', choices=[(0, '✘'), (1, '🔌'), (2, '🔌🔌'), (3, '🔌🔌🔌'), (4, '🔌🔌🔌🔌'), (5, '🔌🔌🔌🔌🔌')])
    submit = SubmitField(label='Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET','POST'])
def add_cafe():
    form = CafeForm()
    if request.method=="GET":
        form.validate_on_submit()
        return render_template("add.html", form=form)
    elif form.validate_on_submit():

        cafe = form.cafe.data
        location = form.location.data
        open_var = form.open.data
        close_var = form.close.data
        coffe = int(form.coffe.data)*'☕️'  if int(form.coffe.data)>0 else '✘'
        wifi = int(form.wifi.data)*'💪'  if int(form.coffe.data)>0 else '✘'
        power = int(form.power.data)*'🔌'  if int(form.coffe.data)>0 else '✘'
        print(cafe,location,open_var, close_var, wifi, power)

        with open('cafe-data.csv', 'a', newline='\n') as csvfile:
            coffewriter = csv.writer(csvfile, delimiter=',')
            coffewriter.writerow([ cafe, location, open_var, close_var, coffe, wifi, power ])
        csvfile.close()

        return redirect(url_for('cafes'))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    

@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    csv_file.close()
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
