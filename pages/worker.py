import streamlit as st
import pandas as pd

st.title("Worker Dashboard")

st.subheader("Assigned Tasks")

tasks = pd.DataFrame([
    {
        "Ticket": "#101",
        "Customer": "Ahmed Embroidery",
        "Issue": "Thread Breaking",
        "Status": "Assigned"
    },
    {
        "Ticket": "#103",
        "Customer": "Fashion Stitch",
        "Issue": "Motor Noise",
        "Status": "In Progress"
    }
])

st.dataframe(tasks, use_container_width=True)

st.divider()

st.subheader("Update Task")

ticket = st.selectbox(
    "Ticket",
    [
        "#101",
        "#103"
    ]
)

status = st.selectbox(
    "Status",
    [
        "Assigned",
        "In Progress",
        "Resolved"
    ]
)

notes = st.text_area(
    "Work Notes"
)

if st.button("Save Update"):
    st.success("Task Updated")
