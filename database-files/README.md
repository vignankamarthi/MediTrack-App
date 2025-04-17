# MediTrack Database Files

This directory contains all SQL files for the MediTrack application database.

## Directory Structure

- **00_meditrack_schema.sql** - Main schema file (can be used to source all other schema files)
- **10_entities/** - Sample data for 17 main entity tables
- **30_relationships/** - Sample data for 25 bridge tables, organized by entity

## Loading Order

When initializing the database, files should be loaded in this order:

1. Schema definition (00_meditrack_schema.sql)
2. Entity data (10_entities/\*)
3. Relationship data (30_relationships/\*)

## Sample Data Requirements

According to project requirements:

- Strong entities should have 30-40 rows
- Weak entities should have 50-75 rows
- Bridge tables should have 125+ rows

## User Personas

The database supports four main user personas:

1. **Head Physician (Dr. James Wilson)**
2. **Nurse (Maria Rodriguez)**
3. **Pharmacist (Sarah Chen)**
4. **System Administrator (Brennan)**

## REST API Support

The database structure and sample data are designed to support all endpoints specified in the REST API matrix for each user persona.

Video for Presentation:
https://drive.google.com/file/d/1hFlxIFWukjAvzhw0FYzKAaQg2r5IsKKh/view?usp=share_link

Video for Presenters Visual: 
https://drive.google.com/file/d/1hFlxIFWukjAvzhw0FYzKAaQg2r5IsKKh/view?usp=share_link
