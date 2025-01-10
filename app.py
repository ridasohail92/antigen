# import pandas as pd
from flask import Flask, render_template, request, Response
from chemistry import smiles_to_svg
#url_for('static', filename='style.css') if we use this file


app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return render_template("base.html")

@app.route('/toxicity/')
def toxicity():
    smilestoToxicity = {
         "CCC(Cl)C(N)C1=CC=CC=C1" : 2.8,
    "CCC(Cl)C(F)C1=CC=CC=C1" : 3.2,
    "CCC(Cl)C(F)C1CCCCC1" : 3.4 ,
    "CCC(Cl)C(N)C1CCCCC1" : 2.6,
    "CCC(F)C(Cl)CC" : 2.8,
    "CCC(F)C(N)CC" : 2.9,
    "CCC(Cl)C(N)C1CCC2CCCCC2C1" : 3.8,
    }
    return render_template('toxicity.html', smilesDict=smilestoToxicity)

@app.route("/compound-image", methods=["GET"], endpoint="get_compound_image")
def get_compound_image():
    smiles = request.args.get("smiles", "")
    return Response(smiles_to_svg(smiles), mimetype="image/svg+xml")
