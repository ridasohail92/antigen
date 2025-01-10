from flask import Flask, render_template, request, Response
from chemistry import smiles_to_svg, compare_to_Smiles

app = Flask(__name__)


@app.route("/", methods=["GET"], endpoint="base")
def root():
    return render_template("home.html")

@app.route('/toxicity/', endpoint="toxicity_results")
def toxicity():
    smiles_query = request.args.get("smiles_query")
    num_compounds = request.args.get("num_compounds")
    # similar_smiles = {
    #      "CCC(Cl)C(N)C1=CC=CC=C1" : 2.8,
    # "CCC(Cl)C(F)C1=CC=CC=C1" : 3.2,
    # "CCC(Cl)C(F)C1CCCCC1" : 3.4 ,
    # "CCC(Cl)C(N)C1CCCCC1" : 2.6,
    # "CCC(F)C(Cl)CC" : 2.8,
    # "CCC(F)C(N)CC" : 2.9,
    # "CCC(Cl)C(N)C1CCC2CCCCC2C1" : 3.8,
    # }
    similar_smiles = compare_to_Smiles(smiles_query, num_compounds)

    sorted_smiles  = {}
    sorted_smiles = {k: v for k, v in sorted(similar_smiles.items(), reverse=True, key=lambda item: item[1])}
    return render_template('toxicity.html', smilesDict=sorted_smiles)

@app.route("/compound-image", methods=["GET"], endpoint="get_compound_image")
def get_compound_image():
    smiles = request.args.get("smiles", "")
    return Response(smiles_to_svg(smiles), mimetype="image/svg+xml")
