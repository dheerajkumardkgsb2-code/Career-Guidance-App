import streamlit as st


st.set_page_config(page_title="Career Guidance App", layout="wide")


from auth.auth_utils import redirect_login, logout
from auth.auth_db import create_db
import pages.About_Us
import pages.Testimonials
import pages.Statistics
import pages.Survey_Prediction
import pages.Chatbot


create_db()


if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = None

def home():
    
    if not st.session_state.logged_in:
        redirect_login()  
    else:
        st.sidebar.title(f"Welcome, {st.session_state.username} 👋")
        
        
        page = st.sidebar.radio("Go to", (
            "Home", "About Us", "Testimonials", "Statistics",
            "Survey Form And Prediction", "Chatbot"
        ))

        st.sidebar.markdown("---")
        
        
        if st.sidebar.button("🚪 Logout"):
            logout()  
        else:
            
            if page == "Home":
                st.title("Welcome to the Career Guidance App 🎓")
                st.write("Use the sidebar to explore features.")
            elif page == "About Us":
                pages.About_Us.About_us()  
            elif page == "Testimonials":
                pages.Testimonials.testimonials()  
            elif page == "Statistics":
                pages.Statistics.statistics()  
            elif page == "Survey Form And Prediction":
                pages.Survey_Prediction.survey_form()  
            elif page == "Chatbot":
                pages.Chatbot.chatbot()  

if __name__ == "__main__":
    home()
