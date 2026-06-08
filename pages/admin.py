import streamlit as st

st.title("Admin Dashboard 2")

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

st.subheader("Recent Complaints")

complaints = [
    {
        "ticket": "#101",
        "customer": "Ahmed Embroidery Center",
        "issue": "Thread Breaking",
        "worker": "Bilal",
        "status": "In Progress"
    },
    {
        "ticket": "#102",
        "customer": "Star Embroidery",
        "issue": "Needle Issue",
        "worker": "Ali",
        "status": "Pending"
    },
    {
        "ticket": "#103",
        "customer": "Fashion Stitch",
        "issue": "Motor Noise",
        "worker": "Unassigned",
        "status": "Open"
    }
]

for complaint in complaints:
    with st.container(border=True):
        st.write(f"**{complaint['ticket']}**")
        st.write(f"Customer: {complaint['customer']}")
        st.write(f"Issue: {complaint['issue']}")
        st.write(f"Worker: {complaint['worker']}")
        st.write(f"Status: {complaint['status']}")
