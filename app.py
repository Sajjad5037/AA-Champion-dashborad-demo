import streamlit as st

st.set_page_config(
    page_title="Embroidery Service System",
    layout="wide"
)

st.title("Embroidery Service Management System")

role = st.selectbox(
    "Select Role",
    [
        "Admin",
        "Worker",
        "Customer"
    ]
)

if role == "Admin":
    st.switch_page("pages/admin.py")

elif role == "Worker":
    st.switch_page("pages/worker.py")

elif role == "Customer":
    st.switch_page("pages/customer.py")
