-- Sample data for TREATMENT table
-- Create 30-40 rows as specified in requirements

USE meditrack;

-- Insert sample treatments here
-- Example:
-- INSERT INTO TREATMENT (treatment_id, treatment_name, description, procedure_code, standard_duration, is_deprecated)
-- VALUES (1, 'ACE Inhibitor Therapy', 'Treatment using angiotensin-converting enzyme inhibitors', 'TX4567', 30, FALSE);


INSERT INTO TREATMENT (treatment_id, treatment_name, description, procedure_code, standard_duration, is_deprecated) VALUES
(1, 'ACE Inhibitor Therapy', 'Treatment using angiotensin-converting enzyme inhibitors for hypertension', 'TX4567', 30, FALSE),
(2, 'Insulin Therapy', 'Administration of insulin for diabetes management', 'TX1234', 60, FALSE),
(3, 'Inhaled Corticosteroids', 'Use of inhaled steroids for asthma control', 'TX7890', 30, FALSE),
(4, 'Coronary Angioplasty', 'Procedure to open blocked coronary arteries', 'TX2345', 120, FALSE),
(5, 'Bronchodilator Therapy', 'Use of bronchodilators for COPD symptom relief', 'TX3456', 15, FALSE),
(6, 'DMARD Therapy', 'Disease-modifying antirheumatic drugs for rheumatoid arthritis', 'TX5678', 90, FALSE),
(7, 'Statin Therapy', 'Use of statins to lower cholesterol levels', 'TX6789', 30, FALSE),
(8, 'Dialysis', 'Treatment to filter blood in kidney failure', 'TX8901', 240, FALSE),
(9, 'Joint Injection', 'Corticosteroid injection for osteoarthritis pain relief', 'TX9012', 15, FALSE),
(10, 'Triptan Therapy', 'Use of triptans for migraine relief', 'TX0123', 10, FALSE),
(11, 'Proton Pump Inhibitor Therapy', 'Use of PPIs for GERD symptom management', 'TX1235', 30, FALSE),
(12, 'Antiarrhythmic Therapy', 'Medications to manage atrial fibrillation', 'TX2346', 60, FALSE),
(13, 'Thyroid Hormone Replacement', 'Levothyroxine for hypothyroidism treatment', 'TX3457', 30, FALSE),
(14, 'Topical Corticosteroids', 'Application of steroids for psoriasis management', 'TX4568', 14, FALSE),
(15, 'Cognitive Behavioral Therapy', 'Psychotherapy for anxiety disorder management', 'TX5679', 60, FALSE),
(16, 'SSRI Therapy', 'Selective serotonin reuptake inhibitors for depression', 'TX6780', 30, FALSE),
(17, 'Dietary Management', 'Specialized diet for irritable bowel syndrome', 'TX7891', 90, FALSE),
(18, 'Diuretic Therapy', 'Use of diuretics for heart failure management', 'TX8902', 30, FALSE),
(19, 'Antiepileptic Therapy', 'Medications to control seizures in epilepsy', 'TX9013', 60, FALSE),
(20, 'Immunosuppressive Therapy', 'Medications to manage Crohn’s disease', 'TX0124', 90, FALSE),
(21, 'Mesalamine Therapy', 'Anti-inflammatory drugs for ulcerative colitis', 'TX1236', 30, FALSE),
(22, 'Dopamine Agonist Therapy', 'Medications to manage Parkinson’s disease symptoms', 'TX2347', 60, FALSE),
(23, 'Interferon Therapy', 'Immunomodulators for multiple sclerosis', 'TX3458', 90, FALSE),
(24, 'Nasal Irrigation', 'Saline irrigation for chronic sinusitis relief', 'TX4569', 10, FALSE),
(25, 'Antihistamine Therapy', 'Medications for allergic rhinitis symptom relief', 'TX5670', 14, FALSE),
(26, 'Antibiotic Therapy', 'Antibiotics for acute bronchitis', 'TX6781', 7, FALSE),
(27, 'IV Antibiotics', 'Intravenous antibiotics for pneumonia', 'TX7892', 10, FALSE),
(28, 'Oral Antibiotics', 'Antibiotics for urinary tract infection', 'TX8903', 7, FALSE),
(29, 'H2 Blocker Therapy', 'Histamine blockers for gastritis treatment', 'TX9014', 14, FALSE),
(30, 'Appendectomy', 'Surgical removal of the appendix', 'TX0125', 60, FALSE),
(31, 'Antiviral Therapy', 'Medications for influenza treatment', 'TX1237', 5, FALSE),
(32, 'Antibiotic Eye Drops', 'Topical antibiotics for conjunctivitis', 'TX2348', 7, FALSE),
(33, 'Ear Drops', 'Antibiotic drops for otitis media', 'TX3459', 7, FALSE),
(34, 'Tonsillectomy', 'Surgical removal of tonsils', 'TX4560', 60, FALSE),
(35, 'Antibiotic Ointment', 'Topical antibiotics for cellulitis', 'TX5671', 10, FALSE),
(36, 'Physical Therapy', 'Rehabilitation for sprained ankle', 'TX6782', 30, FALSE),
(37, 'Cortisone Injection', 'Steroid injection for tendinitis', 'TX7893', 15, FALSE),
(38, 'Fluid Replacement', 'Oral rehydration for viral gastroenteritis', 'TX8904', 3, FALSE),
(39, 'Spinal Decompression', 'Surgical procedure for herniated disc', 'TX9015', 120, FALSE),
(40, 'CPAP Therapy', 'Continuous positive airway pressure for sleep apnea', 'TX0126', 60, FALSE);