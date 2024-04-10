import streamlit as st
import pickle
from streamlit_extras.add_vertical_space import add_vertical_space
import streamlit_shadcn_ui as ui

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
    model_path = "../Backend/asthma.sav"
    model = pickle.load(open(model_path, 'rb'))
    x = [[Tiredness,Dry_Cough,Difficulty_in_Breathing,Sore_Throat,None_Sympton,Pains,Nasal_Congestion,Runny_Nose,None_Experiencing,age_0_9, age_10_19, age_20_24, age_25_59, age_60_plus,gender_male,gender_female]]
    y = model.predict(x)
    return y

def main():
    st.title("Predict Asthma")
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
    col1,col2 = st.columns(2)
    add_vertical_space(2)
    
    if col1.button("Submit"):
        y = predict(tiredness, dry_cough, difficulty_breathing, sore_throat, none_symptom, pains, nasal_congestion, runny_nose, none_experiencing, age, gender)
        if y:
            result = "Child has high changes of not being affected"
        else:
            result = "Child has high changes of being affected"
        st.markdown(f"<h6 style='text-align: center; font-style: italic; color: #2B8C0C'>{result}</h6>", unsafe_allow_html=True)
        
        
    # back to home
    if col2.button("Back to Home"):
        st.switch_page("Landing.py")

if __name__ == "__main__":
    authenticated_menu()
        
    main()
    
    