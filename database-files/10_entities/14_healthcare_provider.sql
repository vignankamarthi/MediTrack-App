-- Sample data for HEALTHCARE_PROVIDER table
-- Create 30-40 rows as specified in requirements

USE meditrack;

-- Insert sample healthcare providers here
-- Example:
-- INSERT INTO HEALTHCARE_PROVIDER (provider_id, first_name, last_name, specialization, license_number, contact_number, email, department)
-- VALUES (1, 'James', 'Wilson', 'Cardiology', 'MD12345', '555-123-4567', 'jwilson@meditrack.com', 'Cardiology');

INSERT INTO HEALTHCARE_PROVIDER (provider_id, first_name, last_name, specialization, license_number, contact_number, email, department) VALUES
(1, 'James', 'Wilson', 'Cardiology', 'MD12345', '555-123-4567', 'jwilson@meditrack.com', 'Cardiology'),
(2, 'Alice', 'Sanders', 'General Practice', 'NP67890', '555-234-5678', 'asanders@meditrack.com', 'Primary Care'),
(3, 'Brian', 'Thompson', 'Administration', 'AD34567', '555-345-6789', 'bthompson@meditrack.com', 'Administration'),
(4, 'Clara', 'Jenkins', 'Neurology', 'MD45678', '555-456-7890', 'cjenkins@meditrack.com', 'Neurology'),
(5, 'David', 'Martinez', 'Pharmacology', 'PH78901', '555-567-8901', 'dmartinez@meditrack.com', 'Pharmacy'),
(6, 'Emma', 'Roberts', 'Pediatrics', 'MD23456', '555-678-9012', 'eroberts@meditrack.com', 'Pediatrics'),
(7, 'Frank', 'Garcia', 'Oncology', 'MD56789', '555-789-0123', 'fgarcia@meditrack.com', 'Oncology'),
(8, 'Grace', 'Lopez', 'Emergency Medicine', 'NP01234', '555-890-1234', 'glopez@meditrack.com', 'Emergency'),
(9, 'Henry', 'Walker', 'Administration', 'AD67890', '555-901-2345', 'hwalker@meditrack.com', 'Administration'),
(10, 'Isabella', 'Adams', 'Orthopedics', 'MD89012', '555-012-3456', 'iadams@meditrack.com', 'Orthopedics'),
(11, 'Jack', 'Brooks', 'General Practice', 'NP34567', '555-123-4568', 'jbrooks@meditrack.com', 'Primary Care'),
(12, 'Katherine', 'Clark', 'Pharmacology', 'PH90123', '555-234-5679', 'kclark@meditrack.com', 'Pharmacy'),
(13, 'Liam', 'Hill', 'Gastroenterology', 'MD12378', '555-345-6780', 'lhill@meditrack.com', 'Gastroenterology'),
(14, 'Mia', 'Morgan', 'Emergency Medicine', 'NP45678', '555-456-7891', 'mmorgan@meditrack.com', 'Emergency'),
(15, 'Noah', 'King', 'Administration', 'AD78901', '555-567-8902', 'nking@meditrack.com', 'Administration'),
(16, 'Olivia', 'Parker', 'Dermatology', 'MD23467', '555-678-9013', 'oparker@meditrack.com', 'Dermatology'),
(17, 'Quinn', 'Reed', 'General Practice', 'NP56789', '555-789-0124', 'qreed@meditrack.com', 'Primary Care'),
(18, 'Rachel', 'Turner', 'Pharmacology', 'PH89012', '555-890-1235', 'rturner@meditrack.com', 'Pharmacy'),
(19, 'Samuel', 'Carter', 'Endocrinology', 'MD34589', '555-901-2346', 'scarter@meditrack.com', 'Endocrinology'),
(20, 'Taylor', 'Bailey', 'Pediatrics', 'NP01245', '555-012-3457', 'tbailey@meditrack.com', 'Pediatrics'),
(21, 'Uma', 'Ward', 'Administration', 'AD23456', '555-123-4569', 'uward@meditrack.com', 'Administration'),
(22, 'Victor', 'Fox', 'Cardiology', 'MD56790', '555-234-5670', 'vfox@meditrack.com', 'Cardiology'),
(23, 'Wendy', 'Gray', 'General Practice', 'NP67812', '555-345-6781', 'wgray@meditrack.com', 'Primary Care'),
(24, 'Xavier', 'Stone', 'Pharmacology', 'PH90145', '555-456-7892', 'xstone@meditrack.com', 'Pharmacy'),
(25, 'Yvonne', 'Bell', 'Neurology', 'MD12390', '555-567-8903', 'ybell@meditrack.com', 'Neurology'),
(26, 'Zachary', 'Cole', 'Emergency Medicine', 'NP23478', '555-678-9014', 'zcole@meditrack.com', 'Emergency'),
(27, 'Amelia', 'Russell', 'Administration', 'AD34589', '555-789-0125', 'arussell@meditrack.com', 'Administration'),
(28, 'Benjamin', 'Harris', 'Oncology', 'MD45690', '555-890-1236', 'bharris@meditrack.com', 'Oncology'),
(29, 'Charlotte', 'Price', 'General Practice', 'NP56701', '555-901-2347', 'cprice@meditrack.com', 'Primary Care'),
(30, 'Daniel', 'Simmons', 'Pharmacology', 'PH67812', '555-012-3458', 'dsimmons@meditrack.com', 'Pharmacy'),
(31, 'Ella', 'Mitchell', 'Cardiology', 'MD78923', '555-123-4570', 'emitchell@meditrack.com', 'Cardiology'),
(32, 'Felix', 'Perry', 'Pediatrics', 'NP89034', '555-234-5671', 'fperry@meditrack.com', 'Pediatrics'),
(33, 'Gabriella', 'Wood', 'Administration', 'AD90145', '555-345-6782', 'gwood@meditrack.com', 'Administration'),
(34, 'Harper', 'Hayes', 'Dermatology', 'MD01256', '555-456-7893', 'hhayes@meditrack.com', 'Dermatology'),
(35, 'Isaac', 'Ross', 'General Practice', 'NP12367', '555-567-8904', 'iross@meditrack.com', 'Primary Care'),
(36, 'Jasmine', 'Cox', 'Pharmacology', 'PH23478', '555-678-9015', 'jcox@meditrack.com', 'Pharmacy'),
(37, 'Kevin', 'Ellis', 'Orthopedics', 'MD34590', '555-789-0126', 'kellis@meditrack.com', 'Orthopedics'),
(38, 'Lily', 'Fisher', 'Emergency Medicine', 'NP45601', '555-890-1237', 'lfisher@meditrack.com', 'Emergency'),
(39, 'Mason', 'Gordon', 'Administration', 'AD56712', '555-901-2348', 'mgordon@meditrack.com', 'Administration'),
(40, 'Natalie', 'Webb', 'Neurology', 'MD67823', '555-012-3459', 'nwebb@meditrack.com', 'Neurology');