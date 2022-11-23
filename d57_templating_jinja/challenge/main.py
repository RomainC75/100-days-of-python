from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    posts_url = "https://api.npoint.io/c790b4d5cab58020d391"
    posts = requests.get(posts_url).json()
    return render_template("index.html", posts=posts)

@app.route('/<int:id>')
def get_post(id):
    posts_url = "https://api.npoint.io/c790b4d5cab58020d391"
    posts = requests.get(posts_url).json()
    return render_template("post.html", posts=posts, id=id)

if __name__ == "__main__":
    app.run(debug=True)
