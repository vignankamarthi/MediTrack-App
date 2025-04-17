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
    
    # Expandable section for Care Management
    with st.sidebar.expander("🏥 Care Management", expanded=True):
        st.page_link("pages/12_Care_Tasks.py", label="📋 Care Tasks")
        st.page_link("pages/13_Patient_Symptoms.py", label="🤒 Patient Symptoms")
    
    # Expandable section for Clinical Data
    with st.sidebar.expander("🔬 Clinical Data", expanded=True):
        st.page_link("pages/14_Lab_Results.py", label="🧪 Lab Results")
        st.page_link("pages/15_Medication_Administration.py", label="💊 Medication Administration")

def PharmacistSideBar():
    """Sidebar links for Pharmacist role."""
    HomePageLink()
    st.sidebar.page_link("pages/21_Pharmacist_Home.py", label="📊 Dashboard")
    # Add pharmacist-specific links

def AdminSideBar():
    """Sidebar links for Admin role."""
    HomePageLink()
    st.sidebar.page_link("pages/31_Admin_Home.py", label="📊 Dashboard")
    # Add admin-specific links
