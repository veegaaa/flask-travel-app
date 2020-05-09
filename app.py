from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def template_index():
    return render_template("index.html")

@app.route("/departure/<int:num_depart>")
def template_departure(num_depart):
    return render_template("departure.html")

@app.route("/tours/<int:id_tour>")
def template_tours(id_tour):
    return render_template("tour.html")

app.run('0.0.0.0', 8000, debug=True)