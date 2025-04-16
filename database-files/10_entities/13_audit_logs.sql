-- Sample data for AUDIT_LOGS table
-- Create 30-40 rows as specified in requirements

USE meditrack;

-- Insert sample audit logs here
-- Example:
-- INSERT INTO AUDIT_LOGS (user_id, action_type, table_affected, record_id, details, ip_address)
-- VALUES (1, 'VIEW', 'PATIENT', 101, 'Viewed patient record', '192.168.1.1');

INSERT INTO AUDIT_LOGS (user_id, action_type, table_affected, record_id, details, ip_address) VALUES
(1, 'VIEW', 'PATIENT', 101, 'Viewed patient record', '192.168.1.1'),
(1, 'UPDATE', 'PATIENT', 101, 'Updated patient medical history', '192.168.1.1'),
(2, 'VIEW', 'PATIENT', 102, 'Viewed patient record', '192.168.1.2'),
(2, 'INSERT', 'MEDICATION', 201, 'Administered medication', '192.168.1.2'),
(3, 'VIEW', 'REPORT', 301, 'Viewed system report', '192.168.1.3'),
(3, 'UPDATE', 'SYSTEM_USERS', 3, 'Updated user role', '192.168.1.3'),
(4, 'VIEW', 'PATIENT', 103, 'Viewed patient record', '192.168.1.4'),
(4, 'INSERT', 'PRESCRIPTION', 401, 'Prescribed medication', '192.168.1.4'),
(5, 'VIEW', 'INVENTORY', 501, 'Viewed medication inventory', '192.168.1.5'),
(5, 'UPDATE', 'INVENTORY', 501, 'Dispensed medication', '192.168.1.5'),
(6, 'VIEW', 'PATIENT', 104, 'Viewed patient record', '192.168.1.6'),
(6, 'INSERT', 'MEDICATION', 202, 'Administered medication', '192.168.1.6'),
(7, 'VIEW', 'PATIENT', 105, 'Viewed patient record', '192.168.1.7'),
(7, 'UPDATE', 'PATIENT', 105, 'Updated patient diagnosis', '192.168.1.7'),
(8, 'VIEW', 'REPORT', 302, 'Viewed system report', '192.168.1.8'),
(8, 'INSERT', 'SYSTEM_USERS', 40, 'Added new user', '192.168.1.8'),
(9, 'VIEW', 'PATIENT', 106, 'Viewed patient record', '192.168.1.9'),
(9, 'INSERT', 'PRESCRIPTION', 402, 'Prescribed medication', '192.168.1.9'),
(10, 'VIEW', 'PATIENT', 107, 'Viewed patient record', '192.168.1.10'),
(10, 'INSERT', 'MEDICATION', 203, 'Administered medication', '192.168.1.10'),
(11, 'VIEW', 'INVENTORY', 502, 'Viewed medication inventory', '192.168.1.11'),
(11, 'UPDATE', 'INVENTORY', 502, 'Dispensed medication', '192.168.1.11'),
(12, 'VIEW', 'PATIENT', 108, 'Viewed patient record', '192.168.1.12'),
(12, 'UPDATE', 'PATIENT', 108, 'Updated patient treatment plan', '192.168.1.12'),
(13, 'VIEW', 'PATIENT', 109, 'Viewed patient record', '192.168.1.13'),
(13, 'INSERT', 'MEDICATION', 204, 'Administered medication', '192.168.1.13'),
(14, 'VIEW', 'REPORT', 303, 'Viewed system report', '192.168.1.14'),
(14, 'UPDATE', 'SYSTEM_USERS', 14, 'Updated user permissions', '192.168.1.14'),
(15, 'VIEW', 'PATIENT', 110, 'Viewed patient record', '192.168.1.15'),
(15, 'INSERT', 'PRESCRIPTION', 403, 'Prescribed medication', '192.168.1.15'),
(16, 'VIEW', 'INVENTORY', 503, 'Viewed medication inventory', '192.168.1.16'),
(16, 'UPDATE', 'INVENTORY', 503, 'Dispensed medication', '192.168.1.16'),
(17, 'VIEW', 'PATIENT', 111, 'Viewed patient record', '192.168.1.17'),
(17, 'UPDATE', 'PATIENT', 111, 'Updated patient contact info', '192.168.1.17'),
(18, 'VIEW', 'PATIENT', 112, 'Viewed patient record', '192.168.1.18'),
(18, 'INSERT', 'PRESCRIPTION', 404, 'Prescribed medication', '192.168.1.18'),
(19, 'VIEW', 'PATIENT', 113, 'Viewed patient record', '192.168.1.19'),
(20, 'VIEW', 'INVENTORY', 504, 'Viewed medication inventory', '192.168.1.20'),
(20, 'UPDATE', 'INVENTORY', 504, 'Dispensed medication', '192.168.1.20'),
(21, 'VIEW', 'REPORT', 304, 'Viewed system report', '192.168.1.21');