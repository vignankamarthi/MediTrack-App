-- Sample data for patient_provider_record bridge table
-- Create 125+ rows as specified in requirements

USE meditrack;

-- Insert sample patient-provider relationships here
-- Example:
-- INSERT INTO patient_provider_record (patient_id, provider_id, relationship_type, is_primary)
-- VALUES (101, 1, 'PRIMARY_CARE', TRUE);

INSERT INTO patient_provider_record (patient_id, provider_id, relationship_type, is_primary) VALUES
(101, 2, 'PRIMARY_CARE', TRUE),
(101, 1, 'SPECIALTY_CARE', FALSE),
(101, 5, 'PHARMACIST', FALSE),
(102, 11, 'PRIMARY_CARE', TRUE),
(102, 19, 'SPECIALTY_CARE', FALSE),
(102, 12, 'PHARMACIST', FALSE),
(103, 17, 'PRIMARY_CARE', TRUE),
(103, 22, 'SPECIALTY_CARE', FALSE),
(103, 15, 'ADMINISTRATIVE', FALSE),
(104, 23, 'PRIMARY_CARE', TRUE),
(104, 16, 'SPECIALTY_CARE', FALSE),
(104, 18, 'PHARMACIST', FALSE),
(105, 29, 'PRIMARY_CARE', TRUE),
(105, 7, 'SPECIALTY_CARE', FALSE),
(105, 24, 'PHARMACIST', FALSE),
(106, 35, 'PRIMARY_CARE', TRUE),
(106, 10, 'SPECIALTY_CARE', FALSE),
(106, 30, 'PHARMACIST', FALSE),
(107, 2, 'PRIMARY_CARE', TRUE),
(107, 13, 'SPECIALTY_CARE', FALSE),
(107, 36, 'PHARMACIST', FALSE),
(108, 11, 'PRIMARY_CARE', TRUE),
(108, 6, 'SPECIALTY_CARE', FALSE),
(108, 5, 'PHARMACIST', FALSE),
(109, 17, 'PRIMARY_CARE', TRUE),
(109, 4, 'SPECIALTY_CARE', FALSE),
(109, 12, 'PHARMACIST', FALSE),
(110, 23, 'PRIMARY_CARE', TRUE),
(110, 19, 'SPECIALTY_CARE', FALSE),
(110, 18, 'PHARMACIST', FALSE),
(111, 29, 'PRIMARY_CARE', TRUE),
(111, 1, 'SPECIALTY_CARE', FALSE),
(111, 24, 'PHARMACIST', FALSE),
(112, 35, 'PRIMARY_CARE', TRUE),
(112, 22, 'SPECIALTY_CARE', FALSE),
(112, 30, 'PHARMACIST', FALSE),
(113, 2, 'PRIMARY_CARE', TRUE),
(113, 16, 'SPECIALTY_CARE', FALSE),
(113, 36, 'PHARMACIST', FALSE),
(114, 11, 'PRIMARY_CARE', TRUE),
(114, 10, 'SPECIALTY_CARE', FALSE),
(114, 5, 'PHARMACIST', FALSE),
(115, 17, 'PRIMARY_CARE', TRUE),
(115, 7, 'SPECIALTY_CARE', FALSE),
(115, 12, 'PHARMACIST', FALSE),
(116, 23, 'PRIMARY_CARE', TRUE),
(116, 13, 'SPECIALTY_CARE', FALSE),
(116, 18, 'PHARMACIST', FALSE),
(117, 29, 'PRIMARY_CARE', TRUE),
(117, 4, 'SPECIALTY_CARE', FALSE),
(117, 24, 'PHARMACIST', FALSE),
(118, 35, 'PRIMARY_CARE', TRUE),
(118, 6, 'SPECIALTY_CARE', FALSE),
(118, 30, 'PHARMACIST', FALSE),
(119, 2, 'PRIMARY_CARE', TRUE),
(119, 19, 'SPECIALTY_CARE', FALSE),
(119, 36, 'PHARMACIST', FALSE),
(120, 11, 'PRIMARY_CARE', TRUE),
(120, 1, 'SPECIALTY_CARE', FALSE),
(120, 5, 'PHARMACIST', FALSE),
(121, 17, 'PRIMARY_CARE', TRUE),
(121, 22, 'SPECIALTY_CARE', FALSE),
(121, 12, 'PHARMACIST', FALSE),
(122, 23, 'PRIMARY_CARE', TRUE),
(122, 16, 'SPECIALTY_CARE', FALSE),
(122, 18, 'PHARMACIST', FALSE),
(123, 29, 'PRIMARY_CARE', TRUE),
(123, 7, 'SPECIALTY_CARE', FALSE),
(123, 24, 'PHARMACIST', FALSE),
(124, 35, 'PRIMARY_CARE', TRUE),
(124, 10, 'SPECIALTY_CARE', FALSE),
(124, 30, 'PHARMACIST', FALSE),
(125, 2, 'PRIMARY_CARE', TRUE),
(125, 13, 'SPECIALTY_CARE', FALSE),
(125, 36, 'PHARMACIST', FALSE),
(126, 11, 'PRIMARY_CARE', TRUE),
(126, 4, 'SPECIALTY_CARE', FALSE),
(126, 5, 'PHARMACIST', FALSE),
(127, 17, 'PRIMARY_CARE', TRUE),
(127, 19, 'SPECIALTY_CARE', FALSE),
(127, 12, 'PHARMACIST', FALSE),
(128, 23, 'PRIMARY_CARE', TRUE),
(128, 1, 'SPECIALTY_CARE', FALSE),
(128, 18, 'PHARMACIST', FALSE),
(129, 29, 'PRIMARY_CARE', TRUE),
(129, 6, 'SPECIALTY_CARE', FALSE),
(129, 24, 'PHARMACIST', FALSE),
(130, 35, 'PRIMARY_CARE', TRUE),
(130, 22, 'SPECIALTY_CARE', FALSE),
(130, 30, 'PHARMACIST', FALSE),
(131, 2, 'PRIMARY_CARE', TRUE),
(131, 16, 'SPECIALTY_CARE', FALSE),
(131, 36, 'PHARMACIST', FALSE),
(132, 11, 'PRIMARY_CARE', TRUE),
(132, 7, 'SPECIALTY_CARE', FALSE),
(132, 5, 'PHARMACIST', FALSE),
(133, 17, 'PRIMARY_CARE', TRUE),
(133, 10, 'SPECIALTY_CARE', FALSE),
(133, 12, 'PHARMACIST', FALSE),
(134, 23, 'PRIMARY_CARE', TRUE),
(134, 13, 'SPECIALTY_CARE', FALSE),
(134, 18, 'PHARMACIST', FALSE),
(135, 29, 'PRIMARY_CARE', TRUE),
(135, 4, 'SPECIALTY_CARE', FALSE),
(135, 24, 'PHARMACIST', FALSE),
(136, 35, 'PRIMARY_CARE', TRUE),
(136, 19, 'SPECIALTY_CARE', FALSE),
(136, 30, 'PHARMACIST', FALSE),
(137, 2, 'PRIMARY_CARE', TRUE),
(137, 1, 'SPECIALTY_CARE', FALSE),
(137, 36, 'PHARMACIST', FALSE),
(138, 11, 'PRIMARY_CARE', TRUE),
(138, 6, 'SPECIALTY_CARE', FALSE),
(138, 5, 'PHARMACIST', FALSE),
(139, 17, 'PRIMARY_CARE', TRUE),
(139, 22, 'SPECIALTY_CARE', FALSE),
(139, 12, 'PHARMACIST', FALSE),
(140, 23, 'PRIMARY_CARE', TRUE),
(140, 16, 'SPECIALTY_CARE', FALSE),
(140, 18, 'PHARMACIST', FALSE),
(101, 3, 'ADMINISTRATIVE', FALSE),
(102, 9, 'ADMINISTRATIVE', FALSE),
(103, 15, 'ADMINISTRATIVE', FALSE),
(104, 21, 'ADMINISTRATIVE', FALSE),
(105, 27, 'ADMINISTRATIVE', FALSE),
(106, 33, 'ADMINISTRATIVE', FALSE),
(107, 39, 'ADMINISTRATIVE', FALSE),
(108, 3, 'ADMINISTRATIVE', FALSE),
(109, 9, 'ADMINISTRATIVE', FALSE),
(110, 15, 'ADMINISTRATIVE', FALSE),
(111, 21, 'ADMINISTRATIVE', FALSE),
(112, 27, 'ADMINISTRATIVE', FALSE),
(113, 33, 'ADMINISTRATIVE', FALSE),
(114, 39, 'ADMINISTRATIVE', FALSE),
(115, 3, 'ADMINISTRATIVE', FALSE),
(116, 9, 'ADMINISTRATIVE', FALSE),
(117, 15, 'ADMINISTRATIVE', FALSE),
(118, 21, 'ADMINISTRATIVE', FALSE),
(119, 27, 'ADMINISTRATIVE', FALSE),
(120, 33, 'ADMINISTRATIVE', FALSE),
(121, 39, 'ADMINISTRATIVE', FALSE),
(122, 3, 'ADMINISTRATIVE', FALSE),
(123, 9, 'ADMINISTRATIVE', FALSE),
(124, 15, 'ADMINISTRATIVE', FALSE),
(125, 21, 'ADMINISTRATIVE', FALSE);