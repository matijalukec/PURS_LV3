from flask import Flask, request, render_template

app = Flask("Prva flask aplikacija")

@app.route('/login', methods=["POST"])
def post_metoda():
    if request.form.get('username') == "PURS" and request.form.get('password') == "1234":
        return render_template("index.html"), 200
    return render_template("login.html"), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)