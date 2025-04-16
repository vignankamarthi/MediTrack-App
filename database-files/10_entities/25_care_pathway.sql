-- Sample data for CARE_PATHWAY table
-- Create 30-40 rows as specified in requirements

USE meditrack;

-- Insert sample care pathways here
-- Example:
-- INSERT INTO CARE_PATHWAY (pathway_id, pathway_name, description, standard_duration, is_active)
-- VALUES (1, 'Hypertension Management', 'Standard care pathway for managing hypertension', 90, TRUE);

USE meditrack;

INSERT INTO CARE_PATHWAY (pathway_id, pathway_name, description, standard_duration, is_active) VALUES
(1, 'Hypertension Management', 'Standard care pathway for managing hypertension', 90, TRUE),
(2, 'Type 2 Diabetes Care', 'Comprehensive care for Type 2 diabetes management', 120, TRUE),
(3, 'Asthma Control', 'Care pathway for asthma symptom management', 60, TRUE),
(4, 'Coronary Artery Disease Care', 'Management of coronary artery disease', 180, TRUE),
(5, 'COPD Management', 'Care pathway for chronic obstructive pulmonary disease', 90, TRUE),
(6, 'Rheumatoid Arthritis Care', 'Standard care for rheumatoid arthritis', 120, TRUE),
(7, 'Hyperlipidemia Management', 'Care pathway for managing elevated lipid levels', 90, TRUE),
(8, 'Chronic Kidney Disease Care', 'Comprehensive care for chronic kidney disease', 180, TRUE),
(9, 'Osteoarthritis Management', 'Care pathway for osteoarthritis treatment', 90, TRUE),
(10, 'Migraine Management', 'Care pathway for migraine prevention and treatment', 60, TRUE),
(11, 'GERD Management', 'Care pathway for gastroesophageal reflux disease', 60, TRUE),
(12, 'Atrial Fibrillation Care', 'Management of atrial fibrillation', 120, TRUE),
(13, 'Hypothyroidism Management', 'Care pathway for hypothyroidism treatment', 90, TRUE),
(14, 'Psoriasis Care', 'Care pathway for managing psoriasis', 90, TRUE),
(15, 'Anxiety Disorder Management', 'Care pathway for anxiety disorder treatment', 120, TRUE),
(16, 'Depression Care', 'Comprehensive care for major depressive disorder', 120, TRUE),
(17, 'IBS Management', 'Care pathway for irritable bowel syndrome', 90, TRUE),
(18, 'Heart Failure Management', 'Care pathway for heart failure treatment', 180, TRUE),
(19, 'Epilepsy Care', 'Care pathway for epilepsy management', 120, TRUE),
(20, 'Crohn’s Disease Care', 'Care pathway for managing Crohn’s disease', 120, TRUE),
(21, 'Ulcerative Colitis Care', 'Care pathway for ulcerative colitis management', 120, TRUE),
(22, 'Parkinson’s Disease Care', 'Care pathway for Parkinson’s disease management', 180, TRUE),
(23, 'Multiple Sclerosis Care', 'Care pathway for multiple sclerosis treatment', 180, TRUE),
(24, 'Chronic Sinusitis Management', 'Care pathway for chronic sinusitis', 60, TRUE),
(25, 'Allergic Rhinitis Management', 'Care pathway for allergic rhinitis treatment', 60, TRUE),
(26, 'Acute Bronchitis Care', 'Care pathway for acute bronchitis treatment', 30, TRUE),
(27, 'Pneumonia Recovery', 'Care pathway for pneumonia treatment and recovery', 30, TRUE),
(28, 'UTI Treatment', 'Care pathway for urinary tract infection', 14, TRUE),
(29, 'Gastritis Management', 'Care pathway for gastritis treatment', 30, TRUE),
(30, 'Appendicitis Post-Surgery Care', 'Care pathway for post-appendectomy recovery', 30, TRUE),
(31, 'Influenza Recovery', 'Care pathway for influenza treatment and recovery', 14, TRUE),
(32, 'Conjunctivitis Treatment', 'Care pathway for conjunctivitis management', 14, TRUE),
(33, 'Otitis Media Treatment', 'Care pathway for otitis media management', 14, TRUE),
(34, 'Tonsillitis Care', 'Care pathway for tonsillitis treatment', 14, TRUE),
(35, 'Cellulitis Treatment', 'Care pathway for cellulitis management', 14, TRUE),
(36, 'Sprained Ankle Recovery', 'Care pathway for sprained ankle rehabilitation', 30, TRUE),
(37, 'Tendinitis Management', 'Care pathway for tendinitis treatment', 30, TRUE),
(38, 'Viral Gastroenteritis Recovery', 'Care pathway for viral gastroenteritis', 14, TRUE),
(39, 'Herniated Disc Management', 'Care pathway for herniated disc treatment', 90, TRUE),
(40, 'Sleep Apnea Management', 'Care pathway for sleep apnea treatment', 120, TRUE);