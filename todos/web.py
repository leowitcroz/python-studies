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

for index ,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.writeTodo(todos)
        del st.session_state[todo]
        st.experimental_rerun()
        
    
st.text_input(label='',placeholder='Add Todo...', on_change=add_todo, key='new_todo')