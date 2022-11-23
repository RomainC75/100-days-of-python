from flask import Flask, render_template
import random
from datetime import datetime
import requests
app = Flask(__name__)

@app.route('/')
def home():
    nb = random.randint(0,10)
    year = datetime.now().year
    name = "Romain C"
    return render_template("index.html", name=name, year=year)

@app.route("/guess/<string:name>")
def guess(name):
    raw_age = requests.get(f'https://api.agify.io?name={name}')
    age = raw_age.json()['age']
    raw_gender = requests.get(f'https://api.genderize.io?name={name}')
    gender = raw_gender.json()['gender']
    
    return render_template("index.html", age=age, gender=gender, name=name, creator="RomainC")

@app.route("/blog/<int:id>")
def blog_id(id):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_posts = requests.get(blog_url).json()
    post = list(filter(lambda post:post['id']==id,blog_posts))
    if len(post)>0:
        print("post : ", post[0])
        return render_template("post.html",  post=post[0] )
    else:
        return "<h1>no post found !</h1>"

@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_posts = requests.get(blog_url).json()
    return render_template("blog.html", posts = blog_posts)



if __name__ == "__main__":
    app.run(debug=True)


