-- Sample data for CARE_TASKS table
-- Create 50-75 rows as specified in requirements

USE meditrack;

-- Insert sample care tasks here
-- Example:
-- INSERT INTO CARE_TASKS (task_id, task_name, description, priority, estimated_duration)
-- VALUES (1, 'Blood Pressure Check', 'Measure and record patient blood pressure', 'HIGH', 10);

INSERT INTO CARE_TASKS (task_id, task_name, description, priority, estimated_duration) VALUES
(1, 'Blood Pressure Check', 'Measure and record patient blood pressure', 'HIGH', 10),
(2, 'Glucose Monitoring', 'Check and record patient blood glucose levels', 'HIGH', 10),
(3, 'Medication Administration', 'Administer prescribed medication to patient', 'HIGH', 15),
(4, 'Inhaler Administration', 'Assist patient with inhaler use for asthma', 'MEDIUM', 10),
(5, 'Wound Dressing Change', 'Clean and redress patient wound', 'HIGH', 20),
(6, 'IV Line Check', 'Inspect and maintain IV line', 'HIGH', 15),
(7, 'Oxygen Saturation Check', 'Measure patient oxygen levels using pulse oximeter', 'MEDIUM', 5),
(8, 'Patient Mobility Assistance', 'Assist patient with walking or repositioning', 'MEDIUM', 20),
(9, 'Vital Signs Monitoring', 'Record patient temperature, pulse, and respiration', 'HIGH', 15),
(10, 'Catheter Care', 'Clean and maintain urinary catheter', 'HIGH', 20),
(11, 'Dietary Intake Monitoring', 'Track and record patient food and fluid intake', 'LOW', 10),
(12, 'Pain Assessment', 'Evaluate and document patient pain levels', 'MEDIUM', 10),
(13, 'Blood Draw', 'Collect blood sample for lab testing', 'HIGH', 15),
(14, 'EKG Monitoring', 'Perform electrocardiogram to monitor heart activity', 'HIGH', 20),
(15, 'Nebulizer Treatment', 'Administer nebulizer treatment for respiratory issues', 'MEDIUM', 15),
(16, 'Patient Education Session', 'Educate patient on condition or treatment plan', 'MEDIUM', 30),
(17, 'Suture Removal', 'Remove stitches from healed wound', 'MEDIUM', 15),
(18, 'Injection Administration', 'Administer intramuscular or subcutaneous injection', 'HIGH', 10),
(19, 'Falls Risk Assessment', 'Evaluate patient for fall risk and implement precautions', 'MEDIUM', 15),
(20, 'Skin Integrity Check', 'Inspect patient skin for pressure ulcers or breakdown', 'MEDIUM', 15),
(21, 'Respiratory Assessment', 'Evaluate patient breathing and lung sounds', 'HIGH', 10),
(22, 'Fluid Balance Monitoring', 'Track patient fluid input and output', 'MEDIUM', 10),
(23, 'Bowel Movement Tracking', 'Record patient bowel movements and consistency', 'LOW', 5),
(24, 'Physical Therapy Session', 'Assist patient with prescribed physical therapy exercises', 'MEDIUM', 30),
(25, 'Dressing Assistance', 'Help patient with dressing and grooming', 'LOW', 20),
(26, 'Weight Measurement', 'Measure and record patient weight', 'LOW', 5),
(27, 'Seizure Monitoring', 'Observe and document seizure activity', 'HIGH', 15),
(28, 'Chest Tube Monitoring', 'Check chest tube function and drainage', 'HIGH', 20),
(29, 'Tracheostomy Care', 'Clean and maintain tracheostomy site', 'HIGH', 20),
(30, 'Feeding Tube Care', 'Maintain and clean feeding tube', 'HIGH', 15),
(31, 'Allergy Assessment', 'Review and document patient allergies', 'MEDIUM', 10),
(32, 'Mental Status Assessment', 'Evaluate patient cognitive and emotional state', 'MEDIUM', 15),
(33, 'Cast Care', 'Inspect and maintain patient cast', 'MEDIUM', 10),
(34, 'Compression Therapy', 'Apply compression stockings or bandages', 'MEDIUM', 15),
(35, 'Oxygen Therapy Monitoring', 'Check oxygen delivery and patient response', 'HIGH', 10),
(36, 'Colostomy Care', 'Clean and change colostomy bag', 'HIGH', 20),
(37, 'Sleep Apnea Monitoring', 'Ensure CPAP machine is functioning and used correctly', 'MEDIUM', 10),
(38, 'Post-Surgical Site Check', 'Inspect surgical site for infection or complications', 'HIGH', 15),
(39, 'Urine Sample Collection', 'Collect urine sample for diagnostic testing', 'MEDIUM', 10),
(40, 'Patient Hygiene Assistance', 'Assist with bathing and personal hygiene', 'LOW', 30);