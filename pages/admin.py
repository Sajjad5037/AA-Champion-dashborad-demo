import streamlit as st

st.set_page_config(
    page_title="Admin Dashboard",
    layout="wide"
)

st.title("Admin Dashboard")

# ==========================
# KPI CARDS
# ==========================

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

# ==========================
# CREATE COMPLAINT
# ==========================

st.subheader("Create Complaint")

col1, col2 = st.columns(2)

with col1:
    customer = st.selectbox(
        "Customer",
        [
            "Ahmed Embroidery Center",
            "Star Embroidery",
            "Fashion Stitch",
            "Noor Textile"
        ]
    )

    machine = st.selectbox(
        "Machine",
        [
            "Tajima TMAR-K1506C",
            "Tajima TMEZ-SC",
            "Barudan BEKY",
            "Ricoma MT-1501"
        ]
    )

with col2:
    worker = st.selectbox(
        "Assign Worker",
        [
            "Bilal",
            "Ali",
            "Hassan",
            "Unassigned"
        ]
    )

    priority = st.selectbox(
        "Priority",
        [
            "Low",
            "Medium",
            "High"
        ]
    )

issue = st.text_area(
    "Issue Description",
    placeholder="Describe the customer's issue..."
)

if st.button("Create Complaint"):
    st.success("Complaint created successfully!")

st.divider()

# ==========================
# RECENT COMPLAINTS
# ==========================

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
        st.write(f"### {complaint['ticket']}")
        st.write(f"**Customer:** {complaint['customer']}")
        st.write(f"**Issue:** {complaint['issue']}")
        st.write(f"**Assigned To:** {complaint['worker']}")
        st.write(f"**Status:** {complaint['status']}")
