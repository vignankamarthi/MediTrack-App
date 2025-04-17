# `pages` Folder

This folder contains all the pages that will be part of the MediTrack healthcare management application. Each file in this folder represents a distinct page that users can navigate to based on their assigned role.

## Page Organization

Streamlit automatically creates a navigation structure based on the files in this folder. Pages are ordered by their filename prefixes (e.g., `01_`, `02_`, etc.), which determines their order in the navigation menu. The numbers in the filenames are only used for ordering and don't appear in the UI.

## Role-Based Access

The application implements role-based access control. Each page checks the user's role stored in the session state and redirects unauthorized users back to the home page. The roles include:

- **Physician**: Pages 01-06, focused on patient care, treatment outcomes, and clinical protocols
- **Nurse**: Pages 11-16, focused on patient care, medication management, and documentation
- **Pharmacist**: Pages 21-25, focused on medication review, prescription outcomes, and patient education
- **Admin**: Pages 31-33, focused on system administration, compliance, and settings

## Example UIs

Some pages (02_ExampleUI1.py and 03_ExampleUI2.py) demonstrate advanced UI capabilities like data visualization, interactive filters, and complex layouts. These examples showcase how to build intuitive interfaces for healthcare data analysis.

## Navigation

Navigation between pages is handled by the `nav.py` module in the `modules` directory. This module provides role-specific sidebar navigation links that only show pages the current user is authorized to access

This application structure provides a framework to demonstrate role-based access control and different UI patterns, but is not intended to be a complete healthcare system implementation.
