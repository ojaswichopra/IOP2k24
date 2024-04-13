import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from PIL import Image
import pickle
import tensorflow as tf
import numpy as np

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
    model_path = "../Backend/jaundice.sav"
    model = pickle.load(open(model_path, 'rb'))
    img_tensor = tf.convert_to_tensor(image)
    if img_tensor.shape[-1] != 3: 
        img_tensor = tf.image.grayscale_to_rgb(img_tensor)
    img_tensor = tf.image.resize(img_tensor, size =(180,180))
    img_tensor = tf.expand_dims(img_tensor, axis=0)
    img = img_tensor/255.0
    y = model.predict(img)
    y = np.argmax(y)
    return y

def render_predict():    
    st.header("Predict Jaundice")
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
            if not prediction:
                str = f"Child has a high probablity of Jaundice"
            else:
                str = f"Child has a low probablity of Jaundice"
            st.markdown(f"<h6 style='text-align: center; font-style: italic; color: #2B8C0C'>{str}</h6>", unsafe_allow_html=True)
            

def render_overview():
    st.header("Jaundice in Children")
    st.image('../assets/jaundice.png',use_column_width=True)
    st.markdown(
        """
        Jaundice is a condition characterized by the yellowing of the skin and eyes. 
        It occurs when there is an excess of bilirubin in the blood, a yellow pigment 
        that is formed by the breakdown of red blood cells. While jaundice is common 
        in newborns, it can also affect older children.
        """
    )
    st.write("---")
    
    st.subheader("Prevalence and Risk in Infants")

    st.markdown(
        """
        **Prevalence**: Jaundice is a common condition in newborns, affecting approximately 
        60% of full-term babies and 80% of premature babies within the first week of life.
        
        **Risks in Infants**: Premature infants are at higher risk of developing jaundice 
        due to their immature liver function, which may not be able to process bilirubin 
        effectively. Additionally, certain factors such as breastfeeding, blood type 
        incompatibility, and infections can increase the risk of jaundice in newborns.
        """
    )
    add_vertical_space(1)
    st.image('../assets/jaundice_prevalence.png', caption='Source: MDPI',use_column_width=True)
    add_vertical_space(2)
    
    st.subheader("Symptoms")

    st.markdown(
        """
        Common symptoms of jaundice in children include:
        
        - Yellowing of the skin and eyes
        - Pale-colored stools
        - Dark-colored urine
        - Irritability or fussiness
        - Poor feeding or difficulty breastfeeding
        
        If your child exhibits any of these symptoms, especially in the first week of life, 
        it is essential to seek medical attention promptly.
        """
    )
    add_vertical_space(2)
    
    st.subheader("Complications")

    st.markdown(
        """
        While jaundice is usually harmless and resolves on its own, in some cases, it 
        can lead to complications such as:
        
        - Kernicterus: A rare but serious condition characterized by the deposition of 
          bilirubin in the brain, which can cause neurological problems such as cerebral 
          palsy, hearing loss, and developmental delays.
        - Acute bilirubin encephalopathy: A condition that occurs when bilirubin levels 
          rise rapidly and cause brain damage, leading to symptoms such as lethargy, poor 
          feeding, and seizures.
        
        These complications are more common in infants with severe jaundice or underlying 
        medical conditions and require immediate medical attention.
        """
    )
    add_vertical_space(1)
    st.image('../assets/jaundice_complications.png', caption='Source: Research Gate',use_column_width=True)
    add_vertical_space(2)
    
    st.markdown(
        """
        For more detailed information about jaundice in children and its management, 
        please refer to reputable sources such as the American Academy of Pediatrics (AAP) 
        or consult with a pediatrician.
        """
    )
       
# Load model architecture
model_architecture = ('../Backend/jaundice_model_architecture.png')
    
# Load saved training data
train_data = ('../Backend/jaundice_train_data.png')

# Load saved model training history
history_accuracy = ('../Backend/jaundice_history_accuracy.png')
history_loss = ('../Backend/jaundice_history_loss.png')

# Load saved confusion matrix
cm = ('../Backend/jaundice_cm.png')

def render_visualization():
    st.header("Our Model")
    add_vertical_space(2)
    visualize_model_architecture()
    visualize_dataset_analysis()
    visualize_training_history()
    visualize_confusion_matrix()
    
# Function to visualize model architecture
def visualize_model_architecture():
    st.subheader("Model Architecture")
    st.image(model_architecture,use_column_width=True)

# Function to visualize dataset analysis
def visualize_dataset_analysis():
    st.subheader("Dataset Analysis")
    st.image(train_data,use_column_width=True)

# Function to visualize model training history
def visualize_training_history():
    st.subheader("Training and Validation Metrics")
    st.image(history_accuracy,use_column_width=True)
    st.image(history_loss,use_column_width=True)

# Function to visualize confusion matrix
def visualize_confusion_matrix():
    st.subheader("Confusion Matrix")
    st.image(cm,use_column_width=True)

def main():
    render_overview()
    st.write("---")
    render_visualization()
    st.write("---")
    render_predict()
    
if __name__ == "__main__":
    authenticated_menu()
    main()
    
    # back to home
    if st.button("Back to Home"):
        st.switch_page("Landing.py")
        