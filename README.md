# MediTrack: Healthcare Management System

## Skills & Technologies Showcased

This project demonstrates proficiency in the following areas:

### Database Design & Implementation
- **Comprehensive Relational Schema**: Designed an expansive healthcare database with 17 entity tables and 25 bridge tables that effectively model complex relationships in a healthcare setting
- **Thorough Data Modeling**: Crafted a detailed medical data model representing interconnected healthcare workflows across physicians, nurses, pharmacists, and system administrators
- **Normalized Database Structure**: Implemented a properly normalized database design that minimizes redundancy while preserving referential integrity
- **Healthcare Domain Relationships**: Successfully modeled the intricate connections between patients, providers, treatments, medications, and outcomes in a cohesive structure
- **Extensive Bridge Table Architecture**: Created a network of junction tables that maintain data consistency while allowing for sophisticated querying
- **Healthcare-Specific Query Design**: Developed specialized queries for clinical effectiveness analysis, medication tracking, and provider performance metrics

### API Development
- **RESTful API Design**: Created a comprehensive API following REST principles with appropriate resource naming and HTTP methods
- **Flask Framework**: Built a Python Flask backend with blueprints for modular code organization
- **Role-Based Routes**: Implemented specialized API endpoints organized by healthcare role (physician, nurse, pharmacist, administrator)
- **Error Handling**: Developed robust exception handling for API requests with appropriate status codes
- **Database Connection Management**: Created efficient database connection patterns using a shared DB connection resource

### System Architecture
- **Containerization**: Implemented Docker and Docker Compose for consistent deployment across environments
- **Microservices Design**: Separated frontend, backend API, and database into independent containerized services
- **Environment Configuration**: Used environment variables and dotenv for secure configuration management
- **Service Discovery**: Implemented container networking for seamless service communication

### Frontend Development
- **Streamlit Framework**: Built interactive web interfaces using Python's Streamlit library
- **Data Visualization**: Created dynamic charts and tables for healthcare analytics
- **Responsive Design**: Implemented mobile-friendly interfaces with custom CSS styling
- **Form Validation**: Added input validation and error handling for data entry forms

This project showcases the ability to design and implement a complete full-stack application with particular strength in healthcare database modeling and API development.

MediTrack is a comprehensive patient care coordination platform designed to transform how healthcare providers collaborate and share critical information through a unified database system. This project was developed for CS 3200 - Database Design under Professor Mark Fontenot

## Project Overview

In today's fragmented healthcare ecosystem, patient data remains isolated in separate systems, leading to potentially life-threatening delays in treatment, wasted resources through redundant testing, and compromised patient care due to information gaps. MediTrack addresses these challenges by:

- Eliminating redundant documentation
- Reducing treatment delays caused by information access barriers
- Preventing medication errors due to incomplete records
- Minimizing the administrative burden on providers

The platform creates a single source of truth for all providers involved in a patient's care journey, enabling data-driven healthcare decisions.

## Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **Backend**: Python Flask (API)
- **Database**: MySQL
- **Containerization**: Docker
- **Development Environment**: Docker Compose

## Project Structure

```
app/
├── Dockerfile           # Docker configuration for the Streamlit app
├── src/                 # Source code for the Streamlit application
│   ├── Home.py          # Main entry point for the application
│   ├── requirements.txt # Python dependencies
│   ├── .streamlit/      # Streamlit configuration
│   ├── modules/         # Shared code modules (navigation, etc.)
│   ├── pages/           # Individual application pages
│   └── static/          # Static assets (CSS, images)
```

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Git

### Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/vignankamarthi/MediTrack-App.git
   cd MediTrack-App
   ```

2. Start the Docker containers:

   ```bash
   docker-compose up
   ```

3. Access the application:
   Open your browser and navigate to `http://localhost:8501`

<br>

4. Dependency Issues:
   If you encounter any dependency issues, ensure you have the following packages installed in your environment:
   
   ```bash
   pip install altair==5.5.0 attrs==25.3.0 blinker==1.9.0 cachetools==5.5.2 certifi==2025.1.31
   pip install cffi==1.17.1 charset-normalizer==3.4.1 click==8.1.8 cryptography==44.0.2 Flask==3.1.0
   pip install gitdb==4.0.12 GitPython==3.1.44 idna==3.10 isodate==0.7.2 itsdangerous==2.2.0
   pip install Jinja2==3.1.6 jsonschema==4.23.0 jsonschema-specifications==2024.10.1 lxml==5.3.2
   pip install MarkupSafe==3.0.2 narwhals==1.35.0 nav==5.3.1 numpy==2.2.4 packaging==24.2
   pip install pandas==2.2.3 pillow==11.2.1 platformdirs==4.3.7 plotly==6.0.1 protobuf==5.29.4
   pip install pyarrow==19.0.1 pycparser==2.22 pydeck==0.9.1 pyspnego==0.11.2
   pip install python-dateutil==2.9.0.post0 python-dotenv==1.1.0 pytz==2025.2 referencing==0.36.2
   pip install requests==2.32.3 requests-file==2.1.0 requests-toolbelt==1.0.0 requests_ntlm==1.3.0
   pip install rpds-py==0.24.0 six==1.17.0 smmap==5.0.2 streamlit==1.44.1 tenacity==9.1.2
   pip install toml==0.10.2 tornado==6.4.2 typing_extensions==4.13.2 tzdata==2025.2 urllib3==2.4.0
   pip install Werkzeug==3.1.3 zeep==4.3.1
   ```
   
   Alternatively, you can create a requirements.txt file with the above dependencies and install them all at once:
   
   ```bash
   pip install -r requirements.txt
   ```

### Login Credentials

The application includes demo accounts for each user role:

- **Physician**: Dr. James Wilson
- **Nurse**: Maria Rodriguez
- **Pharmacist**: Sarah Chen
- **System Administrator**: Brennan Johnson

Select the appropriate role from the home page to log in.

## User Personas

MediTrack is designed to serve four primary user types:

1. **Physicians** (Dr. James Wilson) - Need comprehensive patient information at the point of care and tools for population health management and quality improvement.

2. **Nurses** (Maria Rodriguez) - Coordinate daily patient care activities, document symptoms, administer medications, and ensure care continuity.

3. **Pharmacists** (Sarah Chen) - Require complete medication histories to provide intelligent medication management, flag potential interactions, and ensure medication safety.

4. **System Administrators** (Brennan Johnson) - Maintain the infrastructure, manage user access, and ensure compliance with healthcare regulations.

## Features

### Physician Features

- **Population Health Dashboard**: Visualize treatment outcome trends across patient populations
- **Provider Performance Comparison**: Compare provider metrics in a standardized format
- **Treatment Outcomes Tracking**: Track effectiveness of treatments and protocols
- **Patient Records Management**: Access and manage comprehensive patient information
- **Clinical Protocols**: Develop and maintain evidence-based treatment guidelines

### Nurse Features

- **Patient Care Coordination**: View and manage patient care tasks across providers
- **Medication Administration**: Track and document medication administration
- **Patient Assessment**: Document symptoms and responses to treatments
- **Care Pathways**: Create and update standardized care paths for patients
- **Documentation**: Create and manage clinical documentation

### Pharmacist Features

- **Medication Review**: Review complete medication histories for potential interactions
- **Prescription Outcomes**: Track and analyze medication effectiveness
- **Medication Reconciliation**: Compare pre/post admission medications to prevent errors
- **Patient Education**: Document medication counseling and education

### Administrator Features

- **User Management**: Control access permissions based on roles
- **System Monitoring**: Track performance metrics and system health
- **Audit & Compliance**: Maintain logs and ensure regulatory compliance
- **System Settings**: Configure global application parameters

## Database Design

MediTrack is built on a robust relational database with:

- 17 main entity tables representing core healthcare concepts
- 25 bridge tables managing many-to-many relationships
- Comprehensive data model supporting all user workflows
- RESTful API architecture for secure data access

This project is available for educational purposes only.
