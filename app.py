import streamlit as st

#Set the title of the app
st.title("Welcome to My First Streamlit App")

#Add a text input
name = st.text_input("Enter your name:")

#Display the name entered by the user
if name:
  st.write(f"Hello, (name)! Welcome to the app.")

beautifulsoup4==4.12.3
langchain==0.2.11
matplotlib==3.8.4
nltk==3.8.1
openai==1.37.1
pandas==2.2.2
seaborn==0.13.2
spacy==3.7.5
streaming==0.1.2
streamlit==1.37.0
tensorflow==2.17.0
torch==2.3.0
transformers==4.43.2
utils==1.0.2
