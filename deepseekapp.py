from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st

st.title('deepseek local chatbot dummy (1.5)parameters')

template = """""Question : {question}

Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model='deepseek-r1:1.5b')

chain = prompt | model

question = st.chat_input("enter question here")

if question:
    st.write(chain.invoke({"question" : question}))
