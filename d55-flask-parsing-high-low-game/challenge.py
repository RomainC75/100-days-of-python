from flask import Flask
import random

app = Flask(__name__)

val=random.randint(0,9)

@app.route("/")
def home():
    return '''
    <h1>"Guess a number between 0 and 9"</h1>
    <img src="https://media.giphy.com/media/LzLkUxxsJz6ZG/giphy.gif"/>
    '''

@app.route("/guess/<int:number>")
def test_guess(number):
    if number>val:
        return '''
            <h1>lower</h1>
        '''
    elif number<val:
        return '''
            <h1>higher</h1>
        '''
    else:
        return '''
            <h1>won !</h1>
        '''

if __name__ == "__main__":
    app.run(debug=True)