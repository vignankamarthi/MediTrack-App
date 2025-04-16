-- Sample data for PRESCRIPTIONS table
-- Create 50-75 rows as specified in requirements

USE meditrack;

-- Insert sample prescriptions here
-- Example:
-- INSERT INTO PRESCRIPTIONS (prescription_id, prescriber_id, prescription_date, duration, refills, instructions, is_active)
-- VALUES (1, 1, '2023-05-15', 30, 2, 'Take one tablet by mouth daily with food', TRUE);

INSERT INTO PRESCRIPTIONS (prescription_id, prescriber_id, prescription_date, duration, refills, instructions, is_active) VALUES
(1, 1, '2023-05-15', 30, 2, 'Take one tablet by mouth daily with food', TRUE),
(2, 1, '2023-06-01', 60, 1, 'Take two tablets by mouth daily', TRUE),
(3, 4, '2023-07-10', 30, 3, 'Inhale two puffs twice daily', TRUE),
(4, 4, '2023-08-05', 90, 0, 'Take one tablet by mouth at bedtime', TRUE),
(5, 7, '2023-09-12', 30, 2, 'Take one tablet by mouth daily', TRUE),
(6, 7, '2023-10-01', 60, 1, 'Take one capsule by mouth daily', TRUE),
(7, 10, '2023-11-15', 30, 2, 'Take one tablet by mouth every morning', TRUE),
(8, 10, '2023-12-03', 90, 1, 'Inhale one puff daily', TRUE),
(9, 12, '2024-01-10', 30, 0, 'Take one tablet by mouth twice daily', TRUE),
(10, 12, '2024-02-05', 60, 2, 'Take one tablet by mouth daily with water', TRUE),
(11, 13, '2024-03-01', 30, 1, 'Take one capsule by mouth at night', TRUE),
(12, 13, '2024-04-15', 90, 0, 'Take two tablets by mouth daily', TRUE),
(13, 15, '2024-05-20', 30, 2, 'Take one tablet by mouth daily', TRUE),
(14, 15, '2024-06-10', 60, 1, 'Inhale two puffs every morning', TRUE),
(15, 16, '2024-07-05', 30, 3, 'Take one tablet by mouth daily with food', TRUE),
(16, 16, '2024-08-01', 90, 0, 'Take one capsule by mouth twice daily', TRUE),
(17, 19, '2024-09-12', 30, 2, 'Take one tablet by mouth daily', TRUE),
(18, 19, '2024-10-03', 60, 1, 'Take one tablet by mouth at bedtime', TRUE),
(19, 22, '2024-11-15', 30, 2, 'Take one tablet by mouth every morning', TRUE),
(20, 22, '2024-12-01', 90, 1, 'Inhale one puff twice daily', TRUE),
(21, 25, '2025-01-10', 30, 0, 'Take one tablet by mouth daily', TRUE),
(22, 25, '2025-02-05', 60, 2, 'Take one capsule by mouth daily with food', TRUE),
(23, 28, '2025-03-01', 30, 1, 'Take one tablet by mouth twice daily', TRUE),
(24, 28, '2025-04-15', 90, 0, 'Take one tablet by mouth daily', TRUE),
(25, 31, '2025-05-20', 30, 2, 'Take one tablet by mouth daily with water', TRUE),
(26, 31, '2025-06-10', 60, 1, 'Inhale two puffs daily', TRUE),
(27, 34, '2025-07-05', 30, 3, 'Take one tablet by mouth daily', TRUE),
(28, 34, '2025-08-01', 90, 0, 'Take one capsule by mouth twice daily', TRUE),
(29, 37, '2025-09-12', 30, 2, 'Take one tablet by mouth daily', TRUE),
(30, 37, '2025-10-03', 60, 1, 'Take one tablet by mouth at bedtime', TRUE),
(31, 40, '2025-11-15', 30, 2, 'Take one tablet by mouth every morning', TRUE),
(32, 40, '2025-12-01', 90, 1, 'Inhale one puff daily', TRUE),
(33, 1, '2023-05-20', 30, 0, 'Take one tablet by mouth daily', FALSE),
(34, 4, '2023-06-15', 60, 2, 'Take one capsule by mouth daily with food', FALSE),
(35, 7, '2023-07-01', 30, 1, 'Take one tablet by mouth twice daily', FALSE),
(36, 10, '2023-08-10', 90, 0, 'Take one tablet by mouth daily', FALSE),
(37, 12, '2023-09-05', 30, 2, 'Take one tablet by mouth daily with water', FALSE),
(38, 13, '2023-10-20', 60, 1, 'Inhale two puffs every morning', FALSE),
(39, 15, '2023-11-01', 30, 3, 'Take one tablet by mouth daily', FALSE),
(40, 16, '2023-12-15', 90, 0, 'Take one capsule by mouth twice daily', FALSE);