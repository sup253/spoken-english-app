from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/practice')
def practice():
    return render_template("practice.html")

if __name__ == '__main__':
    app.run(debug=True)

