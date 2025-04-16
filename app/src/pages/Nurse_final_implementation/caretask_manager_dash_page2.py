import streamlit as st
import requests

API_URL = "http://web-api:4000"

def run():
    from layout_template import render_header
    render_header()

    st.markdown("## Care Task Manager")

    if "show_add_form" not in st.session_state:
        st.session_state["show_add_form"] = False
    if "task_to_edit" not in st.session_state:
        st.session_state["task_to_edit"] = None
    if "task_edit_desc" not in st.session_state:
        st.session_state["task_edit_desc"] = ""

    if st.button(" Add Task"):
        st.session_state["show_add_form"] = not st.session_state["show_add_form"]

    if st.session_state["show_add_form"]:
        with st.form("add_task_form"):
            st.subheader("Create a New Care Task")
            task_name = st.text_input("Task Name")
            description = st.text_area("Description")
            priority = st.selectbox("Priority", ["low", "medium", "high"])
            estimated_duration = st.text_input("Estimated Duration (e.g., 30 mins)")

            submitted = st.form_submit_button("Submit Task")

            if submitted:
                new_task = {
                    "task_name": task_name,
                    "description": description,
                    "priority": priority,
                    "estimated_duration": estimated_duration
                }
                try:
                    post_resp = requests.post(f"{API_URL}/care-tasks/", json=new_task)
                    if post_resp.status_code == 201:
                        st.success(" Task successfully added!")
                        st.session_state["show_add_form"] = False
                        st.experimental_rerun()
                    else:
                        st.error(f" Failed to add task: {post_resp.status_code}")
                except Exception as e:
                    st.error(f" Error submitting task: {e}")

    try:
        response = requests.get(f"{API_URL}/care-tasks")
        response.raise_for_status()
        tasks = response.json()
    except Exception as e:
        st.error(f"Failed to load tasks: {e}")
        return

    st.markdown("""
        <style>
            .card {
                background: #fff;
                border-radius: 10px;
                padding: 1rem;
                box-shadow: 0 2px 8px rgba(0,0,0,0.05);
                margin-top: 1.5rem;
            }
            .task-list {
                list-style: none;
                padding-left: 0;
            }
            .task-item {
                display: flex;
                justify-content: space-between;
                border-bottom: 1px solid #eee;
                padding: 1rem 0;
            }
            .task-content {
                display: flex;
                align-items: flex-start;
                gap: 0.75rem;
            }
            .urgency-indicator {
                width: 12px;
                height: 12px;
                border-radius: 50%;
                margin-top: 5px;
            }
            .urgency-high { background-color: #dc3545; }
            .urgency-medium { background-color: #ffc107; }
            .urgency-low { background-color: #28a745; }
            .task-details h4 {
                margin: 0;
                font-size: 16px;
            }
            .task-details p {
                margin: 0.2rem 0 0;
                font-size: 14px;
                color: #555;
            }
            .task-meta {
                text-align: right;
                font-size: 13px;
                color: #777;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="card"><ul class="task-list">', unsafe_allow_html=True)

    for task in tasks:
        task_id = task["task_id"]
        name = task["task_name"]
        desc = task["description"]
        priority = task.get("priority", "low").lower()
        urgency_class = f"urgency-{priority}"

        st.markdown(f"""
            <li class="task-item">
                <div class="task-content">
                    <span class="urgency-indicator {urgency_class}"></span>
                    <div class="task-details">
                        <h4>{name}</h4>
                        <p>{desc}</p>
                    </div>
                </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("🗑️ Delete", key=f"delete_{task_id}"):
                try:
                    del_resp = requests.delete(f"{API_URL}/care-tasks/{task_id}")
                    if del_resp.status_code == 200:
                        st.success(f" Task {task_id} deleted")
                        st.experimental_rerun()
                    else:
                        st.error(" Failed to delete task")
                except Exception as e:
                    st.error(f" {e}")

        with col2:
            if st.button("✏️ Edit", key=f"edit_{task_id}"):
                st.session_state["task_to_edit"] = task_id
                st.session_state["task_edit_desc"] = desc

        st.markdown("</li>", unsafe_allow_html=True)

    st.markdown("</ul></div>", unsafe_allow_html=True)

    # Edit form only shows when task_to_edit is set
    if st.session_state.get("task_to_edit") is not None:
        st.subheader("Edit Task Description")
        new_desc = st.text_area(
            "New Description",
            value=st.session_state.get("task_edit_desc", ""),
            key="edit_desc_input"
        )
        if st.button("Update Description", key="submit_edit"):
            try:
                put_resp = requests.put(
                    f"{API_URL}/care-tasks/{st.session_state['task_to_edit']}/description",
                    json={"description": new_desc}
                )
                if put_resp.status_code == 200:
                    st.success("✅ Description updated.")
                    st.session_state["task_to_edit"] = None
                    st.experimental_rerun()
                else:
                    st.error(" Failed to update description.")
            except Exception as e:
                st.error(f"{e}")