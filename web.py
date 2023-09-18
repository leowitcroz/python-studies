import streamlit as st
import modules.functions as functions


todos = functions.getTodo()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(str(todo).title()) 
    
    
    functions.writeTodo(todos)


st.title('My Todo App')
st.subheader('This is my todo app.')
st.write('This app will increase you productivity')

for todo in todos:
    st.checkbox(todo)
    
st.text_input(label='',placeholder='Add Todo...', on_change=add_todo, key='new_todo')