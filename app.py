from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/options')
def options():
    return render_template('option.html')

@app.route('/test')
def test():
    value = 1 * 2
    return render_template('index.html', value=value) 

if __name__ == '__main__':
    app.run(debug=True)
