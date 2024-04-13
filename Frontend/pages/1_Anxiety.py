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
    st.header("Anxiety Disorder in Children")
    st.image("../assets/anxiety.webp")
    st.markdown(
        """
        Anxiety disorder in children refers to a range of mental health disorders characterized 
        by excessive worry, fear, and nervousness. It can affect a child's behavior, emotions, 
        and physical health, impacting their daily functioning and quality of life.
        """
    )
    st.write("---")
    
    st.subheader("Prevalence and Impact")

    st.markdown(
        """
        **Prevalence**: Anxiety disorders are among the most common mental health disorders 
        in children, with approximately 7% of children experiencing clinically significant 
        anxiety by the age of 12.

        **Impact**: Anxiety disorders can significantly impair a child's academic performance, 
        social relationships, and overall well-being. Untreated anxiety in childhood may 
        also increase the risk of developing other mental health disorders later in life.
        """
    )
    st.image('../assets/anxiety_prevalence.png', caption='Source: Medium',use_column_width=True)
    add_vertical_space(2)
    
    st.subheader("Symptoms")

    st.markdown(
        """
        Common symptoms of anxiety disorder in children may include:

        - Excessive worrying or fearfulness
        - Restlessness or irritability
        - Difficulty concentrating
        - Muscle tension or headaches
        - Fatigue or trouble sleeping
        - Avoidance of certain situations or activities
        
        It's essential to note that symptoms may vary depending on the type of anxiety disorder 
        and the individual child's experiences.
        """
    )
    add_vertical_space(2)
    
    st.subheader("Risk Factors")

    st.markdown(
        """
        **Genetics**: Children with a family history of anxiety disorders may be at a higher 
        risk of developing anxiety themselves.

        **Trauma or Stressful Life Events**: Traumatic experiences or significant life changes, 
        such as moving to a new school or parental divorce, can trigger or exacerbate anxiety 
        symptoms in children.

        **Temperament**: Children who are naturally more shy, sensitive, or perfectionistic 
        may be more prone to developing anxiety disorders.
        """
    )
    add_vertical_space(2)
    
    st.subheader("Treatment and Support")

    st.markdown(
        """
        Effective treatment for anxiety disorder in children often involves a combination of 
        therapy, medication (in some cases), and support from parents, teachers, and mental 
        health professionals. Cognitive-behavioral therapy (CBT) is one of the most common 
        and effective forms of therapy for managing childhood anxiety.
        """
    )
    add_vertical_space(2)
    st.markdown(
        """
        If you suspect that your child may be experiencing anxiety, it's essential to seek 
        professional help from a qualified mental health provider. Early intervention and 
        appropriate support can make a significant difference in managing and overcoming 
        anxiety disorder in children.
        """
    )


def main():
    render_overview()
    st.write("---")

if __name__ == "__main__":
    authenticated_menu()
    main()
    
    # back to home
    if st.button("Back to Home"):
        st.switch_page("Landing.py")
        