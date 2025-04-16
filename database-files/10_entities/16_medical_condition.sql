-- Sample data for MEDICAL_CONDITION table
-- Create 30-40 rows as specified in requirements

USE meditrack;

-- Insert sample medical conditions here
-- Example:
-- INSERT INTO MEDICAL_CONDITION (condition_id, condition_name, description, icd_code, is_chronic)
-- VALUES (1, 'Hypertension', 'Persistently elevated blood pressure in the arteries', 'I10', TRUE);

INSERT INTO MEDICAL_CONDITION (condition_id, condition_name, description, icd_code, is_chronic) VALUES
(1, 'Hypertension', 'Persistently elevated blood pressure in the arteries', 'I10', TRUE),
(2, 'Type 2 Diabetes', 'Chronic condition affecting insulin regulation', 'E11', TRUE),
(3, 'Asthma', 'Chronic respiratory condition causing airway inflammation', 'J45', TRUE),
(4, 'Coronary Artery Disease', 'Narrowing of coronary arteries reducing blood flow to heart', 'I25', TRUE),
(5, 'Chronic Obstructive Pulmonary Disease', 'Progressive lung disease obstructing airflow', 'J44', TRUE),
(6, 'Rheumatoid Arthritis', 'Autoimmune disorder causing joint inflammation', 'M06', TRUE),
(7, 'Hyperlipidemia', 'Elevated levels of lipids in the blood', 'E78', TRUE),
(8, 'Chronic Kidney Disease', 'Gradual loss of kidney function over time', 'N18', TRUE),
(9, 'Osteoarthritis', 'Degenerative joint disease causing cartilage breakdown', 'M19', TRUE),
(10, 'Migraine', 'Recurrent headaches with neurological symptoms', 'G43', TRUE),
(11, 'Gastroesophageal Reflux Disease', 'Chronic acid reflux causing esophageal irritation', 'K21', TRUE),
(12, 'Atrial Fibrillation', 'Irregular and rapid heart rate', 'I48', TRUE),
(13, 'Hypothyroidism', 'Underactive thyroid gland reducing hormone production', 'E03', TRUE),
(14, 'Psoriasis', 'Chronic autoimmune skin condition causing scaly patches', 'L40', TRUE),
(15, 'Anxiety Disorder', 'Persistent excessive worry and fear', 'F41', TRUE),
(16, 'Major Depressive Disorder', 'Persistent low mood and loss of interest', 'F32', TRUE),
(17, 'Irritable Bowel Syndrome', 'Chronic disorder affecting the large intestine', 'K58', TRUE),
(18, 'Heart Failure', 'Heart’s inability to pump blood effectively', 'I50', TRUE),
(19, 'Epilepsy', 'Neurological disorder causing recurrent seizures', 'G40', TRUE),
(20, 'Crohn’s Disease', 'Chronic inflammatory bowel disease', 'K50', TRUE),
(21, 'Ulcerative Colitis', 'Chronic inflammation of the colon and rectum', 'K51', TRUE),
(22, 'Parkinson’s Disease', 'Progressive neurological disorder affecting movement', 'G20', TRUE),
(23, 'Multiple Sclerosis', 'Autoimmune disease affecting the central nervous system', 'G暂时中断35', TRUE),
(24, 'Chronic Sinusitis', 'Persistent inflammation of the sinuses', 'J32', TRUE),
(25, 'Allergic Rhinitis', 'Nasal inflammation due to allergens', 'J30', FALSE),
(26, 'Bronchitis', 'Inflammation of the bronchial tubes', 'J40', FALSE),
(27, 'Pneumonia', 'Infection causing lung inflammation', 'J18', FALSE),
(28, 'Urinary Tract Infection', 'Bacterial infection in the urinary system', 'N39.0', FALSE),
(29, 'Gastritis', 'Inflammation of the stomach lining', 'K29', FALSE),
(30, 'Acute Appendicitis', 'Inflammation of the appendix', 'K35', FALSE),
(31, 'Influenza', 'Viral infection affecting the respiratory system', 'J11', FALSE),
(32, 'Conjunctivitis', 'Inflammation of the eye’s conjunctiva', 'H10', FALSE),
(33, 'Otitis Media', 'Middle ear infection', 'H66', FALSE),
(34, 'Tonsillitis', 'Inflammation of the tonsils', 'J03', FALSE),
(35, 'Cellulitis', 'Bacterial skin infection', 'L03', FALSE),
(36, 'Sprained Ankle', 'Ligament injury in the ankle', 'S93.4', FALSE),
(37, 'Tendinitis', 'Inflammation of a tendon', 'M77', FALSE),
(38, 'Viral Gastroenteritis', 'Viral infection causing gastrointestinal symptoms', 'A08', FALSE),
(39, 'Herniated Disc', 'Displacement of spinal disc material', 'M51', TRUE),
(40, 'Sleep Apnea', 'Breathing interruptions during sleep', 'G47.3', TRUE);