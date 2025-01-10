import pandas as pd
from flask import Flask, render_template, request, redirect
from chemistry.py
#url_for('static', filename='style.css') if we use this file


app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return render_template("base.html")

@app.route('/toxicity/')
def toxicity():
    return render_template('toxicity.html')

def UserSmiles(smiles_query,num_of_comparison):
    return 

smilescomps = pd.read_csv("filewithsmiles")


def compare_smiles(smilescomps):
    print 
    


@app.route("/", methods=["POST"])
def usersmile():
    
    if request.method == 'POST':
       return "Hello"
       '''task_content = request.form['content']
        return 'Finding Your Results...''''
    else:
        return render_template("base.html") 

@app.route("/newsmile/<usersmile>", methods = ["GET"])
def mysmile(usersmile):
   return "This endroute works"
   ''' query = request.args.get(compare_smiles(smilescomps))
    return render_template('finishthis.html') '''
    

if __name__ == "__main__":
    app.run(debug=True) 
