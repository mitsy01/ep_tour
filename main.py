from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/tour/')
def tour():
    return render_template("tour.html")


@app.route('/departure/')
def departure():
    return render_template("departure.html")


if __name__ == "__main__":
    app.run(debug=True)