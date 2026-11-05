import streamlit as st
import sqlite3
from auth.auth_db import create_db  # Ensure the database and table are created

# Ensure the database and table are created before inserting data
create_db()

# Function to register new user
def register_user(username, password):
    conn = sqlite3.connect('auth/users.db')
    cursor = conn.cursor()
    
    # Insert new user into the database
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    
    conn.commit()
    conn.close()

# Function to authenticate a user
def login_user(username, password):
    conn = sqlite3.connect('auth/users.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    
    conn.close()
    
    return user  


def signup():
    st.title("Sign Up")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    
    if st.button("Sign Up"):
        if password == confirm_password:
            try:
                register_user(username, password)
                st.success("You have successfully signed up! You can now log in.")
            except sqlite3.IntegrityError:
                st.error("Username already exists.")
        else:
            st.error("Passwords do not match.")

# Login page
def login():
    st.title("Log In")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Log In"):
        user = login_user(username, password)
        
        if user:
            st.session_state.logged_in = True
            st.session_state.username = username  
            st.success(f"Welcome, {username}!")
            st.session_state.page = "Home" 
            st.rerun()  
        else:
            st.error("Invalid username or password.")


def logout():
    st.session_state.logged_in = False
    st.session_state.username = None
    st.session_state.page = None
    st.rerun() 


def home():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = None
    if 'page' not in st.session_state:
        st.session_state.page = None
    
    if not st.session_state.logged_in:
        redirect_login()
    else:
        
        st.title(f"Welcome {st.session_state.username}")
        page = st.sidebar.radio("Go to", ("Home", "About Us", "Testimonials", "Statistics", "Survey Form", "Prediction", "Chatbot"))
        if page == "Home":
            st.write("Welcome to Career Guidance App!")
        elif page == "Survey Form":
            st.write("Survey Form page")
        
        
        if st.sidebar.button("Logout"):
            logout()


def redirect_login():
    st.title("🔐 Career Guidance App Login")
    option = st.radio("Choose an option:", ["Login", "Sign Up"], horizontal=True)
    if option == "Login":
        login()
    else:
        signup()


home()
