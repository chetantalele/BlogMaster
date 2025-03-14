import streamlit as st
import google.generativeai as genai
import random


api_key = "AIzaSyAsX7k8pjQ6b6z-_dQIk4vKqH5JgbxOXrY"
genai.configure(api_key=api_key)

generation_config = {
    "temperature": 0.75,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)

def generate_blog(user_input, word_count):
    """
    Function to generate a blog based on user input and word count.
    Parameters:
        user_input (str): The topic for the blog.
        word_count (int): The desired number of words for the blog.
    Returns:
        str: The generated blog content.
    """

    # Display a message while the blog is being generated
    st.write("### Generating your blog...")

    st.write(f"While I work on creating your blog, here's a little joke to keep you entertained:\n\n**{get_joke()}**")

    # Start a chat session with the input topic and word count
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    f"Write a blog based on the input topic: {user_input} and number of words: {word_count}\n"
                ],
            },
        ],
    )

    try:
        # Generate a response for the new input
        response = chat_session.send_message(user_input)
        st.success(" Your blog is ready!")
        return response.text

    except Exception as e:
        st.error(f"Error generating blog: {e}")
        return None
    
# Function to generate a joke
def get_joke():
    jokes = [
        "Why don't programmers like nature? It has too many bugs.",
        "Why do Java developers wear glasses? Because they don't see sharp.",
        "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
        "Why don't programmers like nature? It has too many bugs.",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why do Java developers wear glasses? Because they don't see sharp.",
        "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
        "Why do Python programmers prefer using snake_case? Because it's easier to read!",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
        "Why did the developer go broke? Because he used up all his cache.",
        "Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25.",
        "Why did the programmer get kicked out of the beach? Because he kept using the 'C' language!",
        "Why was the computer cold? It left its Windows open."
    ]
    return random.choice(jokes)

def main():

    # Streamlit app
    st.title("BlogMaster: AI-Powered Blog Generation")

    # Display the main image and the friendly robot character
    st.image("blogmaster.jpeg", use_column_width=True) # Adjust the path as needed
    st.write("## Hello! I'm BlogMaster, your friendly robot. Let's create a fantastic blog together!")
    # Get user input
    user_input = st.text_input("Topic", "")
    word_count = st.number_input("Number of words", min_value=100, max_value=5000, value=1000, step=50)

    if st.button("Generate Blog"):
        if user_input and word_count:
            # Call the generate_blog function
            blog_content = generate_blog(user_input, word_count)
            if blog_content:
                st.write(blog_content)
        else:
            st.error("Please provide both the topic and the number of words.")


if __name__ == "__main__":
    main()