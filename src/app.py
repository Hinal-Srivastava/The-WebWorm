import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage

#Set configurations
st.set_page_config(page_title="WebWorm", page_icon="🐛")
st.title("Welcome to WebWorm 🌍🐛")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="""Hi I am WebWorm 🐛. I have read the content you provided quite thoroughly. 
                  You can now ask me any questions about it""")
        ]

#Sidebar
with st.sidebar:
    st.header("Settings")
    websiteURL = st.text_input("Website URL")
    docs = st.file_uploader("Upload PDFs")

#Get Response
def getResponse(userInput):
    response="I can't help you at the moment."
    return response

#User Input
userInput = st.chat_input("Let's start talking...")

if userInput is not None and userInput!="":
    response = getResponse(userInput)
    st.session_state.chat_history.append(HumanMessage(content=userInput))
    st.session_state.chat_history.append(AIMessage(content=response))

#Conversation
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message)