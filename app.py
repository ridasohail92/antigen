#import pandas as pd
from flask import Flask, render_template, request, redirect
#from chemistry.py
#url_for('static', filename='style.css') if we use this file


app = Flask(__name__)


def UserSmiles(smiles_query,num_of_comparison):
    return 

#smilescomps = pd.read_csv("filewithsmiles")


def compare_smiles(smilescomps):
    print 
    


@app.route("/", methods=["GET"])
def usersmile():
    return render_template("home.html") 

@app.route("/newsmile/<usersmile>", methods = ["GET"])
def mysmile(usersmile):
   return "This endroute works"
    

if __name__ == "__main__":
    app.run(debug=True) 
