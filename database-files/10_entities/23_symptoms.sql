-- Sample data for SYMPTOMS table
-- Create 50-75 rows as specified in requirements

USE meditrack;

-- Insert sample symptoms here
-- Example:
-- INSERT INTO SYMPTOMS (symptom_id, symptom_name, description, severity_code)
-- VALUES (1, 'Headache', 'Pain in the head or upper neck', 'MILD-MOD');

INSERT INTO SYMPTOMS (symptom_id, symptom_name, description, severity_code) VALUES
(1, 'Headache', 'Pain in the head or upper neck', 'MILD-MOD'),
(2, 'Fatigue', 'Persistent tiredness or lack of energy', 'MILD-MOD'),
(3, 'Cough', 'Sudden expulsion of air from the lungs', 'MOD'),
(4, 'Fever', 'Elevated body temperature above normal range', 'MOD-SEV'),
(5, 'Shortness of Breath', 'Difficulty breathing or feeling of suffocation', 'MOD-SEV'),
(6, 'Chest Pain', 'Pain or discomfort in the chest area', 'SEV'),
(7, 'Joint Pain', 'Pain or stiffness in the joints', 'MILD-MOD'),
(8, 'Nausea', 'Feeling of unease and urge to vomit', 'MILD-MOD'),
(9, 'Abdominal Pain', 'Pain in the stomach or abdominal region', 'MOD-SEV'),
(10, 'Dizziness', 'Sensation of spinning or loss of balance', 'MILD-MOD'),
(11, 'Sore Throat', 'Pain or irritation in the throat', 'MILD'),
(12, 'Rash', 'Skin eruption or discoloration', 'MILD-MOD'),
(13, 'Muscle Pain', 'Aching or soreness in muscles', 'MILD-MOD'),
(14, 'Swelling', 'Enlargement or puffiness in a body part', 'MOD'),
(15, 'Palpitations', 'Rapid or irregular heartbeat sensation', 'MOD-SEV'),
(16, 'Wheezing', 'High-pitched breathing sound', 'MOD-SEV'),
(17, 'Diarrhea', 'Frequent loose or watery stools', 'MOD'),
(18, 'Constipation', 'Infrequent or difficult bowel movements', 'MILD-MOD'),
(19, 'Itching', 'Unpleasant skin sensation prompting scratching', 'MILD'),
(20, 'Back Pain', 'Pain in the lower or upper back', 'MILD-MOD'),
(21, 'Loss of Appetite', 'Reduced desire to eat', 'MILD-MOD'),
(22, 'Night Sweats', 'Excessive sweating during sleep', 'MOD'),
(23, 'Tremors', 'Involuntary shaking or trembling', 'MOD-SEV'),
(24, 'Blurred Vision', 'Loss of sharpness in vision', 'MOD-SEV'),
(25, 'Tinnitus', 'Ringing or buzzing in the ears', 'MILD-MOD'),
(26, 'Numbness', 'Loss of sensation in a body part', 'MOD-SEV'),
(27, 'Heartburn', 'Burning sensation in the chest from acid reflux', 'MILD-MOD'),
(28, 'Frequent Urination', 'Need to urinate more often than usual', 'MILD-MOD'),
(29, 'Weight Loss', 'Unintentional reduction in body weight', 'MOD-SEV'),
(30, 'Weight Gain', 'Unintentional increase in body weight', 'MILD-MOD'),
(31, 'Dry Mouth', 'Lack of saliva causing mouth dryness', 'MILD'),
(32, 'Insomnia', 'Difficulty falling or staying asleep', 'MILD-MOD'),
(33, 'Anxiety', 'Feelings of nervousness or unease', 'MOD'),
(34, 'Depression', 'Persistent sadness or low mood', 'MOD-SEV'),
(35, 'Chills', 'Feeling cold with shivering', 'MILD-MOD'),
(36, 'Confusion', 'Disorientation or difficulty thinking clearly', 'SEV'),
(37, 'Skin Redness', 'Red or inflamed appearance of skin', 'MILD-MOD'),
(38, 'Hoarseness', 'Rough or strained voice', 'MILD'),
(39, 'Bloating', 'Feeling of fullness or swelling in abdomen', 'MILD-MOD'),
(40, 'Nasal Congestion', 'Blocked or stuffy nose', 'MILD-MOD');