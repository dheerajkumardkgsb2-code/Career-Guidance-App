# 🧠 AI-Powered Career Guidance Portal

An intelligent AI-powered web application that helps students and professionals make informed career decisions through personalized recommendations, skill gap analysis, and real-time career guidance. The platform leverages Artificial Intelligence and predictive analytics to analyze user interests, strengths, and career aspirations, providing tailored career suggestions and valuable industry insights.

---

## 📌 Overview

Traditional career counseling often lacks personalization and accessibility. The AI-Powered Career Guidance Portal bridges this gap by offering an interactive platform where users can assess their interests, receive AI-generated career recommendations, identify skill gaps, and explore career opportunities. An integrated AI chatbot further enhances the experience by answering career-related queries and providing instant guidance.

---

## ✨ Features

- 🔐 **Secure Authentication**
  - User registration and login using SQLite.
  - Secure storage of user credentials and assessment history.

- 📝 **Career Assessment**
  - Interactive questionnaires to evaluate interests, skills, strengths, and career preferences.

- 🤖 **AI-Based Career Recommendations**
  - Personalized career suggestions generated using Hugging Face Transformer models.

- 📊 **Career Insights**
  - Displays information including job demand, salary trends, educational requirements, future growth, and required skills.

- 📈 **Skill Gap Analysis**
  - Identifies missing skills and provides recommendations for improvement.

- 💬 **AI Chatbot**
  - Chatbase-powered chatbot for answering career-related questions and offering real-time assistance.

- 📱 **Responsive Interface**
  - Clean and user-friendly interface built using Streamlit.

---

## 🏗️ System Architecture

The application follows a **3-Tier Architecture**:

### Presentation Layer
- Streamlit
- Interactive and responsive user interface

### Application Layer
- Python
- Handles authentication, AI recommendation logic, user sessions, and business logic

### Data Layer
- SQLite Database
- Stores user credentials, assessment responses, and application data

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend | Streamlit |
| Backend | Python |
| Database | SQLite |
| AI Models | Hugging Face Transformers |
| Chatbot | Chatbase |

---

## 📂 Project Structure

```text
Career-Guidance-Portal/
│── app.py
│── users.db
│── requirements.txt
│── README.md
│── assets/
│── pages/
│── models/
│── utils/
│── chatbot/
└── data/
```

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Career-Guidance-Portal.git
cd Career-Guidance-Portal
```

### Create Virtual Environment (Optional)

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## 🎯 How It Works

1. Register or log in to the platform.
2. Complete the career assessment questionnaire.
3. AI analyzes your responses and interests.
4. Receive personalized career recommendations.
5. View career statistics and skill requirements.
6. Identify skill gaps and recommended improvements.
7. Interact with the AI chatbot for additional career guidance.

---

## 🌟 Future Enhancements

- Resume Analyzer with ATS scoring
- Personality and Aptitude Testing
- Learning Roadmap Generation
- Job & Internship Recommendations
- Multi-language Support
- Career Progress Dashboard
- Integration with LinkedIn and Online Learning Platforms

---

## 📄 License

This project is developed for educational and learning purposes. You are free to use, modify, and extend it for personal or academic projects.
