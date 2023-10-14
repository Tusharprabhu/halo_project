from flask import Flask, render_template
# from functions import test1, test2

app = Flask(__name__)

def hello():
    return "hello"

@app.route('/hello')
def hello():
    return hello()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/options')
def options():
    return render_template('option.html')

@app.route('/calculator')
def calculator():
    return render_template('calculator.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/testing')
def testing():
    return render_template('testing.html')

if __name__ == '__main__':
    app.run(debug=True)
