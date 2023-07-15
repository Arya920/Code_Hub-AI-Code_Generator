import streamlit as st
from PIL import Image
import openai
import re
#from secret_key import openai_key
from main import generate_code

im = Image.open('CodeHub Logo.png')
st.set_page_config(layout="wide",page_title="Stock Price Analysis & Prediction App",page_icon = im)

# <--------------------------hide the right side streamlit menue button ------------------>
# Referance ~ "https://towardsdatascience.com/5-ways-to-customise-your-streamlit-ui-e914e458a17c"
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

# <---------------For Condensing the Layout -------------->
#Referance ~ see above ...
padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)

def main():
    
    # <---------------------------------------------------------- Main Header ------------------------------------------------------------------------------------->
    st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='font-size: 59px; font-weight: bold;'>
            <span style='color: white;'>Code</span>
            <span style='background-color: orange; color: black; padding: 5px;'>Hub</span>
        </h1>
    </div>
    """,
    unsafe_allow_html=True
    )
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,400;0,700;1,400&display=swap');

        .container {
            padding: 2rem;
            background-color: #f0f3f9;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            color: #334e68;
            font-family: 'Roboto', sans-serif;
            font-weight: bold;
            text-align: center;
            margin-bottom: 1.5rem;
        }

        .prompt-input {
            background-color: #ffffff;
            border: 1px solid #d3dbe5;
            border-radius: 5px;
            padding: 0.75rem;
            margin-bottom: 1rem;
            color: #334e68;
            font-family: 'Roboto', sans-serif;
        }

        .generate-btn {
            background-color: #ff6b6b;
            color: #ffffff;
            border: none;
            border-radius: 5px;
            padding: 0.75rem 1.5rem;
            font-weight: bold;
            cursor: pointer;
            font-family: 'Roboto', sans-serif;
        }

        .code-output {
            background-color: #334e68;
            border: 1px solid #d3dbe5;
            border-radius: 5px;
            padding: 1rem;
            font-family: 'Courier New', Courier, monospace;
            font-size: 16px;
            line-height: 1.5;
            color: #ffffff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("**:green[Developed by Arya Chakraborty]** 😁😎😇")

    col1,col2 = st.columns(2)
    with col1:
        user_prompt = st.text_area("**:green[Enter your Question !]**")

    with col2:
        option = st.selectbox(
        '**:green[Choose preferable language ~]**',
        ('Python', 'Java', 'C', 'C++')
        )
    language_prompt = f'''give me the solution code in {option} language'''

#-------------------------------------- FINAL PROMPT---------------------------------------->
    Final_Prompt = ". ".join([user_prompt, language_prompt])

    if st.button("Generate Code"):
        code = generate_code(Final_Prompt)
        st.markdown("<div class='code-output'>{}</div>".format(code), unsafe_allow_html=True)
        

# Run the app
if __name__ == '__main__':
    main()
