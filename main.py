import openai
import streamlit as st
from secret_key import openai_key

openai.api_key = st.secrets["openai_key"]

def generate_code(prompt):
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
         messages=[
        {"role": "user", "content": prompt},
    ]
    )
    generated_code = response.choices[0]['message']['content']
    return generated_code

