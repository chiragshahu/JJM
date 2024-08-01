import streamlit as st
from crew import JJMCrew
import streamlit as st
from streamlit_chat import message as st_message

class CrewOutput:
    def __init__(self, data):
        self.data = data

    def to_dict(self):
        return {"data": self.data}

# import json
# class CustomJSONEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, CrewOutput):
#             return obj.to_dict()
#         return super().default(obj)

# __import__('pysqlite3')
# import sys

# sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

def generate_response(query):

    response = JJMCrew(query)
    answer = response.run()
    
    if isinstance(answer, CrewOutput):
        return str(answer.output)  # or answer.output if it's already a string
    else:
        return str(answer)

def get_chat_history():
    if "history" not in st.session_state:
        st.session_state.history = []
    return st.session_state.history

def add_message_to_history(role, content):
    history = get_chat_history()
    history.append({"role": role, "content": content})
    st.session_state.history = history

def handle_user_input():
    user_input = st.session_state.input
    if user_input:
        add_message_to_history("user", user_input)
        response = generate_response(user_input)
        add_message_to_history("bot", response)
        st.session_state.input = ""

st.set_page_config(page_title="Jal Jeevan Mission Chatbot", page_icon=":robot_face:")
st.title("Jal Jeevan Mission Chatbot")
st.text_input("You:", key="input", on_change=handle_user_input)

# Displaying chat history
chat_history = get_chat_history()

for chat in chat_history:
    if chat["role"] == "user":
        st_message(chat["content"], is_user=True)
    else:
        st_message(chat["content"], is_user=False)