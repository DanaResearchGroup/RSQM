
# RSQM
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

RSQM is a retrosynthesis tool designed to assist in planning synthesis paths for organic molecules. This tool utilizes multiple widely-used machine learning (ML) models for retrosynthesis planning. Each ML model is based on different algorithms and generates predictions in a unique way. By combining these different tools, RSQM aims to increase the possibility of generating a feasible synthetic path for a given input molecule.

## Features
- RSQM integrates multiple ML tools for retrosynthesis planning.
- Predictions made by RSQM are validated through two validation systems:
  1. Forward reaction validation system.
  2. Quantum mechanics validation system.
- RSQM provides an output of the top-rated synthesis paths based on the RS tools and validation systems.

## Repository Contents
- **RS Adapter:** The adapter module responsible for integrating various ML tools and managing their predictions.
- **Forward Validation System:** Module for validating predictions through forward reaction validation.
- **QM Validation System:** Module for validating predictions using quantum mechanics based tools. 



## License
This project is licensed under the [MIT License](LICENSE).
