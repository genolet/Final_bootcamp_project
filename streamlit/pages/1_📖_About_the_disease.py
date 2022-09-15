import streamlit as st
from PIL import Image


header = st.container()

with header:
    st.title("About the disease")
    st.write("Hypothyroidism (underactive thyroid) is a condition in which your thyroid gland doesn't produce enough of certain crucial hormones.")
    st.write("Symptoms may include:")
    st.markdown("- Fatigue")
    st.markdown("- Weight gain")
    st.markdown("- Muscle weakness")
    st.markdown("- Elevated blood cholesterol level")
    st.markdown("- Depression")
    st.markdown("- Impaired memory")
    st.markdown("- Enlarged thyroid gland (goiter)")
    image = Image.open('./images/thyroid_hormones.jpeg')
    new_image = image.resize((600, 500))
    st.image(new_image)
    st.write("The hypothalamus, pituitary, and the thyroid gland (also called the hypothalamic/pituitary/thyroid or HPT axis) control thyroid hormone levels")
    st.write("Thyrotropin-releasing hormone (TRH) made in the hypothalamus binds to the receptors in the pituitary, causing it to release the thyroid-stimulating hormone (TSH), which then stimulates T4 production. Most T3 is produced by removing iodine from T4.")
    st.write("The FTI or Free T4 index is calculated from the total T4 levels and a measurement called thyroid hormone-binding index.")
    st.write("Low T3 and T4 (FTI), together with high TSH levels, are usually an indicator of hypothyroidism.")
    st.write("sources: https://www.mayoclinic.org/diseases-conditions/hypothyroidism/symptoms-causes/syc-20350284, https://health.selfdecode.com/blog/hypothyroidism-may-good-autoimmunity/, ")







