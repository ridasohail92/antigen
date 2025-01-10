from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return render_template("base.html")

@app.route('/toxicity/')
def toxicity():
    return render_template('toxicity.html')

