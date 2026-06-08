import streamlit as st
import pandas as pd

st.title("Customer Dashboard")

st.subheader("My Machines")

machines = pd.DataFrame([
    {
        "Machine": "Tajima TMAR-K1506C",
        "Warranty": "Valid",
        "Status": "Active"
    }
])

st.dataframe(machines, use_container_width=True)

st.divider()

st.subheader("Create Complaint")

issue_type = st.selectbox(
    "Issue Type",
    [
        "Thread Breaking",
        "Needle Issue",
        "Motor Issue",
        "Training Required"
    ]
)

description = st.text_area(
    "Describe the problem"
)

if st.button("Submit Complaint"):
    st.success("Complaint Submitted")

st.divider()

st.subheader("My Complaints")

complaints = pd.DataFrame([
    {
        "Ticket": "#101",
        "Issue": "Thread Breaking",
        "Status": "Assigned"
    },
    {
        "Ticket": "#102",
        "Issue": "Needle Issue",
        "Status": "Resolved"
    }
])

st.dataframe(complaints, use_container_width=True)
