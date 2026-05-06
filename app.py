import streamlit as st

# Page config
st.set_page_config(page_title="Daily To-Do App", page_icon="📝", layout="centered")

st.title("📝 Daily Task Tracker")
st.write("Track your daily tasks easily 🚀")

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Add new task
st.subheader("➕ Add New Task")
new_task = st.text_input("Enter your task")

if st.button("Add Task"):
    if new_task.strip() != "":
        st.session_state.tasks.append({"task": new_task, "done": False})
        st.success("Task added!")
    else:
        st.warning("Please enter a task")

# Display tasks
st.subheader("📋 Your Tasks")

if len(st.session_state.tasks) == 0:
    st.info("No tasks yet. Add one above 👆")
else:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([0.1, 0.7, 0.2])

        # Checkbox (mark complete)
        with col1:
            done = st.checkbox("", value=task["done"], key=f"check_{i}")
            st.session_state.tasks[i]["done"] = done

        # Task text
        with col2:
            if task["done"]:
                st.markdown(f"~~{task['task']}~~")
            else:
                st.write(task["task"])

        # Delete button
        with col3:
            if st.button("❌", key=f"delete_{i}"):
                st.session_state.tasks.pop(i)
                st.rerun()

# Clear all tasks
st.markdown("---")
if st.button("🗑️ Clear All Tasks"):
    st.session_state.tasks = []
    st.rerun()
