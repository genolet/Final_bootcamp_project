import streamlit as st
from PIL import Image

header = st.container()
body = st.container()

with header:
    st.title("Using machine learning for the prediction of hypothyroidism")

with body:
    st.subheader("The random forest machine learning model was chosen for best performance")
    st.write(" ")
    st.write(" ")
    st.write("Data source: https://archive.ics.uci.edu/ml/datasets/thyroid+disease")
    st.write("From 29 initial features, 5 were chosen for disease prediction: sex, whether the patient is on thyroxine medication, TSH, T3 and FTI levels")
    st.write(" ")
    st.write(" ")
    st.write("The following parameters were chosen for the random forest model:")
    image = Image.open('./images/RF_parameters.png')
    st.image(image)
    st.write(" ")
    st.write(" ")
    st.subheader("Results")
    st.write("Confusion matrix: all diseased individuals were recognized by the model!")
    image = Image.open('./images/rf_cm_test.png')
    st.image(image)
    st.write("Metrics")
    image = Image.open('./images/metrics_test_set.png')
    new_image = image.resize((400, 200))
    st.image(new_image)
    st.write("Feature importance")
    image = Image.open('./images/rf_feature_importance.png')
    new_image = image.resize((500, 350))
    st.image(new_image)
    st.subheader("Conclusion")
    st.write("The random forest classifier was able to predict whether an individual was healthy or diseased with 99% accuracy. Most importantly, all diseased individuals were correctly classified by the model!")














