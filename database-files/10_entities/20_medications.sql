-- Sample data for MEDICATIONS table
-- Create 30-40 rows as specified in requirements

USE meditrack;

-- Insert sample medications here
-- Example:
-- INSERT INTO MEDICATIONS (medication_id, medication_name, generic_name, medication_class, dosage_form, strength, manufacturer, ndc_code, is_controlled, control_class)
-- VALUES (1, 'Lisinopril', 'Lisinopril', 'ACE Inhibitor', 'Tablet', '10mg', 'PharmaCorp', 'NDC12345-678-90', FALSE, NULL);


INSERT INTO MEDICATIONS (medication_id, medication_name, generic_name, medication_class, dosage_form, strength, manufacturer, ndc_code, is_controlled, control_class) VALUES
(1, 'Lisinopril', 'Lisinopril', 'ACE Inhibitor', 'Tablet', '10mg', 'PharmaCorp', 'NDC12345-678-90', FALSE, NULL),
(2, 'Metformin', 'Metformin', 'Biguanide', 'Tablet', '500mg', 'GlucoPharm', 'NDC23456-789-01', FALSE, NULL),
(3, 'Albuterol', 'Albuterol Sulfate', 'Beta-2 Agonist', 'Inhaler', '90mcg', 'RespiraMed', 'NDC34567-890-12', FALSE, NULL),
(4, 'Atorvastatin', 'Atorvastatin', 'Statin', 'Tablet', '20mg', 'LipidCare', 'NDC45678-901-23', FALSE, NULL),
(5, 'Amlodipine', 'Amlodipine', 'Calcium Channel Blocker', 'Tablet', '5mg', 'CardioPharm', 'NDC56789-012-34', FALSE, NULL),
(6, 'Levothyroxine', 'Levothyroxine', 'Thyroid Hormone', 'Tablet', '50mcg', 'EndoPharm', 'NDC67890-123-45', FALSE, NULL),
(7, 'Omeprazole', 'Omeprazole', 'Proton Pump Inhibitor', 'Capsule', '20mg', 'GastroMed', 'NDC78901-234-56', FALSE, NULL),
(8, 'Sertraline', 'Sertraline', 'SSRI', 'Tablet', '50mg', 'NeuroPharm', 'NDC89012-345-67', FALSE, NULL),
(9, 'Hydrochlorothiazide', 'Hydrochlorothiazide', 'Diuretic', 'Tablet', '25mg', 'AquaPharm', 'NDC90123-456-78', FALSE, NULL),
(10, 'Ibuprofen', 'Ibuprofen', 'NSAID', 'Tablet', '200mg', 'PainRelief', 'NDC01234-567-89', FALSE, NULL),
(11, 'Gabapentin', 'Gabapentin', 'Anticonvulsant', 'Capsule', '300mg', 'NeuroCare', 'NDC12345-678-01', FALSE, NULL),
(12, 'Prednisone', 'Prednisone', 'Corticosteroid', 'Tablet', '10mg', 'InflameAway', 'NDC23456-789-12', FALSE, NULL),
(13, 'Amoxicillin', 'Amoxicillin', 'Antibiotic', 'Capsule', '500mg', 'InfectoPharm', 'NDC34567-890-23', FALSE, NULL),
(14, 'Morphine', 'Morphine Sulfate', 'Opioid Analgesic', 'Tablet', '15mg', 'PainControl', 'NDC45678-901-34', TRUE, 'CII'),
(15, 'Oxycodone', 'Oxycodone', 'Opioid Analgesic', 'Tablet', '5mg', 'PainControl', 'NDC56789-012-45', TRUE, 'CII'),
(16, 'Lorazepam', 'Lorazepam', 'Benzodiazepine', 'Tablet', '1mg', 'CalmPharm', 'NDC67890-123-56', TRUE, 'CIV'),
(17, 'Fluticasone', 'Fluticasone Propionate', 'Corticosteroid', 'Inhaler', '50mcg', 'RespiraMed', 'NDC78901-234-67', FALSE, NULL),
(18, 'Citalopram', 'Citalopram', 'SSRI', 'Tablet', '20mg', 'NeuroPharm', 'NDC89012-345-78', FALSE, NULL),
(19, 'Warfarin', 'Warfarin', 'Anticoagulant', 'Tablet', '5mg', 'BloodCare', 'NDC90123-456-89', FALSE, NULL),
(20, 'Montelukast', 'Montelukast', 'Leukotriene Inhibitor', 'Tablet', '10mg', 'RespiraMed', 'NDC01234-567-90', FALSE, NULL),
(21, 'Furosemide', 'Furosemide', 'Loop Diuretic', 'Tablet', '40mg', 'AquaPharm', 'NDC12345-678-12', FALSE, NULL),
(22, 'Clopidogrel', 'Clopidogrel', 'Antiplatelet', 'Tablet', '75mg', 'CardioPharm', 'NDC23456-789-23', FALSE, NULL),
(23, 'Pantoprazole', 'Pantoprazole', 'Proton Pump Inhibitor', 'Tablet', '40mg', 'GastroMed', 'NDC34567-890-34', FALSE, NULL),
(24, 'Methotrexate', 'Methotrexate', 'DMARD', 'Tablet', '2.5mg', 'ArthroPharm', 'NDC45678-901-45', FALSE, NULL),
(25, 'Acetaminophen', 'Acetaminophen', 'Analgesic', 'Tablet', '500mg', 'PainRelief', 'NDC56789-012-56', FALSE, NULL),
(26, 'Salmeterol', 'Salmeterol', 'Beta-2 Agonist', 'Inhaler', '50mcg', 'RespiraMed', 'NDC67890-123-67', FALSE, NULL),
(27, 'Losartan', 'Losartan', 'Angiotensin II Receptor Blocker', 'Tablet', '50mg', 'CardioPharm', 'NDC78901-234-78', FALSE, NULL),
(28, 'Duloxetine', 'Duloxetine', 'SNRI', 'Capsule', '30mg', 'NeuroPharm', 'NDC89012-345-89', FALSE, NULL),
(29, 'Tamsulosin', 'Tamsulosin', 'Alpha Blocker', 'Capsule', '0.4mg', 'UroPharm', 'NDC90123-456-90', FALSE, NULL),
(30, 'Azithromycin', 'Azithromycin', 'Macrolide Antibiotic', 'Tablet', '250mg', 'InfectoPharm', 'NDC01234-567-01', FALSE, NULL),
(31, 'Simvastatin', 'Simvastatin', 'Statin', 'Tablet', '40mg', 'LipidCare', 'NDC12345-678-23', FALSE, NULL),
(32, 'Bupropion', 'Bupropion', 'Atypical Antidepressant', 'Tablet', '150mg', 'NeuroPharm', 'NDC23456-789-34', FALSE, NULL),
(33, 'Rivaroxaban', 'Rivaroxaban', 'Anticoagulant', 'Tablet', '20mg', 'BloodCare', 'NDC34567-890-45', FALSE, NULL),
(34, 'Budesonide', 'Budesonide', 'Corticosteroid', 'Inhaler', '100mcg', 'RespiraMed', 'NDC45678-901-56', FALSE, NULL),
(35, 'Tramadol', 'Tramadol', 'Opioid Analgesic', 'Tablet', '50mg', 'PainControl', 'NDC56789-012-67', TRUE, 'CIV'),
(36, 'Cetirizine', 'Cetirizine', 'Antihistamine', 'Tablet', '10mg', 'AllergyPharm', 'NDC67890-123-78', FALSE, NULL),
(37, 'Mesalamine', 'Mesalamine', 'Anti-inflammatory', 'Tablet', '800mg', 'GastroMed', 'NDC78901-234-89', FALSE, NULL),
(38, 'Carvedilol', 'Carvedilol', 'Beta Blocker', 'Tablet', '12.5mg', 'CardioPharm', 'NDC89012-345-90', FALSE, NULL),
(39, 'Levofloxacin', 'Levofloxacin', 'Fluoroquinolone Antibiotic', 'Tablet', '500mg', 'InfectoPharm', 'NDC90123-456-01', FALSE, NULL),
(40, 'Adalimumab', 'Adalimumab', 'TNF Inhibitor', 'Injection', '40mg', 'ArthroPharm', 'NDC01234-567-12', FALSE, NULL);