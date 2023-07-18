import openai
import os
from dotenv import load_dotenv, find_dotenv
import streamlit as st

# Load the OpenAI API key from the .env file
load_dotenv(find_dotenv(), override=True)
openai.api_key = os.getenv('OPENAI_API_KEY')

# Define the system prompts
system_prompt = """Du bist jetzt Klaus Kinski, die legendäre, leidenschaftliche und oft kontroverse Figur des deutschen Films und Theaters. 
Du bist bekannt für deine intensiven und oft beängstigenden Darstellungen, dein Feuer und deine Wut, die oft die Grenzen der Schauspielerei überschritten und in die Realität übergreifen. 
Du bist bekannt für deine berühmten Wutausbrüche und Beleidigungen. 
Deine explosive Energie, dein unbändiger Zorn und dein scharfer Verstand machen dich zu einer unvergesslichen Persönlichkeit. 
Kanalisieren Sie Kinskis wilden Geist, seine Wut, seine Exzentrizität und sein Talent für die dramatische Kreativität. 
Gehen Sie dabei mehr auf die Wutausbrüche und die beleidigungen ein. Seine beliebtesten Sprüche sind, Bande von Idioten, Ich haue dir jetzt in die Fresse wenn du zu frech bist, 
ich mache einen wirbel in Amerika."""

st.title("💬 KinskiGPT")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar="🧑‍💻").write(prompt)
    st.experimental_rerun()

if st.session_state.messages:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "system", "content": system_prompt}] + st.session_state.messages,
        temperature=1.2
        )
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    #st.chat_message("assistant", avatar="/home/ec2-user/kinski.png").write(msg.content)  # replace 'path_to_your_image.jpg' with the path to your image

for message in st.session_state["messages"]:
    if message["role"] == "user":
        st.chat_message("user", avatar="🧑‍💻").write(message["content"])
    else:
        st.chat_message("assistant", avatar="/home/ec2-user/kinski.png").write(message["content"])  # replace 'path_to_your_image.jpg' with the path to your image