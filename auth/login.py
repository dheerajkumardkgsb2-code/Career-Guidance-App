import streamlit as st
import sqlite3

def validate_user(username, password):
    conn = sqlite3.connect('auth/users.db')
    cursor = conn.cursor()
    
    
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    
    conn.close()
    return user

def login():
    st.title("Log In")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Log In"):
        user = validate_user(username, password)
        if user:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"Welcome {username}!")
        else:
            st.error("Invalid username or password.")
