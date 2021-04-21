from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():

    name = "Son"
    return render_template('home.html', name=name)

@app.route('/about')
def about():
    return "Hello, about page"

@app.route('/script')
def test_script():
    return render_template('test-script.html')

if __name__ == '__main__':
    app.run(debug=True)
