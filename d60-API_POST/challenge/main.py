from flask import Flask, render_template, request
import requests
from mail_handler import MailHandler

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

mail_handler = MailHandler()

# print("posts : ", posts)
app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method=="GET":
        return render_template("contact.html", h1="Contact Me")
    elif request.method=="POST":
        print("form-entry ! ", request.form)
        # return "<h1>Successful</h1>"
        quote = mail_handler.craft_email(request.form)
        print("quote : ", quote)
        mail_handler.send_mail( quote=quote ) 
        return render_template("contact.html",h1="successful send!")

# @app.route("/form-entry", methods=['POST'])
# def receive_data():

if __name__ == "__main__":
    app.run(debug=True)
