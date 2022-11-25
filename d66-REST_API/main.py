from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random
from utils import row2dict

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

API_SECRET_KEY = "TopSecretAPIKey"


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")
    

@app.route("/random")
def get_random():
    cafes = Cafe.query.all()
    random_cafe_sqlA = random.choice(cafes)
    random_cafe = row2dict(random_cafe_sqlA)
    print("=====>", random_cafe)
    print("vafes : ", cafes)
    return jsonify(random_cafe)

@app.route("/all")
def get_all():
    cafes = Cafe.query.all()
    all_cafes = [ row2dict(cafe) for cafe in cafes ]
    return jsonify(all_cafes)

@app.route("/search/")
def get_search():
    loc = request.args.get('loc')
    print("loc : ", loc)
    cafes =  Cafe.query.filter_by(location=loc).all()
    if len(cafes)==0:
        return {"error":"Sorry, we don't have a cafe a that location"}, 400
    return jsonify([row2dict(cafe) for cafe in cafes ])

@app.route("/add", methods=['POST'])
def add_cafe():
    try:
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("loc"),
            has_sockets=bool(request.form.get("sockets")),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            can_take_calls=bool(request.form.get("calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
            )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success":"new cafe added !"})
    except:
        return jsonify(response={"error":"oops, something went wrong !"}),400

@app.route("/update-price/<int:id>", methods=['PATCH'])
def update_price(id):
    try:
        new_price = request.args.get("new_price")
        print("id : ", id, "new_price : ", new_price)
        found_cafe = Cafe.query.filter_by(id=id).first()
        print("found_cafe : ", found_cafe)
        found_cafe.coffee_price=new_price
        db.session.commit()  
        return jsonify(response={"success":"cafe updated"}),201
    except:
        return jsonify(response={"error":"oops, something went wrong !"}),400
    
@app.route("/delete/<int:id>", methods=['DELETE'])
def delete(id):
    try:
        api_key=request.args.get("api_key")
        print("key : ", api_key)
        if api_key != API_SECRET_KEY:
            return jsonify(response={"erro":"wrong api_key"}),401    
        found_cafe = Cafe.query.get(id)
        if not found_cafe:
            return jsonify(response={"erro":"cafe not found"}),401    
        db.session.delete(found_cafe)
        db.session.commit()
        return jsonify(response={"success":"cafe deleted"}),201
    except:
        return jsonify(response={"error":"oops, something went wrong !"}),400
    


    
    



## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
