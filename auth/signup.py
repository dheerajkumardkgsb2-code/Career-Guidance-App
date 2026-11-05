import streamlit as st
import sqlite3
from auth.auth_db import create_db  

create_db()

def register_user(username, password):
    conn = sqlite3.connect('auth/users.db')
    cursor = conn.cursor()
    
    
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    
    conn.commit()
    conn.close()

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
            st.experimental_rerun()  
        else:
            st.error("Invalid username or password.")
