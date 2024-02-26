#SMILES format validation of input molecules
from rdkit import Chem
def SMILES(target):
    if not target:
        return "No molecules were entered"

    mol = Chem.MolFromSmiles(target)
    if mol:
        smiles = Chem.MolToSmiles(mol)
        return smiles
    else:
        return "Invalid molecule"
# input details        
def get_user_input():
    project_name = input("Enter the name of the project: ")
    target_molecule = SMILES(input("Enter the target molecule in SMILES: "))
    retrosynthesis_software = input("Enter the retrosynthesis software name: ")
    banned_molecules_input = SMILES(input("Enter banned molecules (comma-separated, leave blank if none): "))
    banned_molecules = [mol.strip() for mol in banned_molecules_input.split(',') if mol.strip()]

    return project_name, target_molecule, retrosynthesis_software, banned_molecules

#ASKCOS 
import copy
import numpy as np
import requests
query_template = {
    "smiles": "",
    "expand_one_options": {
        "template_max_count": 100,
        "template_max_cum_prob": 0.995,
        "banned_chemicals": [],
        "banned_reactions": [],
        "retro_backend_options": [
            {
                "retro_backend": "template_relevance",
                "retro_model_name": "reaxys",
                "max_num_templates": 100,
                "max_cum_prob": 0.995,
                "attribute_filter": []
            }
        ],
        "use_fast_filter": True,
        "filter_threshold": 0.75,
        "cluster_precursors": False,
        "cluster_setting": {
            "feature": "original",
            "cluster_method": "hdbscan",
            "fp_type": "morgan",
            "fp_length": 512,
            "fp_radius": 1,
            "classification_threshold": 0.2
        },
        "extract_template": False,
        "return_reacting_atoms": False,
        "selectivity_check": False
    },
    "build_tree_options": {
        "expansion_time": 60,
        "max_branching": 25,
        "max_depth": 6,
        "exploration_weight": 1,
        "return_first": True
    },
    "enumerate_paths_options": {
        "path_format": "json",
        "json_format": "nodelink",
        "sorting_metric": "plausibility",
        "validate_paths": True,
        "score_trees": False,
        "cluster_trees": False,
        "cluster_method": "hdbscan",
        "min_samples": 5,
        "min_cluster_size": 5,
        "paths_only": False,
        "max_paths": 200
    },
}
def askcos(target_molecule):
    HOST = "0.0.0.0"
    PORT = "9100"
    smiles = target_molecule
    #times = []
    #successes = []
    data = copy.deepcopy(query_template)
    data["smiles"] = smiles.strip()
    resp = requests.post(
        url=f"http://{HOST}:{PORT}/api/tree-search/mcts/call-sync-without-token",
        json=data
    ).json()
    #first_path_time = resp["result"]["stats"]["first_path_time"]
    total_paths = resp["result"]["stats"]["total_paths"]
    paths=resp["result"]["paths"]
    print(f"SMILES: {smiles.strip()}, {total_paths}, {paths}")

#IBMRXN
def ibm(target_molecule):
    import time
    from IBMRXN.rxn4chemistry import RXN4ChemistryWrapper
    api_key = 'apk-ffe4dcc5783fbb45eb10438d30de862effbffe625cbc045b35af42ec289854796b7c2b1014932e62681601dcf0479d60f31ea74b83c1786a203ba638a528c9d2fa26e2690847d1eb68bba8e88fa23be1'
    smiles=target_molecule
    rxn4chemistry_wrapper = RXN4ChemistryWrapper(api_key=api_key)
    rxn4chemistry_wrapper.create_project('test_wrapper')
    time.sleep(1)
    rxn4chemistry_wrapper.project_id
    time.sleep(1)
    response= rxn4chemistry_wrapper.predict_automatic_retrosynthesis(smiles)
    time.sleep(1)
    rsp=response['prediction_id']
    time.sleep(1)
    results = rxn4chemistry_wrapper.get_predict_automatic_retrosynthesis_results(rsp)
    status= results['status']
    print(status)
    while status!='SUCCESS':
        time.sleep(1)
        rsp=response['prediction_id']
        time.sleep(1)
        results = rxn4chemistry_wrapper.get_predict_automatic_retrosynthesis_results(rsp)
        time.sleep(1)
        status= results['status']
        print (status)
    
    for item in results:
        print(item)
    print (results)

if __name__ == "__main__":
    # Get user input
    project_name, target_molecule, retrosynthesis_software, banned_molecules = get_user_input()

    # Display input information
    print("\nProject Name:", project_name)
    print("Target Molecule:", target_molecule)
    print("Retrosynthesis Software:", retrosynthesis_software)
    print("Banned Molecules:", banned_molecules)
    if retrosynthesis_software== "askcos": 
       askcos(target_molecule)
    elif retrosynthesis_software=='ibm':
        ibm(target_molecule)
