import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

st.set_page_config(page_title="위로의 나침반", page_icon="👂")
st.title("👂 위로의 나침반 👂")

with st.expander('위로의 나침반이란? '):
    st.write('위로의 나침반은 힘든 수험생활을 하고 있는 학생들에게 위로를 건네주고 올바른 방향을 제시해주는 챗봇입니다.😊')
    
if "messages" not in st.session_state:
    st.session_state["messages"] = []
    
# 이전 대화기록을 출력해 주는 코드
if len(st.session_state["messages"]) > 0:
    for role, message in st.session_state["messages"]:
        st.chat_message(role).write(message)

if user_input:= st.chat_input("메시지를 입력해주세요."):
    #사용자가 입력한 코드
    st.chat_message("user").write(f"{user_input}")
    st.session_state["messages"].append({"user", user_input})
    
    #LLM을 사용하여 AI의 답변을 작성
    prompt = ChatPromptTemplate.from_template(
        """질문에 대하여 짧고 간결하게 답변해주세요.
{question}                                 
"""
)
        
    chain = prompt | ChatOpenAI() 
    response = chain.invoke({"question": user_input})
    msg = response.content
    
    #AI의 답변
    with st.chat_message("assistant"):
        #msg = f"당신이 입력한 내용: {user_input}"
        st.write(msg)
        st.session_state["messages"].append(("assistant", msg))