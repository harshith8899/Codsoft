import streamlit as st
import os
import json
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from JSON file with error handling"""
    try:
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as f:
                return json.load(f)
        return []
    except (json.JSONDecodeError, IOError) as e:
        st.error(f"Error loading tasks: {e}")
        return []

def save_tasks(tasks):
    """Save tasks to JSON file with error handling"""
    try:
        with open(TASKS_FILE, "w") as f:
            json.dump(tasks, f, indent=2)
    except IOError as e:
        st.error(f"Error saving tasks: {e}")

def main():
    st.title("📝 To-Do List App")
    
    # Initialize or load tasks
    tasks = load_tasks()

    # Add task section
    with st.form("add_task"):
        new_task = st.text_input("Add a new task:", key="new_task")
        add_button = st.form_submit_button("Add Task")
        
        if add_button and new_task:
            tasks.append({
                "task": new_task,
                "completed": False,
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
            })
            save_tasks(tasks)
            st.rerun()

    # Display tasks section
    st.subheader("Your Tasks:")
    
    if not tasks:
        st.info("No tasks yet! Add one above.")
        return

    for i, task in enumerate(tasks):
        col1, col2, col3 = st.columns([0.7, 0.15, 0.15])
        
        # Task checkbox
        with col1:
            completed = st.checkbox(
                f"{task['task']} (Created: {task.get('created_at', 'N/A')})",
                value=task["completed"],
                key=f"task_{i}"
            )
            if completed != task["completed"]:
                tasks[i]["completed"] = completed
                save_tasks(tasks)
                st.rerun()
        
        # Priority indicator (optional)
        with col2:
            priority = st.selectbox(
                "Priority",
                ["Low", "Medium", "High"],
                key=f"priority_{i}",
                index=1 if "priority" not in task else ["Low", "Medium", "High"].index(task["priority"])
            )
            if "priority" not in task or priority != task["priority"]:
                tasks[i]["priority"] = priority
                save_tasks(tasks)
        
        # Delete button
        with col3:
            if st.button("❌", key=f"delete_{i}"):
                tasks.pop(i)
                save_tasks(tasks)
                st.rerun()
                break

if __name__ == "__main__":
    main()