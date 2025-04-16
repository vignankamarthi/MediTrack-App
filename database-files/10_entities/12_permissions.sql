-- Sample data for PERMISSIONS table
-- Create 30-40 rows as specified in requirements

USE meditrack;

-- Insert sample permissions here
-- Example:
-- INSERT INTO PERMISSIONS (permission_name, description, user_id, is_active)
-- VALUES ('view_patient_records', 'Can view patient medical records', 1, TRUE);

INSERT INTO PERMISSIONS (permission_name, description, user_id, is_active) VALUES
('view_patient_records', 'Can view patient medical records', 1, TRUE),
('edit_patient_records', 'Can edit patient medical records', 1, TRUE),
('prescribe_medication', 'Can prescribe medications', 1, TRUE),
('view_patient_records', 'Can view patient medical records', 2, TRUE),
('edit_patient_records', 'Can edit patient medical records', 2, TRUE),
('administer_medication', 'Can administer medications', 2, TRUE),
('manage_users', 'Can manage system users', 3, TRUE),
('view_reports', 'Can view system reports', 3, TRUE),
('view_patient_records', 'Can view patient medical records', 4, TRUE),
('prescribe_medication', 'Can prescribe medications', 4, TRUE),
('edit_patient_records', 'Can edit patient medical records', 4, TRUE),
('dispense_medication', 'Can dispense medications', 5, TRUE),
('view_inventory', 'Can view medication inventory', 5, TRUE),
('view_patient_records', 'Can view patient medical records', 6, TRUE),
('administer_medication', 'Can administer medications', 6, TRUE),
('view_patient_records', 'Can view patient medical records', 7, TRUE),
('prescribe_medication', 'Can prescribe medications', 7, TRUE),
('edit_patient_records', 'Can edit patient medical records', 7, TRUE),
('manage_users', 'Can manage system users', 8, TRUE),
('view_reports', 'Can view system reports', 8, TRUE),
('view_patient_records', 'Can view patient medical records', 9, TRUE),
('edit_patient_records', 'Can edit patient medical records', 9, TRUE),
('prescribe_medication', 'Can prescribe medications', 9, TRUE),
('view_patient_records', 'Can view patient medical records', 10, TRUE),
('administer_medication', 'Can administer medications', 10, TRUE),
('dispense_medication', 'Can dispense medications', 11, TRUE),
('view_inventory', 'Can view medication inventory', 11, TRUE),
('view_patient_records', 'Can view patient medical records', 12, TRUE),
('prescribe_medication', 'Can prescribe medications', 12, TRUE),
('edit_patient_records', 'Can edit patient medical records', 12, TRUE),
('view_patient_records', 'Can view patient medical records', 13, TRUE),
('administer_medication', 'Can administer medications', 13, TRUE),
('manage_users', 'Can manage system users', 14, TRUE),
('view_reports', 'Can view system reports', 14, TRUE),
('view_patient_records', 'Can view patient medical records', 15, TRUE),
('prescribe_medication', 'Can prescribe medications', 15, TRUE),
('edit_patient_records', 'Can edit patient medical records', 15, TRUE),
('dispense_medication', 'Can dispense medications', 16, TRUE),
('view_inventory', 'Can view medication inventory', 16, TRUE),
('view_patient_records', 'Can view patient medical records', 17, TRUE);