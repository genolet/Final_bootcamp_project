import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import functions.functions as f

header = st.container()
input_features = st.container()

with header:
    st.title("Hypothyroid Disease Predictor")

with input_features:
	st.subheader("Please enter the following values:")
	sex = st.selectbox(
     'Please enter the patient´s sex',
     ('Female', 'Male'))
	on_thyroxine = st.selectbox(
     'Is the patient on thyroxine medication?',
     ("Yes", 'No'))
	on_antithyroid_medication = st.selectbox(
     'Is the patient on antithyroid medication?',
     ("Yes", 'No'))
	pregnant = st.selectbox(
     'Is the patient pregnant?',
     ("Yes", 'No'))
	goitre = st.selectbox(
     'Does the patient suffer from goiter?',
     ("Yes", 'No'))
	tsh = st.slider('Please enter the patient´s TSH levels (mU/L)', 0.0, 150.0, 0.5)
	t3 = st.slider('Please enter the patient´s T3 levels (nmol/L)', 0.0, 11.0, 0.05)
	fti = st.slider('Please enter the patient´s FTI levels (nmol/L)', 0.0, 400.0, 0.5)


def thyroid_disease_predictor(sex, on_thyroxine, on_antithyroid_medication, pregnant, goitre, tsh, t3, fti):
    try:
        values = []
        features = [sex, on_thyroxine, on_antithyroid_medication, pregnant, goitre, tsh, t3, fti]
        for feature in features:
            values.append(feature)
        columns = ["sex", "on_thyroxine", "on_antithyroid_medication", "pregnant", "goitre", "tsh", "t3", "fti"]
        df = pd.DataFrame(values).T
        df.columns = columns
        df["sex"] = df["sex"].replace({"Female":1, "Male":0})
        cols = ["on_thyroxine", "on_antithyroid_medication", "pregnant", "goitre"]
        for col in cols:
            df[col] = df[col].replace({"Yes":1, "No":0})
        scaler = f.load("./transformers/minmaxscaler.pickle")
        df = scaler.transform(df)
        rf_clf = f.load("./models/rf_clf.pickle")
        pred = rf_clf.predict(df)
        pred_prob = rf_clf.predict_proba(df)
        if pred[0] == "Healthy":
            return "The patient has a {:.1f}% probability of being healthy".format((pred_prob[0][1])*100) 
        if pred[0] == "Diseased":
            return "The patient has a {:.1f}% probability of suffering from hypothyroidism".format((pred_prob[0][0])*100) 
    except:
        return "Opps, sorry, something went wrong. Please enter values again."

result = None 

c1 = st.container()
with c1:

    col1, col2, col3 = st.columns(3)

    with col2:

        if st.button('Predict the patient´s state 🩺'):
            result = thyroid_disease_predictor(sex, on_thyroxine, on_antithyroid_medication, pregnant, goitre, tsh, t3, fti)


c2 = st.container()     
with c2:
    st.write(" ")
    if result is not None:
        st.write(result)







