api_key = 'apk-ff425012514385974a54b3638328b2d3033dcd17f3f1a0d9517031d0dc730320f529724669890085fefa3686fcfb1406350b91baba5d7156ebc4a50c1a10bb4047b2d60f066ee583143b6eee53076880'
from rxn4chemistry import RXN4ChemistryWrapper

rxn4chemistry_wrapper = RXN4ChemistryWrapper(api_key=api_key)

rxn4chemistry_wrapper.create_project('test_wrapper')
print(rxn4chemistry_wrapper.project_id)