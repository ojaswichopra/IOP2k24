import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.add_vertical_space import add_vertical_space
import streamlit_shadcn_ui as ui

title = "TinyTot Diagnosis"
page_icon = "🩺"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"
st.set_page_config(page_title=title, page_icon=page_icon, layout=layout)
selection = None

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

    st.markdown(
        """
    <style>
        [data-testid="collapsedControl"] {
            display: none
        }
    </style>
    """,
        unsafe_allow_html=True,
    )

    # Title and Introduction
    st.markdown("<h1 style='text-align: center; color: #2B8C0C'>Welcome to TinyTot Diagnosis</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Unveiling the Future of Pediatric Healthcare!</h3>", unsafe_allow_html=True)
    
    # Images Section
    st.image('Landing.jpg', caption='TinyTot Diagnosis: Empowering Care, Transforming Lives')

    # Story Section
    st.markdown("<h2 style='text-align: center; color: #2B8C0C'>Our Story</h2>",unsafe_allow_html=True)
    ui.metric_card(title='Every child deserves a healthy and happy start in life. Inspired by this belief, we embarked on a journey to harness the power of artificial intelligence for the benefit of pediatric healthcare. Our interdisciplinary team of data scientists, pediatricians, and caregivers came together with a shared vision: to create a world where every child\'s health is safeguarded from the very beginning.', content="",description="") 

    # Power of Prediction
    st.markdown("<h2 style='text-align: center; color: #2B8C0C'>The Power of Prediction</h2>",unsafe_allow_html=True)
    ui.metric_card(title='Imagine being able to anticipate health challenges before they even manifest. With our predictive models, we\'re turning this vision into reality. From childhood anxiety disorder to pneumonia, jaundice to asthma, cerebral palsy to Down syndrome and autism disorder, our models analyze a wealth of data to identify potential risks early on..', content="",description="") 

    # Insights Section
    st.markdown("<h2 style='text-align: center; color: #2B8C0C'>Insights That Matter</h2>",unsafe_allow_html=True)
    ui.metric_card(title='It\'s not just about prediction—it\'s about understanding. Our models don\'t just flag risks; they provide deep insights into each condition, helping caregivers make informed decisions about treatment and management. Whether it\'s uncovering patterns in symptom progression, identifying genetic markers, or recommending personalized interventions, TinyTot Diagnosis is dedicated to equipping caregivers with the knowledge they need to provide the best possible care for every child.', content="",description="") 

    # Empowering Caregivers
    st.markdown("<h2 style='text-align: center; color: #2B8C0C'>Empowering Caregivers, Transforming Lives</h2>",unsafe_allow_html=True)
    ui.metric_card(title='At the heart of TinyTot Diagnosis is a commitment to empowerment. We believe that by arming caregivers with powerful tools and knowledge, we can make a tangible difference in the lives of children and families around the world. Our platform is designed to be intuitive, accessible, and user-friendly, ensuring that caregivers can seamlessly integrate our insights into their daily practice, making informed decisions that impact lives for the better.', content="",description="") 

    # Join Us Section
    st.markdown("<h2 style='text-align: center; color: #2B8C0C'>Join Us in Shaping the Future</h2>",unsafe_allow_html=True)
    ui.metric_card(title='The journey towards a healthier future for children begins with you. Whether you\'re a caregiver, a healthcare professional, or simply someone passionate about pediatric health, we invite you to join us in our mission. Explore our platform, engage with our community, and together, let\'s shape a world where every child has the opportunity to thrive.', content="",description="") 

    # Footer
    st.markdown("<h6 style='text-align: center; font-style: italic; color: #2B8C0C'>TinyTot Diagnosis is a project aimed at improving pediatric healthcare through machine learning and data-driven insights.</h6>",unsafe_allow_html=True)

    
if __name__ == "__main__":
    authenticated_menu()
    main()