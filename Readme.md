# Hypothyroidism Disease Predictor

### Objective

This project aims to implement machine learning algorithms to predict hypothyroidism. Base machine learning models such as logistic regression, K nearest neighbors, naive Bayes, and random forest were tested for best performance, together with deep learning algorithms. 

### Data sources

Thyroid dataset: [https://archive.ics.uci.edu/ml/datasets/thyroid+disease](https://archive.ics.uci.edu/ml/datasets/thyroid+disease)

### Languages and tools

Python

Jupyter notebook

Streamlit

### Results

Out of all the tested machine learning models, the Random Forest classifier was chosen for best performance. The model was able to predict healthy and diseased individuals with 99% accuracy. Most importantly, all diseased individuals were correctly diagnosed in a test dataset with approx. 1:12 data imbalance (diseased: healthy).

A hypothyroidism disease predictor can be found in: ./notebooks/[Thyroid_disease_predictor.ipynb](http://localhost:8888/notebooks/notebooks/Thyroid_disease_predictor.ipynb)

It can be visualized on the browser by running the following script (streamlit run):

./streamlit/🩺_Hypothyroidism_disease_predictor.py

### Folders in this project

- data: data generated in the jupyter notebooks (clean) and raw data from the hypothyroid dataset.
- models: fitted random forest classifier
- notebooks:
    - [Data_cleaning_thyroid_ds.ipynb](http://localhost:8888/notebooks/notebooks/Data_cleaning_thyroid_ds.ipynb)
    - [Feature_selection_hypothyroid_ds.ipynb](http://localhost:8888/notebooks/notebooks/Feature_selection_hypothyroid_ds.ipynb)
    - [EDA_hypothyroid_ds.ipynb](http://localhost:8888/notebooks/notebooks/EDA_hypothyroid_ds.ipynb): exploratory data analysis (EDA) on hypothyroid dataset
    - [Base_machine_learning_models_hypothyroid_ds.ipynb](http://localhost:8888/notebooks/notebooks/Base_machine_learning_models_hypothyroid_ds.ipynb): binary classification using logistic regression, KNN, naive bayes and random forest
    - [Neural_networks_hypothyroid_ds.ipynb](http://localhost:8888/notebooks/notebooks/Neural_networks_hypothyroid_ds.ipynb): deep learning with Keras (this notebook was run using google drive)
    - [Thyroid_disease_predictor.ipynb](http://localhost:8888/notebooks/notebooks/Thyroid_disease_predictor.ipynb)
- transformers: fitted minmaxscaler
- functions: data cleaning, feature selection and loading function for scaler and model import
- streamlit: hypothyroidism predictor using streamlit app