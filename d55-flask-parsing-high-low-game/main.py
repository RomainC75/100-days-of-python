from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_func():
        return f'<b>{function()}</b>'
    return wrapper_func
def make_emphasis(function):
    def wrapper_func():
        return f'<em>{function()}</em>'
    return wrapper_func
def make_underline(function):
    def wrapper_func():
        return f'<u>{function()}</u>'
    return wrapper_func

@app.route('/')
def hello():
    return "<p>Hello, World!</p>"


@app.route("/username/<string:name>")
@make_bold
# @make_underlined
def hello_name(name):
    # return f'<h1 style="text-align:center">Hello sdfsdf{name}</h1>'
    return "bye"



if __name__ == "__main__":
    app.run(debug=True) 