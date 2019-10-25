from flask import Flask, render_template

app = Flask(__name__)


@app.route("/base")
def get_main_page():
    return render_template("base.html")


@app.route("/home")
def get_home_page():
    return render_template("home.html")


@app.route("/home/vegetables")
def get_vegetable_page():
    return render_template("vegetables.html", vegetables=['beans', 'carrot', 'beetroot', 'cucumber'])


@app.route("/home/fruits")
def get_fruits_page():
    return render_template("fruits.html", fruits=['melon', 'apple', 'strawberry', 'grape'])


if __name__== "__main__":
    app.run(debug=True)
