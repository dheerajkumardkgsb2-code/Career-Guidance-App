import streamlit as st
import os

def About_us():
    st.title("👨‍💻 About Us")

    st.markdown("""
        **Career Guidance Hub** is a data-driven platform designed to help students and professionals make informed career decisions.  
        Built with the aim of simplifying the career exploration process, the platform combines modern AI tools with career psychology and labor market insights.
    """)

    st.subheader("🌟 Founder")

    base_path = os.path.dirname(os.path.dirname(__file__))  
    image_path = os.path.join(base_path, "images")  

    st.image(os.path.join(image_path, "ashmit.jpg"), caption="Ashmit Rawat - Software Developer and Founder", width=300)

    st.subheader("💼 Mission")

    st.markdown("""
    Choosing the right career can be challenging in today’s fast-evolving world. Career Guidance Hub is developed to offer:
    
    - 🎯 **Personalized Recommendations** aligned with individual interests and aptitudes  
    - 📊 **Up-to-date Statistics** on job demand, skills, salaries, and education  
    - 🤖 **AI-powered Tools** including a smart survey and chatbot for dynamic support

    The goal is to provide accessible, reliable, and practical guidance that empowers users to navigate their career paths with clarity and confidence.
    """)

if __name__ == "__main__":
    About_us()
