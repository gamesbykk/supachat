import requests
import json
import streamlit as st

prompt=st.chat_input()
if prompt:
  with st.chat_message('User'):
    st.write(prompt)
  out=requests.post(
      "https://ishwarikatariya.app.modelbit.com/v1/chat/latest",
      headers={"Content-Type": "application/json"},
      data=json.dumps(
          {
              "data":f"System: Give response to prompt only. \n\n User: {prompt} \n\n Assistant:"
          }
      ),
  ).json()
  with st.chat_message('Assistant'):
    st.write(out)
