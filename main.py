import openai
import os
import streamlit as st

# Zugriff auf die OpenAI API key aus den Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Definieren der System-Prompts
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
    
for message in st.session_state["messages"]:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("assistant").write(message["content"])
