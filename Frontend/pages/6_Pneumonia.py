import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from PIL import Image
import pickle
import tensorflow as tf
import cv2
import numpy as np

def predict_image(image):
    model_path = "../Backend/pnemonia.sav"
    model = pickle.load(open(model_path, 'rb'))
    img_tensor = tf.convert_to_tensor(image)
    img_tensor = tf.expand_dims(img_tensor, axis=-1)
    if img_tensor.shape[-1] != 3: 
        img_tensor = tf.image.grayscale_to_rgb(img_tensor) 
    img_tensor = tf.image.resize(img_tensor, size =(120,120))
    img_tensor = tf.expand_dims(img_tensor, axis=0)
    print(img_tensor.shape)
    img = img_tensor/255.0
    
    
    y = model.predict(img)
    y = np.argmax(y)
    return y

# sidebar page links
def authenticated_menu():
    st.sidebar.empty()
    st.sidebar.page_link("pages/1_Anxiety.py", label="Anxiety Disorder")
    st.sidebar.page_link("pages/2_Asthama.py", label="Asthma")
    st.sidebar.page_link("pages/3_CP.py", label="Cerebral Palsy")
    st.sidebar.page_link("pages/4_Down.py", label="Down Syndrome")
    st.sidebar.page_link("pages/5_Jaundice.py", label="Jaundice")
    st.sidebar.page_link("pages/6_Pneumonia.py", label="Pneumonia")
    
def main():
    st.title("Predict Pneumonia")
    st.write("Upload an image (in jpg or png format) and click the 'Predict' button to perform prediction:")
    add_vertical_space(2)

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        if st.button('Predict'):
            # Pass the image to the prediction function
            prediction = predict_image(image)
            prediction*=100
            prediction = "{:.3f}".format(prediction)
            str = f"Child has a probablity of {prediction}% Jaundice"
            st.markdown(f"<h6 style='text-align: center; font-style: italic; color: #2B8C0C'>{str}</h6>", unsafe_allow_html=True)

if __name__ == "__main__":
    authenticated_menu()
    
    # back to home
    if st.button("Back to Home"):
        st.switch_page("Landing.py")
        
    main()