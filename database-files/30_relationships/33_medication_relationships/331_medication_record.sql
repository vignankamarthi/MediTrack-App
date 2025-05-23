-- Sample data for medication_record bridge table
-- Create 125+ rows as specified in requirements

USE meditrack;

-- Insert sample patient-medication relationships here
-- Example:
-- INSERT INTO medication_record (patient_id, medication_id, dosage, frequency)
-- VALUES (101, 1, '10mg', 'DAILY');

USE meditrack;

INSERT INTO medication_record (patient_id, medication_id, dosage, frequency) VALUES
(101, 1, '10mg', 'DAILY'),
(101, 4, '20mg', 'DAILY'),
(101, 7, '20mg', 'DAILY'),
(102, 3, '2 puffs', 'TWICE DAILY'),
(102, 8, '50mg', 'DAILY'),
(102, 20, '10mg', 'DAILY'),
(103, 5, '5mg', 'DAILY'),
(103, 9, '25mg', 'DAILY'),
(103, 22, '75mg', 'DAILY'),
(104, 2, '500mg', 'TWICE DAILY'),
(104, 10, '200mg', 'AS NEEDED'),
(104, 18, '20mg', 'DAILY'),
(105, 6, '50mcg', 'DAILY'),
(105, 11, '300mg', 'THREE TIMES DAILY'),
(105, 21, '40mg', 'DAILY'),
(106, 17, '50mcg', 'DAILY'),
(106, 26, '50mcg', 'TWICE DAILY'),
(106, 36, '10mg', 'DAILY'),
(107, 1, '10mg', 'DAILY'),
(107, 12, '10mg', 'DAILY'),
(107, 25, '500mg', 'AS NEEDED'),
(108, 7, '20mg', 'DAILY'),
(108, 13, '500mg', 'THREE TIMES DAILY'),
(108, 28, '30mg', 'DAILY'),
(109, 8, '50mg', 'DAILY'),
(109, 19, '5mg', 'DAILY'),
(109, 27, '50mg', 'DAILY'),
(110, 4, '20mg', 'DAILY'),
(110, 16, '1mg', 'AS NEEDED'),
(110, 23, '40mg', 'DAILY'),
(111, 5, '5mg', 'DAILY'),
(111, 9, '25mg', 'DAILY'),
(111, 31, '40mg', 'DAILY'),
(112, 3, '2 puffs', 'TWICE DAILY'),
(112, 20, '10mg', 'DAILY'),
(112, 32, '150mg', 'DAILY'),
(113, 2, '500mg', 'TWICE DAILY'),
(113, 10, '200mg', 'AS NEEDED'),
(113, 24, '2.5mg', 'WEEKLY'),
(114, 7, '20mg', 'DAILY'),
(114, 17, '50mcg', 'DAILY'),
(114, 30, '250mg', 'DAILY'),
(115, 1, '10mg', 'DAILY'),
(115, 21, '40mg', 'DAILY'),
(115, 33, '20mg', 'DAILY'),
(116, 4, '20mg', 'DAILY'),
(116, 8, '50mg', 'DAILY'),
(116, 25, '500mg', 'AS NEEDED'),
(117, 5, '5mg', 'DAILY'),
(117, 12, '10mg', 'DAILY'),
(117, 27, '50mg', 'DAILY'),
(118, 3, '2 puffs', 'TWICE DAILY'),
(118, 18, '20mg', 'DAILY'),
(118, 36, '10mg', 'DAILY'),
(119, 6, '50mcg', 'DAILY'),
(119, 11, '300mg', 'THREE TIMES DAILY'),
(119, 23, '40mg', 'DAILY'),
(120, 2, '500mg', 'TWICE DAILY'),
(120, 9, '25mg', 'DAILY'),
(120, 28, '30mg', 'DAILY'),
(121, 1, '10mg', 'DAILY'),
(121, 4, '20mg', 'DAILY'),
(121, 22, '75mg', 'DAILY'),
(122, 7, '20mg', 'DAILY'),
(122, 17, '50mcg', 'DAILY'),
(122, 32, '150mg', 'DAILY'),
(123, 5, '5mg', 'DAILY'),
(123, 10, '200mg', 'AS NEEDED'),
(123, 27, '50mg', 'DAILY'),
(124, 3, '2 puffs', 'TWICE DAILY'),
(124, 20, '10mg', 'DAILY'),
(124, 25, '500mg', 'AS NEEDED'),
(125, 8, '50mg', 'DAILY'),
(125, 13, '500mg', 'THREE TIMES DAILY'),
(125, 31, '40mg', 'DAILY'),
(126, 2, '500mg', 'TWICE DAILY'),
(126, 9, '25mg', 'DAILY'),
(126, 23, '40mg', 'DAILY'),
(127, 1, '10mg', 'DAILY'),
(127, 21, '40mg', 'DAILY'),
(127, 33, '20mg', 'DAILY'),
(128, 4, '20mg', 'DAILY'),
(128, 17, '50mcg', 'DAILY'),
(128, 36, '10mg', 'DAILY'),
(129, 5, '5mg', 'DAILY'),
(129, 12, '10mg', 'DAILY'),
(129, 28, '30mg', 'DAILY'),
(130, 3, '2 puffs', 'TWICE DAILY'),
(130, 8, '50mg', 'DAILY'),
(130, 27, '50mg', 'DAILY'),
(131, 6, '50mcg', 'DAILY'),
(131, 11, '300mg', 'THREE TIMES DAILY'),
(131, 22, '75mg', 'DAILY'),
(132, 2, '500mg', 'TWICE DAILY'),
(132, 10, '200mg', 'AS NEEDED'),
(132, 23, '40mg', 'DAILY'),
(133, 1, '10mg', 'DAILY'),
(133, 9, '25mg', 'DAILY'),
(133, 31, '40mg', 'DAILY'),
(134, 7, '20mg', 'DAILY'),
(134, 20, '10mg', 'DAILY'),
(134, 36, '10mg', 'DAILY'),
(135, 4, '20mg', 'DAILY'),
(135, 21, '40mg', 'DAILY'),
(135, 27, '50mg', 'DAILY'),
(136, 3, '2 puffs', 'TWICE DAILY'),
(136, 8, '50mg', 'DAILY'),
(136, 25, '500mg', 'AS NEEDED'),
(137, 5, '5mg', 'DAILY'),
(137, 12, '10mg', 'DAILY'),
(137, 28, '30mg', 'DAILY'),
(138, 2, '500mg', 'TWICE DAILY'),
(138, 17, '50mcg', 'DAILY'),
(138, 33, '20mg', 'DAILY'),
(139, 6, '50mcg', 'DAILY'),
(139, 11, '300mg', 'THREE TIMES DAILY'),
(139, 23, '40mg', 'DAILY'),
(140, 1, '10mg', 'DAILY'),
(140, 9, '25mg', 'DAILY'),
(140, 27, '50mg', 'DAILY');