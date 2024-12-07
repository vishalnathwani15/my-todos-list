import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todos"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)




st.title("my app") 
st.subheader("this is my todo app")
st.write("This app is for your productivity")


for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        # st.experimental_rerun() if this argument not running then go to below argument
        st.rerun()

st.text_input(label="Enter the todo:", placeholder="Add new todo", on_change=add_todo, key="new_todos")