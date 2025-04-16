-- Sample data for LAB_RESULTS table
-- Create 50-75 rows as specified in requirements

USE meditrack;

-- Insert sample lab results here
-- Example:
-- INSERT INTO LAB_RESULTS (result_id, patient_id, test_name, test_date, result_date, result_value, reference_range, unit_of_measure, is_abnormal, lab_notes)
-- VALUES (1, 101, 'Complete Blood Count', '2023-06-01', '2023-06-02', '14.5', '12.0-15.5', 'g/dL', FALSE, 'Results within normal range');

INSERT INTO LAB_RESULTS (result_id, patient_id, test_name, test_date, result_date, result_value, reference_range, unit_of_measure, is_abnormal, lab_notes) VALUES
(1, 101, 'Complete Blood Count', '2023-06-01', '2023-06-02', '14.5', '12.0-15.5', 'g/dL', FALSE, 'Results within normal range'),
(2, 101, 'Blood Glucose', '2023-06-01', '2023-06-02', '110', '70-99', 'mg/dL', TRUE, 'Elevated fasting glucose'),
(3, 102, 'Lipid Panel', '2023-07-10', '2023-07-11', '200', '<200', 'mg/dL', TRUE, 'Elevated total cholesterol'),
(4, 102, 'Hemoglobin A1c', '2023-07-10', '2023-07-11', '6.5', '<5.7', '%', TRUE, 'Indicates prediabetes'),
(5, 103, 'Thyroid Stimulating Hormone', '2023-08-15', '2023-08-16', '3.2', '0.4-4.0', 'mIU/L', FALSE, 'Normal thyroid function'),
(6, 103, 'Basic Metabolic Panel', '2023-08-15', '2023-08-16', '135', '135-145', 'mmol/L', FALSE, 'Sodium levels normal'),
(7, 104, 'internals(7, 'Complete Blood Count', '2023-09-05', '2023-09-06', '13.8', '12.0-15.5', 'g/dL', FALSE, 'Normal hemoglobin levels'),
(8, 104, 'Liver Function Test', '2023-09-05', '2023-09-06', '0.9', '0.2-1.0', 'mg/dL', FALSE, 'Normal bilirubin levels'),
(9, 105, 'Lipid Panel', '2023-10-01', '2023-10-02', '180', '<200', 'mg/dL', FALSE, 'Cholesterol within range'),
(10, 105, 'Blood Glucose', '2023-10-01', '2023-10-02', '95', '70-99', 'mg/dL', FALSE, 'Normal fasting glucose'),
(11, 106, 'Urinalysis', '2023-11-12', '2023-11-13', 'Negative', 'Negative', NULL, FALSE, 'No signs of infection'),
(12, 106, 'C-Reactive Protein', '2023-11-12', '2023-11-13', '2.5', '<3.0', 'mg/L', FALSE, 'No significant inflammation'),
(13, 107, 'Complete Blood Count', '2023-12-01', '2023-12-02', '15.0', '12.0-15.5', 'g/dL', FALSE, 'Normal results'),
(14, 107, 'Electrolyte Panel', '2023-12-01', '2023-12-02', '4.5', '3.5-5.0', 'mmol/L', FALSE, 'Normal potassium levels'),
(15, 108, 'Hemoglobin A1c', '2024-01-15', '2024-01-16', '7.0', '<5.7', '%', TRUE, 'Indicates diabetes'),
(16, 108, 'Kidney Function Test', '2024-01-15', '2024-01-16', '1.0', '0.6-1.2', 'mg/dL', FALSE, 'Normal creatinine levels'),
(17, 109, 'Lipid Panel', '2024-02-10', '2024-02-11', '210', '<200', 'mg/dL', TRUE, 'Elevated LDL cholesterol'),
(18, 109, 'Thyroid Panel', '2024-02-10', '2024-02-11', '5.5', '0.4-4.0', 'mIU/L', TRUE, 'Elevated TSH, possible hypothyroidism'),
(19, 110, 'Blood Glucose', '2024-03-05', '2024-03-06', '120', '70-99', 'mg/dL', TRUE, 'Elevated glucose, follow-up needed'),
(20, 110, 'Complete Blood Count', '2024-03-05', '2024-03-06', '12.5', '12.0-15.5', 'g/dL', FALSE, 'Normal hemoglobin'),
(21, 111, 'Liver Function Test', '2024-04-01', '2024-04-02', '1.2', '0.2-1.0', 'mg/dL', TRUE, 'Slightly elevated bilirubin'),
(22, 111, 'Basic Metabolic Panel', '2024-04-01', '2024-04-02', '140', '135-145', 'mmol/L', FALSE, 'Normal sodium levels'),
(23, 112, 'Urinalysis', '2024-05-10', '2024-05-11', 'Positive', 'Negative', NULL, TRUE, 'Possible UTI, culture ordered'),
(24, 112, 'C-Reactive Protein', '2024-05-10', '2024-05-11', '5.0', '<3.0', 'mg/L', TRUE, 'Mild inflammation detected'),
(25, 113, 'Complete Blood Count', '2024-06-15', '2024-06-16', '14.0', '12.0-15.5', 'g/dL', FALSE, 'Normal results'),
(26, 113, 'Blood Glucose', '2024-06-15', '2024-06-16', '90', '70-99', 'mg/dL', FALSE, 'Normal fasting glucose'),
(27, 114, 'Lipid Panel', '2024-07-01', '2024-07-02', '190', '<200', 'mg/dL', FALSE, 'Cholesterol within range'),
(28, 114, 'Hemoglobin A1c', '2024-07-01', '2024-07-02', '5.5', '<5.7', '%', FALSE, 'Normal A1c'),
(29, 115, 'Thyroid Stimulating Hormone', '2024-08-10', '2024-08-11', '2.8', '0.4-4.0', 'mIU/L', FALSE, 'Normal thyroid function'),
(30, 115, 'Kidney Function Test', '2024-08-10', '2024-08-11', '0.8', '0.6-1.2', 'mg/dL', FALSE, 'Normal creatinine'),
(31, 116, 'Complete Blood Count', '2024-09-05', '2024-09-06', '13.5', '12.0-15.5', 'g/dL', FALSE, 'Normal hemoglobin'),
(32, 116, 'Electrolyte Panel', '2024-09-05', '2024-09-06', '4.0', '3.5-5.0', 'mmol/L', FALSE, 'Normal potassium'),
(33, 117, 'Blood Glucose', '2024-10-01', '2024-10-02', '115', '70-99', 'mg/dL', TRUE, 'Elevated glucose, monitor closely'),
(34, 117, 'Liver Function Test', '2024-10-01', '2024-10-02', '0.7', '0.2-1.0', 'mg/dL', FALSE, 'Normal bilirubin'),
(35, 118, 'Urinalysis', '2024-11-12', '2024-11-13', 'Negative', 'Negative', NULL, FALSE, 'No abnormalities'),
(36, 118, 'C-Reactive Protein', '2024-11-12', '2024-11-13', '1.5', '<3.0', 'mg/L', FALSE, 'No significant inflammation'),
(37, 119, 'Complete Blood Count', '2024-12-01', '2024-12-02', '14.8', '12.0-15.5', 'g/dL', FALSE, 'Normal results'),
(38, 119, 'Lipid Panel', '2024-12-01', '2024-12-02', '220', '<200', 'mg/dL', TRUE, 'Elevated cholesterol, lifestyle changes advised'),
(39, 120, 'Hemoglobin A1c', '2025-01-15', '2025-01-16', '6.0', '<5.7', '%', TRUE, 'Prediabetes, follow-up recommended'),
(40, 120, 'Kidney Function Test', '2025-01-15', '2025-01-16', '1.1', '0.6-1.2', 'mg/dL', FALSE, 'Normal creatinine levels');