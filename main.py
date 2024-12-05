from flask import Flask, render_template, request, redirect, url_for

from data import data

app = Flask(__name__)
DEPARTURES = data.departures

@app.route('/')
def index():
    return render_template("index.html", departures=DEPARTURES, tours=data.tours)


@app.route('/tour/<int:index>')
def tour(index):
    tour = data.tours.get(index)
    return render_template("tour.html", departures=DEPARTURES, tour=tour)


@app.route('/departure/<dep>/')
def departure(dep):
    return render_template("departure.html", departures=DEPARTURES)


if __name__ == "__main__":
    app.run(debug=True)