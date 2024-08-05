import streamlit as st

# Set page title
st.title("To-Do List App")

# Function to add a new task
def add_task():
    if st.session_state["new_task"]:
        st.session_state["tasks"].append(st.session_state["new_task"])
        st.session_state["new_task"] = ""

# Function to delete a task
def delete_task(task):
    st.session_state["tasks"].remove(task)

# Initialize session state variables
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []
if "new_task" not in st.session_state:
    st.session_state["new_task"] = ""

# Input for new task
st.text_input("Add a new task:", key="new_task", on_change=add_task)

# Display tasks
st.write("Your Tasks:")
for task in st.session_state["tasks"]:
    st.write(f"- {task} ", st.button("Delete", key=task, on_click=delete_task, args=(task,)))

# Button to clear all tasks
if st.button("Clear All Tasks"):
    st.session_state["tasks"] = []
