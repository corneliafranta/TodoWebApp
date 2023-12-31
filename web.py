import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = "\n" + st.session_state["new_todo"]
    todos.append(todo)
    functions.save_todos(todos)


st.title("My Todo App")
st.subheader("This is my Todo App.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.remove_item(todo)
        del st.session_state[todo]
        st.rerun()

st.text_input(label=" ",
              placeholder="Add a new todo...",
              on_change=add_todo,
              key="new_todo"
              )
