import requests
import json
import streamlit as st

prompt=st.chat_input()
if prompt:
  with st.chat_message('User'):
    st.write(prompt)
  out=requests.post(
      "https://ishwarikatariya.app.modelbit.com/v1/chat/7",
      headers={"Content-Type": "application/json"},
      data=json.dumps(
          {
              "data":f"System: You are a helpful AI mathematician. Always explain your answer step-by-step so the user can understand. \n\n User: {prompt} \n\n Assistant:"
          }
      ),
  ).json()
  text=out['data']['message']
  text=eval(text)[0]
  text=text['generated_text'].split('User:')[0]
  with st.chat_message('Assistant'):
    st.write(text)
