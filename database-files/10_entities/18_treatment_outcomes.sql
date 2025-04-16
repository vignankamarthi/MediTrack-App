-- Sample data for TREATMENT_OUTCOMES table
-- Create 50-75 rows as specified in requirements

USE meditrack;

-- Insert sample treatment outcomes here
-- Example:
-- INSERT INTO TREATMENT_OUTCOMES (outcome_id, treatment_id, outcome_name, description, is_positive)
-- VALUES (1, 1, 'Reduced Blood Pressure', 'Patient blood pressure decreased to normal range', TRUE);

INSERT INTO TREATMENT_OUTCOMES (outcome_id, treatment_id, outcome_name, description, is_positive) VALUES
(1, 1, 'Reduced Blood Pressure', 'Patient blood pressure decreased to normal range', TRUE),
(2, 1, 'Dizziness', 'Patient experienced mild dizziness as side effect', FALSE),
(3, 2, 'Stabilized Blood Glucose', 'Patient blood sugar levels stabilized', TRUE),
(4, 2, 'Hypoglycemia', 'Patient experienced low blood sugar episodes', FALSE),
(5, 3, 'Improved Breathing', 'Patient reported easier breathing and fewer asthma attacks', TRUE),
(6, 3, 'Throat Irritation', 'Patient experienced throat irritation from inhaler', FALSE),
(7, 4, 'Restored Blood Flow', 'Successful restoration of blood flow to heart', TRUE),
(8, 4, 'Bruising at Site', 'Patient had bruising at catheter insertion site', FALSE),
(9, 5, 'Reduced Wheezing', 'Patient experienced less wheezing and shortness of breath', TRUE),
(10, 5, 'Tremors', 'Patient reported mild tremors as side effect', FALSE),
(11, 6, 'Decreased Joint Pain', 'Patient reported reduced joint pain and stiffness', TRUE),
(12, 6, 'Gastrointestinal Upset', 'Patient experienced nausea and stomach discomfort', FALSE),
(13, 7, 'Lowered Cholesterol', 'Patient LDL cholesterol levels decreased significantly', TRUE),
(14, 7, 'Muscle Pain', 'Patient reported muscle soreness as side effect', FALSE),
(15, 8, 'Improved Kidney Function', 'Patient kidney function stabilized with regular dialysis', TRUE),
(16, 8, 'Fatigue', 'Patient experienced fatigue post-dialysis', FALSE),
(17, 9, 'Pain Relief', 'Patient reported significant reduction in joint pain', TRUE),
(18, 9, 'Injection Site Swelling', 'Patient had mild swelling at injection site', FALSE),
(19, 10, 'Migraine Relief', 'Patient reported reduced migraine frequency and intensity', TRUE),
(20, 10, 'Nausea', 'Patient experienced nausea as side effect', FALSE),
(21, 11, 'Reduced Acid Reflux', 'Patient reported fewer GERD symptoms', TRUE),
(22, 11, 'Headache', 'Patient experienced mild headaches', FALSE),
(23, 12, 'Regular Heart Rhythm', 'Patient heart rhythm stabilized', TRUE),
(24, 12, 'Fatigue', 'Patient reported tiredness as side effect', FALSE),
(25, 13, 'Normalized Thyroid Levels', 'Patient thyroid hormone levels returned to normal', TRUE),
(26, 13, 'Weight Gain', 'Patient experienced slight weight gain', FALSE),
(27, 14, 'Cleared Skin', 'Patient reported reduction in psoriatic lesions', TRUE),
(28, 14, 'Skin Irritation', 'Patient experienced mild skin irritation', FALSE),
(29, 15, 'Reduced Anxiety', 'Patient reported lower anxiety levels after therapy', TRUE),
(30, 15, 'Emotional Fatigue', 'Patient felt emotionally drained after sessions', FALSE),
(31, 16, 'Improved Mood', 'Patient reported better mood and reduced depressive symptoms', TRUE),
(32, 16, 'Insomnia', 'Patient experienced sleep disturbances', FALSE),
(33, 17, 'Reduced IBS Symptoms', 'Patient reported fewer IBS flare-ups', TRUE),
(34, 17, 'Diet Adjustment Difficulty', 'Patient struggled with dietary restrictions', FALSE),
(35, 18, 'Improved Heart Function', 'Patient reported better heart function and less shortness of breath', TRUE),
(36, 18, 'Swelling', 'Patient experienced mild edema as side effect', FALSE),
(37, 19, 'Seizure Control', 'Patient reported fewer seizures', TRUE),
(38, 19, 'Drowsiness', 'Patient experienced drowsiness as side effect', FALSE),
(39, 20, 'Reduced Inflammation', 'Patient reported decreased Crohn’s disease symptoms', TRUE),
(40, 20, 'Increased Infection Risk', 'Patient had higher susceptibility to infections', FALSE);