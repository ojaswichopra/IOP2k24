import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

# sidebar page links
def authenticated_menu():
    st.sidebar.empty()
    st.sidebar.page_link("pages/1_Anxiety.py", label="Anxiety Disorder")
    st.sidebar.page_link("pages/2_Asthama.py", label="Asthma")
    st.sidebar.page_link("pages/3_CP.py", label="Cerebral Palsy")
    st.sidebar.page_link("pages/4_Down.py", label="Down Syndrome")
    st.sidebar.page_link("pages/5_Jaundice.py", label="Jaundice")
    st.sidebar.page_link("pages/6_Pneumonia.py", label="Pneumonia")
    
def render_overview():
    st.header("Cerebral Palsy in Children")
    st.image('../assets/cp.webp')
    st.markdown(
        """
        Cerebral Palsy (CP) is a group of disorders that affect movement and muscle coordination. 
        It is caused by damage to the developing brain, usually before birth. CP can vary in severity, 
        and individuals with CP may have difficulty with muscle control, coordination, balance, and posture.
        """
    )
    st.write("---")
    
    st.subheader("Prevalence and Impact")

    st.markdown(
        """
        **Prevalence**: Cerebral Palsy is one of the most common motor disabilities in childhood, 
        affecting approximately 2 to 3 children per 1,000 live births globally.
        
        **Impact**: CP can have a significant impact on a child's life, affecting their ability to 
        move, communicate, play, learn, and perform daily activities independently.
        """
    )
    st.image('../assets/cerebral_palsy_prevalence.jpeg', caption='Source: Frontiers', use_column_width=True)
    add_vertical_space(2)
    
    st.subheader("Causes and Risk Factors")

    st.markdown(
        """
        **Causes**: The exact cause of CP is often unknown, but it is believed to result from 
        abnormal brain development or damage to the brain before, during, or shortly after birth.
        
        **Risk Factors**: Some factors that may increase the risk of CP include premature birth, 
        low birth weight, multiple births (e.g., twins, triplets), maternal infections during pregnancy, 
        and complications during birth.
        """
    )
    add_vertical_space(2)
    
    st.subheader("Symptoms and Diagnosis")

    st.markdown(
        """
        Common symptoms of Cerebral Palsy in children include:
        
        - Muscle stiffness or rigidity
        - Involuntary movements or tremors
        - Delayed motor milestones (e.g., crawling, walking)
        - Difficulty with fine motor skills (e.g., grasping objects)
        - Balance and coordination problems
        - Speech and language difficulties
        
        Diagnosis of CP typically involves a comprehensive evaluation of a child's medical history, 
        developmental milestones, physical examination, and neuroimaging tests (e.g., MRI, CT scan).
        """
    )
    add_vertical_space(1)
    st.image('../assets/cerebral_palsy_symptoms.jpeg', caption='Source: UCSF Department of Pediatrics', use_column_width=True)
    add_vertical_space(2)
    
    st.markdown(
        """
        For more detailed information about Cerebral Palsy in children, its causes, symptoms, 
        diagnosis, and management, please consult healthcare professionals and reputable sources 
        such as the Centers for Disease Control and Prevention (CDC) or the Cerebral Palsy Alliance.
        """
    )   
    
cm = ('../Backend/CP/CP_cm.png')
train_data = ('../Backend/CP/CP_train_data.png')

def visualize_confusion_matrix():
    st.subheader("Confusion Matrix")
    st.image(cm,use_column_width=True)
    
def visualize_train_data():
    st.subheader("Training Data")
    st.image(train_data,use_column_width=True)
    
def render_visualization():
    st.header("Our Model")
    add_vertical_space(2)
    visualize_train_data()
    visualize_confusion_matrix()

def main():
    render_overview()
    st.write("---")
    render_visualization()
    
if __name__ == "__main__":
    authenticated_menu()
    main()
    # back to home
    if st.button("Back to Home"):
        st.switch_page("Landing.py")
        
    