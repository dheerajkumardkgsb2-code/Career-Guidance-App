import streamlit as st
import base64
import os

def testimonials():
    st.title("💬 Testimonials")
    st.markdown("### Hear from Our Users:")

    
    default_image_path = os.path.join("images", "default_dp.jpg")

    
    def get_base64_image(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    default_image_base64 = get_base64_image(default_image_path)

    testimonials_data = [
        {"name": "Ravi", "feedback": "This app helped me understand what I truly want to pursue!", "emoji": "🙏"},
        {"name": "Sneha", "feedback": "Very intuitive and simple to use. Love the survey results!", "emoji": "💡"},
        {"name": "Amit", "feedback": "The statistics gave me a new perspective on job market trends.", "emoji": "📊"}
    ]

    # Custom CSS
    st.markdown(f"""
        <style>
            .testimonial-container {{
                background: linear-gradient(135deg, #2c3e50, #34495e);
                color: #f1f1f1;
                padding: 25px;
                border-radius: 15px;
                margin-bottom: 20px;
                box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
                transition: all 0.3s ease;
                transform: translateY(0);
                animation: bounceIn 1s ease-out;
                display: flex;
                align-items: flex-start;
                gap: 20px;
            }}

            .testimonial-container:hover {{
                background: linear-gradient(135deg, #34495e, #2c3e50);
                transform: scale(1.05) translateY(-5px);
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
            }}

            .testimonial-image {{
                width: 60px;
                height: 60px;
                border-radius: 50%;
                object-fit: cover;
                border: 2px solid #4CAF50;
                box-shadow: 0 2px 6px rgba(0,0,0,0.3);
            }}

            .testimonial-content {{
                flex: 1;
            }}

            .testimonial-name {{
                font-size: 20px;
                font-weight: bold;
                color: #4CAF50;
                margin-bottom: 10px;
                animation: fadeIn 1s ease-out;
            }}

            .testimonial-feedback {{
                font-size: 17px;
                color: #ddd;
                line-height: 1.5;
                animation: fadeIn 1s ease-out 0.5s;
            }}

            .testimonial-emoji {{
                font-size: 30px;
                margin-left: 10px;
            }}

            .testimonial-divider {{
                border-top: 1px solid #555;
                margin-top: 20px;
                margin-bottom: 15px;
            }}

            @keyframes bounceIn {{
                0% {{
                    transform: scale(0.3) translateY(20px);
                    opacity: 0;
                }}
                50% {{
                    transform: scale(1.1) translateY(-10px);
                    opacity: 1;
                }}
                100% {{
                    transform: scale(1) translateY(0);
                    opacity: 1;
                }}
            }}

            @keyframes fadeIn {{
                from {{
                    opacity: 0;
                    transform: translateY(20px);
                }}
                to {{
                    opacity: 1;
                    transform: translateY(0);
                }}
            }}

            .testimonial-emoji:hover {{
                color: #f39c12;
                cursor: pointer;
            }}
        </style>
    """, unsafe_allow_html=True)

    for t in testimonials_data:
        st.markdown(f"""
            <div class="testimonial-container">
                <img class="testimonial-image" src="data:image/jpeg;base64,{default_image_base64}" />
                <div class="testimonial-content">
                    <div class="testimonial-name">{t['name']}</div>
                    <div class="testimonial-feedback">{t['feedback']}<span class="testimonial-emoji">{t['emoji']}</span></div>
                </div>
            </div>
            <div class="testimonial-divider"></div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    testimonials()
