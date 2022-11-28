# streamlit is a very important tool to develop web app
# it integrates graphs easily
import streamlit as st
import functions

# get todos.txt
todos = functions.get_todos()

# get a wide webpage and also responsive to shape change
st.set_page_config(layout = "wide")

# we want input sth in the box, and it will show in the webpage
# and it will show in the todos.txt
# note: mouse cursor should be in front of the new line in todos.txt
def add_todo():
    # session_state: a dictionary, contain input data in pairs
    # e.g. when input "hello", you get: {"new_todo":"Hello"}
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My todo app")
st.subheader("This is a subheader")
st.write("This app is to increase your <b>productivity</b>",
         # this one allows streamlit uses HTML element
         # And HMTL only can be used in .write function
         unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    # if True, means if is checked
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        # delete the item in the .txt too
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="",placeholder="Add new todo...",
              on_change = add_todo, key="new_todo")

# to run it, go to terminal, and input:
# streamlit run web.py

