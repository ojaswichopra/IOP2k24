import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from PIL import Image
import pickle
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
    
model_path = "../Backend/pnemonia.sav"
model = pickle.load(open(model_path, 'rb'))

# Load model architecture
model_architecture = ('../Backend/pnemonia_model_architecture.png')
    
# Load saved training data
train_data = ('../Backend/pnemonia_train_data.png')

# Load saved model training history
history_accuracy = ('../Backend/pnemonia_history_accuracy.png')
history_loss = ('../Backend/pnemonia_history_loss.png')

# Load saved confusion matrix
cm = ('../Backend/pnemonia_cm.png')

# Function to render the visualization page
def render_visualization():
    st.header("Our Model")
    add_vertical_space(2)
    visualize_model_architecture(model)
    visualize_dataset_analysis()
    visualize_training_history()
    visualize_confusion_matrix()

# Function to visualize model architecture
def visualize_model_architecture(model):
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

def render_overview():
    st.header("Pneumonia in Children")

    st.markdown(
        """
        Pneumonia is an infection that inflames the air sacs in one or both lungs. 
        It can be caused by bacteria, viruses, or fungi. In children, pneumonia can be particularly 
        concerning due to their developing immune systems and smaller airways, making them more 
        vulnerable to respiratory infections.
        """
    )
    st.write("---")
    
    st.subheader("Prevalence and Risk in Infants")

    st.markdown(
        """
        **Prevalence**: Pneumonia is a leading cause of death in children worldwide, 
        accounting for approximately 15% of all deaths in children under the age of 5.
        
        **Risks in Infants**: Infants, especially those under the age of 1, are at higher 
        risk of developing pneumonia due to their immature immune systems and limited 
        exposure to pathogens, making them more susceptible to infections.
        """
    )
    st.image('../assets/Pneumonia_risk.png', caption='Source: Research Gate',use_column_width=True)
    add_vertical_space(2)
    
    st.subheader("Statistics")

    st.markdown(
        """
        - According to the World Health Organization (WHO), pneumonia kills an estimated 
          2.5 million children under the age of 5 every year, with the majority of deaths 
          occurring in developing countries.
        - In the United States, pneumonia is one of the most common reasons for hospitalizations 
          among children, particularly infants and young children.
        """
    )
    st.image('../assets/pnemonia_stats.png', caption='Source: Journal of Global Health',use_column_width=True)
    add_vertical_space(2)
    
    st.subheader("Symptoms")

    st.markdown(
        """
        Common symptoms of pneumonia in children include:
        
        - Cough, which may produce phlegm
        - Fever, often accompanied by chills
        - Rapid or difficult breathing
        - Chest pain, especially when breathing deeply
        - Fatigue or lethargy
        - Loss of appetite
        
        If your child exhibits any of these symptoms, especially if they are under the age of 5, 
        it is essential to seek medical attention promptly.
        """
    )
    st.image('../assets/pnemonia_symptoms.png', caption='Source: PLOS ONE',use_column_width=True)
    add_vertical_space(2)
    
    st.markdown(
        """
        For more detailed information about pneumonia in children and its symptoms, please refer 
        to reputable sources such as the Centers for Disease Control and Prevention (CDC) or the 
        American Academy of Pediatrics (AAP).
        """
    )   

def predict_image(image):
    img_tensor = tf.convert_to_tensor(image)
    img_tensor = tf.expand_dims(img_tensor, axis=-1)
    if img_tensor.shape[-1] != 3: 
        img_tensor = tf.image.grayscale_to_rgb(img_tensor) 
    img_tensor = tf.image.resize(img_tensor, size =(120,120))
    img_tensor = tf.expand_dims(img_tensor, axis=0)
    print(img_tensor.shape)
    img = img_tensor/255.0
    y = model.predict(img)
    return y

def render_predict():
    st.header("Predict Pneumonia")
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
            prediction = round(prediction[0][0],3)
            str = f"Child has a probablity of {prediction}% Jaundice"
            st.markdown(f"<h6 style='text-align: center; font-style: italic; color: #2B8C0C'>{str}</h6>", unsafe_allow_html=True)
    
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
        
    