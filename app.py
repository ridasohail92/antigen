import pandas as pd
from flask import Flask, render_template, request, redirect
#from chemistry.py import 
#url_for('static', filename='style.css') if we use this file


app = Flask(__name__)


def compare_to_Smiles(smiles_query,num_compounds):
    return "dataframe"

#smilescomps = pd.read_csv("filewithsmiles")



@app.route("/", endpoint = "base")
def base_site(): 
    return render_template("base.html") 

@app.route("/newsmile", methods = ["POST"], endpoint = "toxicity _results")
def get_new_smile():
    smiles_query = request.args.get("smiles_query")
    num_compounds = request.args.get("num_compounds")
    similar_smiles = compare_to_Smiles(smiles_query,num_compounds)

    sorted_smiles  = {}
    sorted_smiles = {k: v for k, v in sorted(similar_smiles.items(), key=lambda item: item[1])}
    return render_template('find.html', smilesDict=sorted_smiles)
    

if __name__ == "__main__":
    app.run(debug=True) 
