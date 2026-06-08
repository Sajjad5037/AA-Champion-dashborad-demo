import streamlit as st
import pandas as pd

st.title("Admin Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Customers", 145)

with col2:
    st.metric("Machines", 212)

with col3:
    st.metric("Open Complaints", 18)

with col4:
    st.metric("Workers", 6)

st.divider()

st.subheader("Incoming Complaints")

complaints = pd.DataFrame([
    {
        "Ticket": "#101",
        "Customer": "Ahmed Embroidery",
        "Issue": "Thread Breaking",
        "Status": "Open"
    },
    {
        "Ticket": "#102",
        "Customer": "Star Embroidery",
        "Issue": "Needle Issue",
        "Status": "Open"
    }
])

st.dataframe(complaints, use_container_width=True)

st.divider()

st.subheader("Assign Worker")

ticket = st.selectbox(
    "Complaint",
    [
        "#101",
        "#102"
    ]
)

worker = st.selectbox(
    "Worker",
    [
        "Bilal",
        "Ali",
        "Hassan"
    ]
)

if st.button("Assign"):
    st.success(f"{ticket} assigned to {worker}")
