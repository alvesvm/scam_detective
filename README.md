# SCAM Detective
<p align="center">
  <img align="middle" src="/docs/logo.png" alt="SCAMDetective" width="800" class="center">
 </p>


SCAM Detective is a machine learning application and web portal (https://scamdetective.mml.unc.edu/) to identify putative Small Colloidally Aggregating Molecules (SCAMs) in chemical libraries used in high-throughput screening (HTS). SCAM Detective models were developed to predict, with high accuracy, the detergent-sensitive aggregation of compounds in AmpC β-lactamase and cruzain inhibition assays, the preferred counter-screens used widely to identify false positives in the HTS campaigns.

The SCAM Detective provides an alternative method for assessing the potential of chemicals to be putative aggregators and cause false-positive readouts in bioassays. SCAM Detective makes predictions based on Quantitative Structure-Interference Relationship (QSIR) models built on two independent datasets generated from High Throughput Screening campaigns against AmpC β-lactamase (PubChem AID [485341](https://pubchem.ncbi.nlm.nih.gov/bioassay/485341)/[485294](https://pubchem.ncbi.nlm.nih.gov/bioassay/485294) and AID [585](https://pubchem.ncbi.nlm.nih.gov/bioassay/585)/[584](https://pubchem.ncbi.nlm.nih.gov/bioassay/584)) and the cysteine protease cruzain (PubChem AID [1476](https://pubchem.ncbi.nlm.nih.gov/bioassay/1476)/[1478](https://pubchem.ncbi.nlm.nih.gov/bioassay/1476)). The models were developed using open-source chemical descriptors based on ECFP6-like Morgan fingerprints with 2048 bits and an atom radius of 3 calculated in RDKit, along with the random forest (RF) algorithm, using Python 3.6. The models were generated applying the best practices for model development and validation widely accepted by the community (see the figure below).

<p align="center">
  <img align="middle" src="/docs/Fig1.png" alt="workflow" width="800" class="center">
 </p>

A web application version of this tool is available at: https://scamdetective.mml.unc.edu/.
The toolkit in this GitHub allows batch predictions.

# Supported functionality
## Tasks:
* To predict, with high accuracy, the detergent-sensitive aggregation of compounds in AmpC β-lactamase and cruzain inhibition assays, the preferred counter-screens used widely to identify false positives in the HTS campaigns.
* Maps of the predicted fragment contribution are generated allowing interpretation of the predictions.

## Data types allowed as input
* SDF
* SMILES in .csv or .txt.

## Requirements
* Download QSIR models from [here](https://figshare.com/s/bcf12452709c1fac3a58).
* Python 3.6+ ([Anaconda](https://www.anaconda.com/distribution/) distribution is recommended)
* [RDKit](https://www.rdkit.org/docs/Install.html)
* [scikit-learn](http://scikit-learn.org/)

## More information
For more information, please refer to our paper:
Alves, V. M.; Capuzzi, S. J.; Braga, R.; Korn, D.; Hochuli, J.; Bowler, K.; Yasgar, A.; Rai, G.; Simeonov, A.; Muratov, E. N.; Zakharov, A. V.; Tropsha, A. SCAM Detective: Accurate Predictor of Small, Colloidally-Aggregating Molecules. *J. Chem. Inf. Model.* **2020**, *acs.jcim.0c00415*. https://doi.org/10.1021/acs.jcim.0c00415. Our paper was the Editor's choice for the August issue of the journal:

<p align="center">
  <img align="middle" src="/docs/cover.png" alt="JCIMcover" width="400px" class="center">
 </p>

# Acknowledgements

SCAM Detective is sponsored by the [UNC Eshelman School of Pharmacy](https://pharmacy.unc.edu/) of the [University of North Carolina at Chapel Hill](https://www.unc.edu/).
<p align="middle">
  <img src="./docs/ESOP.png" alt="ESOP" width="500px">
  <img src="./docs/UNC.jpg" alt="UNC" width="300px">
  <br>
</p>
