import streamlit as st
import pandas as pd
import altair as alt

def statistics():
    st.title("📈 Career Insights Dashboard")

    
    data = {
        "Career": [
            "Software Engineer", "Data Scientist", "Doctor", "UX Designer", "Teacher",
            "Mechanical Engineer", "Civil Engineer", "Pharmacist", "Lawyer", "Accountant",
            "AI Engineer", "Psychologist", "Digital Marketer", "Biotechnologist", "Architect"
        ],
        "Avg Salary (INR LPA)": [12, 15, 10, 8, 5, 6, 6.5, 5.5, 8, 6, 18, 7, 6, 7.5, 8],
        "Demand Score": [90, 95, 80, 75, 85, 72, 68, 65, 82, 70, 96, 78, 83, 74, 79]
    }

    df = pd.DataFrame(data).sort_values(by="Demand Score", ascending=True)

    col1, col2 = st.columns([2, 1])

    
    with col1:
        st.subheader("💰 Average Salary by Career (INR LPA)")

        bar_salary = alt.Chart(df).mark_bar().encode(
            y=alt.Y('Career:N', sort='-x', title="Career"),
            x=alt.X('Avg Salary (INR LPA):Q', title="Average Salary (LPA)"),
            color=alt.Color('Career:N', legend=None),
            tooltip=['Career', 'Avg Salary (INR LPA)']
        ).properties(height=500)

        st.altair_chart(bar_salary, use_container_width=True)

        st.subheader("📈 Market Demand by Career")

        line_demand = alt.Chart(df).mark_line(point=alt.OverlayMarkDef(filled=True, fill="black")).encode(
            x=alt.X('Career:N', sort=df['Career'].tolist(), title="Career"),
            y=alt.Y('Demand Score:Q', title="Demand Score (0-100)"),
            tooltip=['Career', 'Demand Score'],
            color=alt.value("#1f77b4")
        ).properties(height=400)

        st.altair_chart(line_demand, use_container_width=True)

    
    with col2:
        st.subheader("🧾 About This Data")
        st.markdown(""" 
        This dashboard presents up-to-date salary and demand information for various career paths in India.

        *💡 Key Insights:*
        - 💼 *AI Engineer* & *Data Scientist* top the list in salary and demand.
        - 👨‍⚕ *Doctor, Lawyer, and Psychologist* remain prestigious and relevant.
        - 🛠 Engineering fields are steady in demand with moderate pay.
        - 🎨 Creative fields like *UX Design* and *Architecture* are gaining traction.
        - 📢 *Digital Marketing* is emerging as a strong option in the tech-business crossover space.

        *ℹ Notes:*
        - Salaries represent average fresh-to-mid-level income in INR Lakhs Per Annum (LPA).
        - Demand score is based on job market trends, skill scarcity, and hiring patterns (0–100 scale).
        """)
        st.markdown("📍 Use this data as a guide to align your interests, skills, and career goals.")

    
    st.subheader("🔍 Explore Career Details")

   
    career_option = st.radio(
        "Select a career to learn more:",
        ("Software Engineer", "Data Scientist", "Doctor", "UX Designer", "Teacher", 
         "Mechanical Engineer", "Civil Engineer", "Pharmacist", "Lawyer", "Accountant", 
         "AI Engineer", "Psychologist", "Digital Marketer", "Biotechnologist", "Architect")
    )

    
    if career_option == "Software Engineer":
        st.markdown(""" 
        *Role:* Design, develop, and maintain software systems.

        *Required Skills:* Programming (Java, Python, C++), problem-solving, algorithm design.

        *Education Needed:* Bachelor's in Computer Science or related field.

        *Salary Range:* ₹8-12 LPA.

        *Demand:* High, especially in tech firms and startups.
        """)

    elif career_option == "Data Scientist":
        st.markdown(""" 
        *Role:* Analyze and interpret complex data to help organizations make data-driven decisions.

        *Required Skills:* Data analysis, machine learning, Python, SQL, R.

        *Education Needed:* Bachelor's/Master's in Computer Science, Statistics, or related field.

        *Salary Range:* ₹12-18 LPA.

        *Demand:* Extremely high, particularly in technology and finance sectors.
        """)

    elif career_option == "Doctor":
        st.markdown(""" 
        *Role:* Provide medical care and treatment to patients.

        *Required Skills:* Medical knowledge, communication, empathy.

        *Education Needed:* Medical degree (MBBS) and specialization.

        *Salary Range:* ₹6-15 LPA (depending on specialization).

        *Demand:* High, with consistent need across urban and rural areas.
        """)

    elif career_option == "UX Designer":
        st.markdown(""" 
        *Role:* Improve user experiences by designing intuitive and functional user interfaces.

        *Required Skills:* UI/UX design, prototyping, user research, wireframing.

        *Education Needed:* Bachelor's in Design or related field.

        *Salary Range:* ₹5-10 LPA.

        *Demand:* Growing rapidly with the rise of digital products.
        """)

    elif career_option == "Mechanical Engineer":
        st.markdown(""" 
        *Role:* Design, develop, and test mechanical systems, including engines and machines.

        *Required Skills:* Solid mechanics, thermodynamics, CAD software, problem-solving.

        *Education Needed:* Bachelor's in Mechanical Engineering.

        *Salary Range:* ₹5-8 LPA.

        *Demand:* Steady, especially in manufacturing and automotive industries.
        """)

    elif career_option == "Civil Engineer":
        st.markdown(""" 
        *Role:* Design and manage the construction of infrastructure such as roads, bridges, and buildings.

        *Required Skills:* Project management, construction techniques, CAD, material science.

        *Education Needed:* Bachelor's in Civil Engineering.

        *Salary Range:* ₹5-7 LPA.

        *Demand:* Moderate, driven by the infrastructure boom in urban development.
        """)


    elif career_option == "Pharmacist":
        st.markdown("""
        *Role:* Dispense prescription medications, counsel patients on proper usage, and manage medication therapy.

        *Required Skills:* Knowledge of pharmaceuticals, patient care, attention to detail.

        *Education Needed:* Bachelor's in Pharmacy (B.Pharm) or Doctor of Pharmacy (Pharm.D.).

        *Salary Range:* ₹3-6 LPA.

        *Demand:* Steady, especially in healthcare, retail, and pharmaceutical industries.
        """)

    elif career_option == "Lawyer":
        st.markdown("""
        *Role:* Represent clients in legal matters, provide legal advice, and prepare documents.

        *Required Skills:* Legal knowledge, communication, research, negotiation.

        *Education Needed:* Bachelor's in Law (LLB), followed by further specialization in a legal field.

        *Salary Range:* ₹5-10 LPA (varies based on experience and specialization).

        *Demand:* High, with steady demand in corporate law, family law, and criminal law.
        """)

    elif career_option == "Accountant":
        st.markdown("""
        *Role:* Manage financial records, prepare reports, and ensure tax compliance.

        *Required Skills:* Knowledge of accounting principles, attention to detail, proficiency in software like Tally, Excel.

        *Education Needed:* Bachelor's in Commerce (B.Com) or Chartered Accountant (CA).

        *Salary Range:* ₹4-8 LPA.

        *Demand:* High, especially in corporate finance, auditing, and tax firms.
        """)

    elif career_option == "AI Engineer":
        st.markdown("""
        *Role:* Design and develop AI models and systems, applying machine learning algorithms to solve complex problems.

        *Required Skills:* Python, machine learning, deep learning, data analysis.

        *Education Needed:* Bachelor's/Master's in Computer Science, AI, or related field.

        *Salary Range:* ₹10-20 LPA.

        *Demand:* Extremely high, driven by the rapid growth of AI technologies across industries.
        """)

    elif career_option == "Psychologist":
        st.markdown("""
        *Role:* Assess, diagnose, and treat mental health disorders through therapy and counseling.

        *Required Skills:* Communication, empathy, psychological testing, counseling techniques.

        *Education Needed:* Bachelor's/Master's in Psychology, followed by a specialization or PhD.

        *Salary Range:* ₹4-12 LPA.

        *Demand:* Growing, especially in clinical, corporate, and counseling roles.
        """)

    elif career_option == "Digital Marketer":
        st.markdown("""
        *Role:* Promote brands and products through online channels using strategies like SEO, social media, and content marketing.

        *Required Skills:* SEO, SEM, content creation, social media management, data analytics.

        *Education Needed:* Bachelor's in Marketing, Digital Media, or related field.

        *Salary Range:* ₹4-8 LPA.

        *Demand:* High, especially in e-commerce and tech-driven industries.
        """)

    elif career_option == "Biotechnologist":
        st.markdown("""
        *Role:* Work with biological systems to create products or processes for medical, agricultural, or industrial use.

        *Required Skills:* Laboratory skills, research, knowledge of genetics and microbiology.

        *Education Needed:* Bachelor's/Master's in Biotechnology or related field.

        *Salary Range:* ₹5-9 LPA.

        *Demand:* Growing, especially in pharmaceuticals, healthcare, and agriculture.
        """)

    elif career_option == "Architect":
        st.markdown("""
        *Role:* Design and plan buildings, ensuring functionality, aesthetics, and safety.

        *Required Skills:* Creativity, project management, CAD software, building codes knowledge.

        *Education Needed:* Bachelor's/Master's in Architecture.

        *Salary Range:* ₹6-12 LPA.

        *Demand:* Steady, particularly in urban development and infrastructure projects.
        """)

    elif career_option == "Teacher":
        st.markdown("""
        *Role:* Teach students at various educational levels, plan lessons, and assess student progress.

        *Required Skills:* Communication, patience, subject expertise, classroom management.

        *Education Needed:* Bachelor's/Master's in Education or a specific subject.

        *Salary Range:* ₹3-8 LPA (depending on the institution and subject).

        *Demand:* Steady, especially in primary, secondary, and higher education institutions.
        """)

if __name__ == "__main__":
    statistics()
