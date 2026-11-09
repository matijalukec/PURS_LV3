from flask import Flask, render_template

app = Flask("Prva flask aplikacija")

@app.get('/')
def index():
    return render_template("index.html"), 200

@app.get('/login')
def hello_world():
    return render_template("login.html"), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)