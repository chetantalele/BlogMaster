import streamlit as st
import google.generativeai as genai
import random
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GoogleGeminiAPIKey")

genai.configure(api_key=api_key)

# Configuration for AI model
generation_config = {
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 50,
    "max_output_tokens": 5000,
    "response_mime_type": "text/plain",
}

# Initialize the AI model
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)

def generate_blog(user_input, word_count):
    """
    Generates a blog post based on user input and desired word count.
    """
    
    st.markdown("""
    <div style='text-align: center;'>
        <h3>📝 Crafting Your Blog...</h3>
        <p style='color: gray;'>Sit back and relax while we create an amazing piece for you!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info(f"✨ While we craft your blog, here’s a motivational quote to inspire you: \n **{get_motivational_quote()}**")
    
    try:
        chat_session = model.start_chat(
            history=[
                {"role": "user", "parts": [f"Write a blog on '{user_input}' with approximately {word_count} words."]},
            ],
        )
        response = chat_session.send_message(user_input)
        st.success("🎉 Your blog is ready!")
        return response.text
    except Exception as e:
        st.error(f"🚨 Error generating blog: {e}")
        return None

def get_motivational_quote():
    """
    Returns a random motivational quote.
    """
    quotes = [
        "Believe in yourself and all that you are!",
        "The best way to predict the future is to create it.",
        "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "Your only limit is your mind.",
        "Dream big. Work hard. Make it happen.",
        "Don't watch the clock; do what it does—keep going!",
        "Great things never come from comfort zones.",
        "Every accomplishment starts with the decision to try.",
    ]
    return random.choice(quotes)

def main():
    """
    Streamlit App UI Setup
    """
    st.set_page_config(page_title="BlogMaster AI", page_icon="📝", layout="wide")
    
    st.markdown("""
    <div style='text-align: center;'>
        <h1>🚀 BlogMaster AI</h1>
        <p style='font-size:18px; color: gray;'>Generate high-quality blogs in seconds with AI-powered creativity!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.image("blogai.jpg", use_column_width=True)
    
    st.markdown("---")
    
    user_input = st.text_input("📌 Enter Blog Topic:", placeholder="e.g., The Future of AI in Healthcare")
    word_count = st.slider("✍️ Desired Word Count:", min_value=100, max_value=5000, value=1000, step=50)
    
    if st.button("✨ Generate My Blog ✨"):
        if user_input and word_count:
            blog_content = generate_blog(user_input, word_count)
            if blog_content:
                st.markdown("""
                <div style='text-align: center;'>
                    <h3>📖 Your AI-Generated Blog</h3>
                </div>
                """, unsafe_allow_html=True)
                st.write(blog_content)
        else:
            st.warning("⚠️ Please enter a topic and select a word count before generating.")

if __name__ == "__main__":
    main()