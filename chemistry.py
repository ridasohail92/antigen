# import

import pandas as pd
import numpy as np

# ---------------------- RDKit packages
from rdkit.Chem import AllChem
from rdkit.Chem import rdMolDescriptors as rdmd
from rdkit import Chem
from rdkit import DataStructs

import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors
import torch
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib


# ------------------- hide warning
import warnings

warnings.filterwarnings("ignore")


def compare_to_Smiles(query_smiles, top_n):
    """ """

    dataset = pd.read_csv("dataset.csv")

    from rdkit.Chem import PandasTools

    PandasTools.AddMoleculeColumnToFrame(dataset, "SMILES", "Structure")

    # Let us find compounds similar Aspirin
    query = AllChem.MolFromSmiles("O=C(C)Oc1ccccc1C(=O)O")
    query_fps = AllChem.GetMorganFingerprintAsBitVect(query, 2, nBits=4096)

    # Calculate the fingerprints of all the compounds(total 2904)
    all_Mfpts = [
        AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=4096)
        for mol in dataset.Structure
    ]

    # calculate Tanimoto coefficient of the query compound against each of the compounds in the dataset
    # put them in the list
    Tanimoto_similarity = [
        DataStructs.FingerprintSimilarity(
            query_fps, x, metric=DataStructs.TanimotoSimilarity
        )
        for x in all_Mfpts
    ]

    # put the Tanimoto coefficient values into data frame.
    dataset["tanimoto_values"] = Tanimoto_similarity

    # sort Tanimoto coefficient values in decreasing order
    # dataset_sorted = dataset.sort_values(['tanimoto_values'],ascending=False)

    top_n = 10  # Set the number of top rows you want
    dataset_sorted = dataset.sort_values(["tanimoto_values"], ascending=False).head(
        top_n
    )

    # Function to compute molecular descriptors from SMILES
    def compute_descriptors(smiles):
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return None
        descriptors = {}
        for name, func in Descriptors.descList:
            descriptors[name] = func(mol)
        return descriptors

    # Apply descriptor computation to your dataset
    dataset_sorted["descriptors"] = dataset_sorted["SMILES"].apply(compute_descriptors)

    # Convert the descriptors into a feature matrix (excluding rows with None)
    feature_matrix = []
    for descriptors in dataset_sorted["descriptors"]:
        if descriptors is not None:
            feature_matrix.append(list(descriptors.values()))
        else:
            feature_matrix.append([None] * len(Descriptors.descList))

    # Create a DataFrame for the features
    features_df = pd.DataFrame(
        feature_matrix, columns=[desc[0] for desc in Descriptors.descList]
    )

    # Standardize the features
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features_df.fillna(0))

    # Load a toxicity prediction pipeline
    model = pd.read_csv("prediction.csv")

    # Merge the two datasets on the 'SMILES' column
    output_df = pd.merge(
        dataset_sorted, model[["SMILES", "Toxicity"]], on="SMILES", how="left"
    )

    # Convert the output dataframe to a dictionary
    toxicity_dict = output_df.set_index("SMILES")["Toxicity"].to_dict()

    # Display the dictionary
    # print(toxicity_dict)

    return toxicity_dict
