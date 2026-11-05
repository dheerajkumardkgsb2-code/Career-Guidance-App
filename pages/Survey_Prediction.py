# survey_prediction.py

import os
import json
import requests
import streamlit as st
from utils.survey_logic import calculate_score

# Set API Key environment variable
os.environ["HUGGINGFACE_API_KEY"] = ""  # Add your actual key here or use dotenv

# Styling for UI
st.markdown("""
    <style>
        .big-font { font-size: 18px !important; }
        .question-container { margin-bottom: 20px; }
        .question-container label { font-size: 16px; font-weight: bold; }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            font-weight: bold;
            padding: 10px 20px;
            border-radius: 5px;
            border: none;
        }
        .stButton > button:hover { background-color: #45a049; }
        .section-title {
            font-size: 22px;
            font-weight: bold;
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Function to call HuggingFace API
def get_career_recommendations(holland_code, subjects_marks):
    model = "HuggingFaceH4/zephyr-7b-beta"
    api_key = os.getenv("HUGGINGFACE_API_KEY")

    if not api_key:
        raise ValueError("HUGGINGFACE_API_KEY is missing!")

    subjects_text = "\n".join(f"- {subj}: {marks}" for subj, marks in subjects_marks.items())

    prompt = f"""
    Based on the Holland Code ({holland_code}) and high school subjects and marks:
    {subjects_text}

    Suggest 5 career options that best match my skills and personality type for India.
    For each career, provide:
    - **Job Title**
    - **Brief Job Description**
    - **Future Job Demand in India** (Growing, Stable, Declining)
    - **Required Education in India** (Degree, Certification, etc.)
    - **Estimated Average Salary in INR**
    - **Skills Required**
    - **Any Additional Notes**

    Format the response in a structured way, using bullet points for clarity.
    """

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 1000,
            "temperature": 0.7,
            "top_p": 0.9,
            "repetition_penalty": 1.2
        }
    }

    try:
        response = requests.post(
            f"https://api-inference.huggingface.co/models/{model}",
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        result = response.json()

        if isinstance(result, list) and result:
            return result[0].get("generated_text", "No meaningful response generated.")
        else:
            return "No response from the model or unexpected response format."

    except requests.exceptions.RequestException as e:
        return f"An error occurred while connecting to the API: {str(e)}"
    except json.JSONDecodeError:
        return "Failed to decode the response from the API."

# Streamlit form logic
def survey_form():
    st.title("📝 Career Survey")
    st.markdown("""**Welcome to the Career Survey!**  
    This survey will help us assess your strengths, preferences, and interests to provide personalized career recommendations.
    Please answer the following questions honestly and thoughtfully.""", unsafe_allow_html=True)

    st.markdown("<div class='section-title'>🔍 Personal Preferences</div>", unsafe_allow_html=True)
    q1 = st.radio("Do you enjoy working with numbers and data?", ["Yes", "No"], key="q1_survey")
    q2 = st.radio("Do you like helping others in need?", ["Yes", "No"], key="q2_survey")
    q3 = st.radio("Do you prefer creative tasks over analytical ones?", ["Yes", "No"], key="q3_survey")
    q4 = st.radio("Are you interested in technology and innovation?", ["Yes", "No"], key="q4_survey")
    q5 = st.radio("Do you enjoy problem-solving?", ["Yes", "No"], key="q5_survey")
    q6 = st.radio("Do you like to work independently?", ["Yes", "No"], key="q6_survey")

    st.markdown("<div class='section-title'>🧠 Skills & Aptitude</div>", unsafe_allow_html=True)
    q7 = st.radio("Do you prefer leadership roles?", ["Yes", "No"], key="q7_survey")
    q8 = st.radio("Do you prefer to work in teams?", ["Yes", "No"], key="q8_survey")
    q9 = st.radio("Are you interested in arts, music, or design?", ["Yes", "No"], key="q9_survey")
    q10 = st.radio("Do you like working with your hands or machinery?", ["Yes", "No"], key="q10_survey")
    q11 = st.radio("Do you have strong mathematical and logical skills?", ["Yes", "No"], key="q11_survey")
    q12 = st.radio("Are you comfortable working with complex software and systems?", ["Yes", "No"], key="q12_survey")

    st.markdown("<div class='section-title'>🌱 Additional Preferences</div>", unsafe_allow_html=True)
    q13 = st.radio("Are you good at communicating ideas to others?", ["Yes", "No"], key="q13_survey")
    q14 = st.radio("Do you enjoy learning new technologies?", ["Yes", "No"], key="q14_survey")
    q15 = st.radio("Do you like performing research and analysis?", ["Yes", "No"], key="q15_survey")
    q16 = st.radio("Are you detail-oriented and meticulous?", ["Yes", "No"], key="q16_survey")
    q17 = st.radio("Do you have strong organizational skills?", ["Yes", "No"], key="q17_survey")
    q18 = st.radio("Do you enjoy teaching or mentoring others?", ["Yes", "No"], key="q18_survey")

    st.markdown("<div class='section-title'>🌍 Broader Interests</div>", unsafe_allow_html=True)
    q19 = st.radio("Are you interested in global or environmental issues?", ["Yes", "No"], key="q19_survey")
    q20 = st.radio("Do you enjoy writing or content creation?", ["Yes", "No"], key="q20_survey")

    st.markdown("<div class='section-title'>📚 Academic Background</div>", unsafe_allow_html=True)
    math_marks = st.number_input("Math Marks", min_value=0, max_value=100, value=80, key="math_input")
    science_marks = st.number_input("Science Marks", min_value=0, max_value=100, value=85, key="science_input")
    english_marks = st.number_input("English Marks", min_value=0, max_value=100, value=75, key="english_input")

    if st.button("Submit Survey", key="submit_survey_btn"):
        answers = [
            q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,
            q11, q12, q13, q14, q15, q16, q17, q18, q19, q20
        ]
        score = calculate_score(answers)
        st.session_state['survey_score'] = score
        st.success("Survey submitted successfully!")
        st.markdown("Fetching personalized recommendations...")

        try:
            holland_code = "RIASEC"  # Static placeholder, can be dynamic later
            subjects_marks = {
                "Math": math_marks,
                "Science": science_marks,
                "English": english_marks
            }

            career_recommendations = get_career_recommendations(holland_code, subjects_marks)
            st.markdown("### 🎯 Career Recommendations:")
            st.write(career_recommendations)

        except Exception as e:
            st.error(f"Failed to get recommendations: {str(e)}")

# Entry point
if __name__ == "__main__":
    survey_form()
