import streamlit as st
from PIL import Image
import numpy as np
import pickle
from streamlit_extras.add_vertical_space import add_vertical_space
import tensorflow as tf

# sidebar page links
def authenticated_menu():
    st.sidebar.empty()
    st.sidebar.page_link("pages/1_Anxiety.py", label="Anxiety Disorder")
    st.sidebar.page_link("pages/2_Asthama.py", label="Asthma")
    st.sidebar.page_link("pages/3_CP.py", label="Cerebral Palsy")
    st.sidebar.page_link("pages/4_Down.py", label="Down Syndrome")
    st.sidebar.page_link("pages/5_Jaundice.py", label="Jaundice")
    st.sidebar.page_link("pages/6_Pneumonia.py", label="Pneumonia")
    
def predict_image(image):
    model_path = "../Backend/down.sav"
    model = pickle.load(open(model_path, 'rb'))
    img_tensor = tf.convert_to_tensor(image)
    if img_tensor.shape[-1] != 3: 
        img_tensor = tf.image.grayscale_to_rgb(img_tensor)
    img_tensor = tf.image.resize(img_tensor, size =(250,250))
    img_tensor = tf.expand_dims(img_tensor, axis=0)
    img = img_tensor/255.0
    y = model.predict(img)
    return y

def render_predict(): 
    st.header("Predict Down Syndrome")
    st.write("Upload an image (in jpg or png format) and click the 'Predict' button to perform prediction:")
    add_vertical_space(2)

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        if st.button('Predict'):
            # Pass the image to the prediction function
            prediction = predict_image(image)
            # Display the prediction result
            prediction*=100
            prediction = "{:.3f}".format(prediction[0][0])
            str = f"Child has a probablity of {prediction}% Down Syndrome"
            st.markdown(f"<h6 style='text-align: center; font-style: italic; color: #2B8C0C'>{str}</h6>", unsafe_allow_html=True)
    
def render_overview():
    st.header("Down Syndrome in Children")
    st.image('../assets/down.png')
    st.markdown(
        """
        Down syndrome is a genetic disorder caused by the presence of an extra chromosome 21. 
        It is characterized by distinct physical features, developmental delays, and intellectual 
        disabilities. Down syndrome occurs in approximately 1 in every 700 births, making it one 
        of the most common chromosomal conditions.
        """
    )
    st.write("---")
    
    st.subheader("Prevalence and Risk Factors")

    st.markdown(
        """
        **Prevalence**: Down syndrome affects individuals of all races and ethnicities 
        worldwide, with prevalence rates varying across populations. The risk of having a 
        child with Down syndrome increases with maternal age, particularly for women over 35.
        
        **Risks Factors**: Apart from maternal age, other risk factors include having a 
        family history of Down syndrome or carrying a chromosomal translocation.
        """
    )
    st.image('../assets/down_syndrome_prevalence.png', caption='Source: Research Gate', use_column_width=True)
    add_vertical_space(2)
    
    st.subheader("Characteristics")

    st.markdown(
        """
        Common characteristics of Down syndrome include:
        
        - Low muscle tone (hypotonia)
        - Upward slanting eyes
        - Small ears and mouth
        - Flat nasal bridge
        - Short stature
        - Developmental delays, including speech and motor skills
        - Intellectual disabilities
        
        It's important to note that individuals with Down syndrome are unique and may 
        exhibit a wide range of abilities and challenges.
        """
    )
    st.image('../assets/down_syndrome_characteristics.png', caption='Source: DSEE', use_column_width=True)
    add_vertical_space(2)
    
    st.subheader("Support and Resources")

    st.markdown(
        """
        Despite the challenges associated with Down syndrome, individuals with this condition 
        can lead fulfilling lives with the appropriate support and resources. Early intervention 
        programs, educational support, and access to healthcare services are crucial in 
        maximizing the potential of individuals with Down syndrome.
        """
    )
    add_vertical_space(2)
    st.markdown(
        """
        For more information and support for individuals with Down syndrome and their families, 
        please refer to organizations such as the National Down Syndrome Society (NDSS) or 
        the Global Down Syndrome Foundation.
        """
    )


def main():
    render_overview()
    st.write("---")
    st.write("---")
    render_predict()
        
            
    
if __name__ == "__main__":
    authenticated_menu()
    main()
    
    # back to home
    if st.button("Back to Home"):
        st.switch_page("Landing.py")
        
    