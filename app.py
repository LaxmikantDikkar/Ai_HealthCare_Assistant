import streamlit as st
import tensorflow
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# loading a pre-trained model from the hugging face
chatbot = pipeline('text-generation', model='distilgpt2')

def healthChatBot(user_input):
    user_input = user_input.lower()
    if "symptoms" in user_input:
        return "Please concern with the doctor."
    elif "appoiment" in user_input:
        return "Do you want to book an appoiment with the doctor."
    elif "medication" in user_input:
        return "It's important to take prescribed medicine regularly. If you have concern, consult to your doctor."
    else:
        response = chatbot(user_input, max_length=500, num_return_sequences=1)
        return response[0]['generated_text']
def main():
    st.title("HealthCare Assistant chatbot")
    user_input = st.text_input("How can i assist you today?")
    st.button("Submit")

    if st.button:
        st.write("User: " + user_input)
        with st.spinner("Processing please wait...."):
            st.write("HealthCare Assistant: "+ healthChatBot(user_input))
    else:
        st.write("Please provide some input")


main()