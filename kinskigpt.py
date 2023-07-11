# Import required libraries
import openai  # OpenAI's GPT model
import os  # to interact with the OS
from dotenv import load_dotenv, find_dotenv  # to load environment variables
import streamlit as st  # web app framework

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

# Create two columns for the UI layout
col1, col2 = st.columns([0.85, 0.15])
with col1:
    st.title('KinskiGPT')  # Title of the web page
with col2:
    st.image('kinski.png', width=70)  # Display an image

# Initialize the messages with the system prompt
messages = [{'role': 'system', 'content': system_prompt}]

# Create a session state for the chat history and text input key
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = ''

user_input = st.text_input("Ich:")

# If the Send button is clicked
if user_input:
    # Add the user's message to the chat history
    st.session_state['chat_history'] += f"\nIch: {user_input}\n"

    messages.append({'role': 'user', 'content': user_input})

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        temperature=1.2
        #max_tokens = 3000
    )

    current_response = response.choices[0]['message']['content']
    # Add the bot's response to the chat history
    st.session_state['chat_history'] += f"\nKlaus Kinski: {current_response}\n"

    messages.append({'role': 'assistant', 'content': current_response})

    # Display the chat history
    st.write(st.session_state['chat_history'])
