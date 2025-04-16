# caretask_manager_dash_page2.py

import streamlit as st
import requests

API_URL = "http://localhost:5000"

def run():

    # need import
    from layout_template import render_header
    render_header()

    st.markdown("## 📝 Care Task Manager")

    # get  care tasks from API
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
                margin-bottom: 2rem;
            }
            .card-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                border-bottom: 1px solid #e0e0e0;
                margin-bottom: 1rem;
            }
            .card-title {
                font-size: 20px;
                font-weight: bold;
                color: #003366;
            }
            .btn-outline {
                padding: 0.4rem 0.8rem;
                border: 1px solid #007bff;
                border-radius: 6px;
                background: white;
                color: #007bff;
                font-size: 14px;
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
            .urgency-high {
                background-color: #dc3545;
            }
            .urgency-medium {
                background-color: #ffc107;
            }
            .urgency-low {
                background-color: #28a745;
            }
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

    # Build out care tasks cardsin HTML
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("""
        <div class="card-header">
            <div class="card-title">Care Tasks</div>
            <button class="btn-outline">Add Task</button>
        </div>
        <div class="card-body">
            <ul class="task-list">
    """, unsafe_allow_html=True)

    for task in tasks:
        priority = task.get("priority", "low").lower()
        urgency_class = f"urgency-{priority}"
        st.markdown(f"""
            <li class="task-item">
                <div class="task-content">
                    <span class="urgency-indicator {urgency_class}"></span>
                    <div class="task-details">
                        <h4>{task.get("task_name", "Unnamed Task")}</h4>
                        <p>{task.get("description", "No description provided.")}</p>
                    </div>
                </div>
                <div class="task-meta">
                    <div class="task-assigned">Assigned to: You</div>
                    <div class="task-due">Due: Today</div>
                </div>
            </li>
        """, unsafe_allow_html=True)

    st.markdown("""
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

