import streamlit as st

# Navigation functions based on role
def SideBarLinks(role):
    """Display sidebar navigation links based on user role."""
    if role == "physician":
        PhysicianSideBar()
    elif role == "nurse":
        NurseSideBar()
    elif role == "pharmacist":
        PharmacistSideBar()
    elif role == "admin":
        AdminSideBar()

def HomePageLink():
    """Home page link for all roles."""
    st.sidebar.page_link("Home.py", label="🏠 Home")

def PhysicianSideBar():
    """Sidebar links for Physician role."""
    HomePageLink()
    st.sidebar.page_link("pages/01_Physician_Home.py", label="📊 Dashboard")
    
    # Expandable section for Example UIs
    with st.sidebar.expander("📈 Provider Analysis", expanded=True):
        st.page_link("pages/02_ExampleUI1.py", label="Provider Comparison")
        st.page_link("pages/03_ExampleUI2.py", label="Population Health")
    
    # Other physician links
    st.sidebar.page_link("pages/04_Treatment_Outcomes.py", label="💊 Treatment Outcomes")
    st.sidebar.page_link("pages/05_Patient_Records.py", label="👤 Patient Records")
    st.sidebar.page_link("pages/06_Clinical_Protocols.py", label="📝 Clinical Protocols")

def NurseSideBar():
    """Sidebar links for Nurse role."""
    HomePageLink()
    st.sidebar.page_link("pages/11_Nurse_Home.py", label="📊 Dashboard")
    
    # Patient care management
    st.sidebar.page_link("pages/12_Patient_Care.py", label="👤 Patient Care")
    st.sidebar.page_link("pages/13_Medication_Management.py", label="💊 Medication Management")
    st.sidebar.page_link("pages/14_Task_Management.py", label="📋 Task Management")
    st.sidebar.page_link("pages/15_Care_Pathways.py", label="🛤️ Care Pathways")
    st.sidebar.page_link("pages/16_Documentation.py", label="📄 Documentation")

def PharmacistSideBar():
    """Sidebar links for Pharmacist role."""
    HomePageLink()
    st.sidebar.page_link("pages/21_Pharmacist_Home.py", label="📊 Dashboard")
    st.sidebar.page_link("pages/22_Medication_Review.py", label="💊 Medication Review")
    st.sidebar.page_link("pages/23_Prescription_Outcomes.py", label="📋 Prescription Outcomes")
    st.sidebar.page_link("pages/24_Medication_Reconciliation.py", label="✅ Medication Reconciliation")
    st.sidebar.page_link("pages/25_Patient_Education.py", label="📚 Patient Education")

def AdminSideBar():
    """Sidebar links for Admin role."""
    HomePageLink()
    st.sidebar.page_link("pages/31_Admin_Home.py", label="📊 Dashboard")
    st.sidebar.page_link("pages/32_Admin_Compliance.py", label="🔒 Audit & Compliance")
    st.sidebar.page_link("pages/33_Admin_Settings.py", label="⚙️ System Settings")
    
    # Additional admin links that would link to future pages
    st.sidebar.markdown("---")
    st.sidebar.page_link("pages/31_Admin_Home.py", label="👥 User Management", help="Manage system users and permissions")
    st.sidebar.page_link("pages/31_Admin_Home.py", label="🗄️ Database Admin", help="Database management and maintenance")
