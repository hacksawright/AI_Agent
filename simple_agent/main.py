from dotenv import load_dotenv
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()

def init_chat_model():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash"
    ) 

llm = init_chat_model()

class State(TypedDict):
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)

def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()

while True:
    try:
        user_input = input("Bạn: ")
        
        if user_input.lower() in  ["quit", "exit"]:
            print("Chatbot goodbye!")
            break
        state = graph.invoke({"messages": [{"role" : "user", "content": user_input}]})
        print(state["messages"][-1].content)
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
        break

