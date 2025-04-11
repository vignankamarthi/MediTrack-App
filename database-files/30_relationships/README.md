# Relationship Tables

This directory contains sample data for all relationship (bridge) tables in the MediTrack database.

## Organization

The files are organized by the main entity they relate to:

- **31_patient_relationships** - All relationships connecting patients to other entities
- **33_medication_relationships** - All relationships connecting medications to other entities
- **34_treatment_relationships** - All relationships connecting treatments to other entities
- **35_provider_relationships** - All relationships connecting healthcare providers to other entities
- **36_pathway_relationships** - All relationships connecting care pathways to other entities
- **37_other_relationships** - All other relationship tables

## Bridge Tables Overview

In total, there are 25 bridge tables in the MediTrack database:

1. Patient-related bridge tables (10)
2. Medication-related bridge tables (3)
3. Treatment-related bridge tables (3)
4. Provider-related bridge tables (3)
5. Pathway-related bridge tables (2)
6. Other bridge tables (4)

## Loading Order

Files must be loaded in numeric order to maintain referential integrity.
