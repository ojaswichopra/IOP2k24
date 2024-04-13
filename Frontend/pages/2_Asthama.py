import streamlit as st
import pickle
from streamlit_extras.add_vertical_space import add_vertical_space

model_path = "../Backend/asthma.sav"
model = pickle.load(open(model_path, 'rb'))

# sidebar page links
def authenticated_menu():
    st.sidebar.empty()
    st.sidebar.page_link("pages/1_Anxiety.py", label="Anxiety Disorder")
    st.sidebar.page_link("pages/2_Asthama.py", label="Asthma")
    st.sidebar.page_link("pages/3_CP.py", label="Cerebral Palsy")
    st.sidebar.page_link("pages/4_Down.py", label="Down Syndrome")
    st.sidebar.page_link("pages/5_Jaundice.py", label="Jaundice")
    st.sidebar.page_link("pages/6_Pneumonia.py", label="Pneumonia")
 
def age_to_range(age):
    age_0_9 = 1 if age >= 0 and age <= 9 else 0
    age_10_19 = 1 if age >= 10 and age <= 19 else 0
    age_20_24 = 1 if age >= 20 and age <= 24 else 0
    age_25_59 = 1 if age >= 25 and age <= 59 else 0
    age_60_plus = 1 if age >= 60 else 0
    
    return age_0_9, age_10_19, age_20_24, age_25_59, age_60_plus

def gender_types(gender):
    gender_male = 1 if gender.lower() == 'male' else 0
    gender_female = 1 if gender.lower() == 'female' else 0
    return gender_male, gender_female
   
def predict(Tiredness, Dry_Cough, Difficulty_in_Breathing, Sore_Throat, None_Sympton, Pains, Nasal_Congestion, Runny_Nose, None_Experiencing, Age, Gender):
    Tiredness=Tiredness
    Dry_Cough=Dry_Cough
    Difficulty_in_Breathing=Difficulty_in_Breathing
    Sore_Throat=Sore_Throat
    None_Sympton=None_Sympton
    Pains=Pains
    Nasal_Congestion=Nasal_Congestion
    Runny_Nose=Runny_Nose
    None_Experiencing=None_Experiencing
    age_0_9, age_10_19, age_20_24, age_25_59, age_60_plus = age_to_range(Age)
    gender_male,gender_female = gender_types(Gender)
    x = [[Tiredness,Dry_Cough,Difficulty_in_Breathing,Sore_Throat,None_Sympton,Pains,Nasal_Congestion,Runny_Nose,None_Experiencing,age_0_9, age_10_19, age_20_24, age_25_59, age_60_plus,gender_male,gender_female]]
    y = model.predict(x)
    return y

def render_predict():
    st.header("Predict Asthma")
    st.markdown("##### Choose symptoms that apply..")
    add_vertical_space(2)
    
    c1,c2,c3 = st.columns(3)
    with c1:
        tiredness = st.checkbox("Tiredness")
        dry_cough = st.checkbox("Dry Cough")
        difficulty_breathing = st.checkbox("Difficulty in Breathing")
    with c2:
        sore_throat = st.checkbox("Sore Throat")
        none_symptom = st.checkbox("None Symptom")
        pains = st.checkbox("Pains")
    with c3:
        nasal_congestion = st.checkbox("Nasal Congestion")
        runny_nose = st.checkbox("Runny Nose")
        none_experiencing = st.checkbox("None Experiencing")
    age = st.number_input("Age", min_value=0, step=1)
    gender = st.selectbox("Gender", ["Male", "Female"])
    add_vertical_space(2)
    
    if st.button("Submit"):
        y = predict(tiredness, dry_cough, difficulty_breathing, sore_throat, none_symptom, pains, nasal_congestion, runny_nose, none_experiencing, age, gender)
        if y:
            result = "Child has high changes of not being affected"
        else:
            result = "Child has high changes of being affected"
        st.markdown(f"<h6 style='text-align: center; font-style: italic; color: #2B8C0C'>{result}</h6>", unsafe_allow_html=True)
        
def render_overview():
    st.header("Asthma in Children")

    st.markdown(
        """
        Asthma is a chronic condition that affects the airways, causing inflammation and narrowing 
        of the air passages, which can lead to breathing difficulties. It is one of the most common 
        chronic diseases in childhood.
        """
    )
    st.write("---")
    
    st.subheader("Prevalence and Risk Factors")

    st.markdown(
        """
        **Prevalence**: Asthma affects approximately 5-10% of children worldwide and is one of 
        the leading causes of hospitalizations and emergency department visits among children.
        
        **Risk Factors**: Several factors contribute to the development of asthma in children, 
        including genetic predisposition, exposure to tobacco smoke, air pollution, allergens 
        (such as pollen, dust mites, and pet dander), respiratory infections, and certain 
        environmental factors.
        """
    )
    add_vertical_space(1)
    st.image('../assets/asthma_Prevalence.jpg', caption='Source: Frontiers',use_column_width=True)
    add_vertical_space(2)
    
    st.subheader("Symptoms")

    st.markdown(
        """
        Common symptoms of asthma in children include:
        
        - Wheezing
        - Shortness of breath
        - Chest tightness or pain
        - Coughing, especially at night or during exercise
        - Difficulty sleeping due to coughing or wheezing
        - Fatigue
        
        It's essential for parents and caregivers to recognize these symptoms and seek medical 
        attention for proper diagnosis and management of asthma in children.
        """
    )
    add_vertical_space(1)
    st.image('../assets/asthma_symptoms.jpg', caption='Source: MDPI',use_column_width=True)
    add_vertical_space(2)
    
    st.subheader("Management and Treatment")

    st.markdown(
        """
        Asthma management in children typically involves:
        
        - Avoiding triggers: Identifying and avoiding allergens and irritants that can trigger 
          asthma symptoms.
        - Medications: Depending on the severity and frequency of symptoms, children may require 
          medications such as inhaled corticosteroids, bronchodilators, or oral medications 
          to control inflammation and relieve symptoms.
        - Asthma action plan: Developing a written asthma action plan in collaboration with 
          healthcare providers to outline daily management, symptom monitoring, and steps to 
          take during asthma attacks or exacerbations.
        - Regular follow-up: Children with asthma should have regular follow-up visits with 
          healthcare providers to assess asthma control, adjust treatment as needed, and provide 
          education and support to families.
        """
    )
    
# Load saved training data
train_data_ageDistribution = ('../Backend/asthma_train_data_ageDistribution.png')
train_data_genderDistribution = ('../Backend/asthma_train_data_genderDistribution.png')
train_data_inputParams = ('../Backend/asthma_train_data_inputParams.png')
train_data_SeverityDistribution = ('../Backend/asthma_train_data_SeverityDsitribution.png')
train_data_symptomFreq = ('../Backend/asthma_train_data_symptomFreq.png')
cm = ('../Backend/asthma_cm.png')

def visualize_dataset_analysis():
    st.subheader("Dataset Analysis")
    st.image(train_data_inputParams,use_column_width=True)
    st.image(train_data_ageDistribution,use_column_width=True)
    st.image(train_data_genderDistribution,use_column_width=True)
    st.image(train_data_SeverityDistribution,use_column_width=True)
    st.image(train_data_symptomFreq,use_column_width=True)

# Function to visualize confusion matrix
def visualize_confusion_matrix():
    st.subheader("Confusion Matrix")
    st.image(cm,use_column_width=True)
    
def render_visualization():
    st.header("Our Model")
    add_vertical_space(2)
    visualize_dataset_analysis()
    visualize_confusion_matrix()
        
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
    