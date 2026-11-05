import streamlit as st

def show_career_form():
    st.title("📋 Career Preference Form")

    name = st.text_input("Your Name")
    age = st.slider("Your Age", 15, 40, 20)
    interests = st.multiselect("Your Interests", ["Science", "Arts", "Technology", "Business", "Medicine", "Design"])
    skills = st.multiselect("Your Skills", ["Analytical", "Creative", "Communication", "Technical", "Leadership"])
    goal = st.text_area("Your Career Goal")

    if st.button("Submit"):
        st.success("Form Submitted!")
        st.session_state['form_data'] = {
            "name": name,
            "age": age,
            "interests": interests,
            "skills": skills,
            "goal": goal
        }
