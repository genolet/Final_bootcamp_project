import streamlit as st
from PIL import Image

header = st.container()

st.sidebar.success(" ")

with header:
    st.title("Hypothyroidism Disease Predictor")
    st.subheader("Identify patients suffering from hypothyroidism disease by imputing 8 simple values!")
    image = Image.open('./images/ThyroidDiseases_share.jpeg')
    new_image = image.resize((200, 300))
    st.image(new_image)
    st.write(" ")
    st.write(" ")
    st.write("About one in 300 persons suffer from hypothyroidism. However, reaching the correct diagnosis can be challenging, especially since it doesn't depend on just one indicator. The Hypothyroid Disease Predictor helps doctors decide whether a patient suffers or not from this type of thyroid disorder.")







