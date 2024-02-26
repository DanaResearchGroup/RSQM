response = rxn4chemistry_wrapper.predict_automatic_retrosynthesis(
    'O=C(C)Oc1ccccc1C(=O)O'
)
results = rxn4chemistry_wrapper.get_predict_automatic_retrosynthesis_results(
    response['65673aff0fb57c001f3d5126']
)
print(results['status'])

print(results['retrosynthetic_paths'][0])
