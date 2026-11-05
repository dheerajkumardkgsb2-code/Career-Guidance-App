# 🎓 Career Guidance Portal

An intelligent, AI-powered web application that helps students and professionals make informed career choices by providing personalized recommendations, skill gap analysis, and access to a smart chatbot.

---

## 🧠 Overview

The Career Guidance Portal leverages AI and predictive analytics to guide users toward suitable career paths based on their strengths, interests, and aspirations. It bridges the gap left by traditional career counseling with dynamic tools like:

- AI-driven career recommendation engine
- Interactive form-based survey and aptitude analysis
- Real-time chatbot assistance
- Personalized growth feedback

---

## 🚀 Features

- 🔐 **Authentication System**  
  Secure login and signup using SQLite for user data management.

- 📝 **Career Survey & Assessment**  
  Users answer tailored questions to evaluate their preferences and strengths.

- 🤖 **AI-Based Career Recommendations**  
  Generates career suggestions using Hugging Face NLP models (e.g., Zephyr, LLaMA).

- 📊 **Career Statistics**  
  Provides insights on job demand, required education, average salaries, and future growth.

- 💬 **Chatbot Integration**  
  Embedded Chatbase chatbot helps users interact conversationally with the platform.

- 📁 **Modular Architecture**  
  Clean separation of UI, logic, database, and API integrations.

---

## 🏗️ System Architecture

Follows a **3-tier architecture**:

1. **Presentation Layer** (Frontend):  
   Developed using `Streamlit` for clean, responsive UI.

2. **Application Layer** (Logic):  
   Python-based backend processes user input, session state, and routing.

3. **Data Layer** (Storage):  
   Uses `SQLite` (`users.db`) for storing user credentials and responses.

---

## 🛠️ Tech Stack

| Layer             | Technology               |
|------------------|--------------------------|
| Frontend         | Streamlit                |
| Backend          | Python                   |
| Database         | SQLite                   |
| AI Integration   | Hugging Face Transformers |
| Chatbot          | Chatbase                 |

---

