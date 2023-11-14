import streamlit as st
from langchain.llms import GooglePalm
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from key import GOOGLE_API_KEY
import os

# Initialize the model
llm = GooglePalm(temperature=0.1, google_api_key=GOOGLE_API_KEY)

# Define the prompt template
prompt_template = PromptTemplate(
    input_variables=['name'],
    template="{name}(japanese_name) backstory, powers/abilities"
)

# Create the chain
chain = LLMChain(llm=llm, prompt=prompt_template)

# Streamlit App
st.title("TheOtaku-Fandom")

# Take user input for 'name'
name = st.text_input("Enter The Character name:")

# Add a search button
search_button = st.button("Search")

if search_button:
    # Check if a name is entered before performing the search
    if name:
        # Generate output based on the entered name
        result = chain.run(name)
        st.write(result)
    else:
        st.warning("Please enter a character name before clicking the search button.")