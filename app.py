import streamlit as st

st.set_page_config(
    page_title="Embroidery Service Management System",
    layout="wide"
)

st.title("Embroidery Service Management System")

st.markdown("""
### Welcome

This demo shows how embroidery machine sales, support, workers, and customer complaints can be managed through a single system.

👈 Select a page from the sidebar:

- Admin Dashboard
- Worker Dashboard
- Customer Dashboard
""")

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Customers", 145)

with col2:
    st.metric("Machines", 212)

with col3:
    st.metric("Open Complaints", 18)

with col4:
    st.metric("Workers", 6)

st.info(
    "This is a demo application using mock data to demonstrate the future workflow."
)
