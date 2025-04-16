-- Sample data for SYSTEM_USERS table
-- Create 30-40 rows as specified in requirements

USE meditrack;

-- Insert sample system users here
-- Example:
-- INSERT INTO SYSTEM_USERS (user_name, password, email, role, first_name, last_name) 
-- VALUES ('jwilson', 'hashed_password', 'jwilson@meditrack.com', 'physician', 'James', 'Wilson');

INSERT INTO SYSTEM_USERS (user_name, password, email, role, first_name, last_name) VALUES
('jwilson', 'hashed_password_123', 'jwilson@meditrack.com', 'physician', 'James', 'Wilson'),
('asanders', 'hashed_password_456', 'asanders@meditrack.com', 'nurse', 'Alice', 'Sanders'),
('bthompson', 'hashed_password_789', 'bthompson@meditrack.com', 'admin', 'Brian', 'Thompson'),
('cjenkins', 'hashed_password_101', 'cjenkins@meditrack.com', 'physician', 'Clara', 'Jenkins'),
('dmartinez', 'hashed_password_112', 'dmartinez@meditrack.com', 'nurse', 'David', 'Martinez'),
('eroberts', 'hashed_password_134', 'eroberts@meditrack.com', 'pharmacist', 'Emma', 'Roberts'),
('fgarcia', 'hashed_password_156', 'fgarcia@meditrack.com', 'physician', 'Frank', 'Garcia'),
('glopez', 'hashed_password_178', 'glopez@meditrack.com', 'nurse', 'Grace', 'Lopez'),
('hwalker', 'hashed_password_190', 'hwalker@meditrack.com', 'admin', 'Henry', 'Walker'),
('iadams', 'hashed_password_202', 'iadams@meditrack.com', 'physician', 'Isabella', 'Adams'),
('jbrooks', 'hashed_password_214', 'jbrooks@meditrack.com', 'nurse', 'Jack', 'Brooks'),
('kclark', 'hashed_password_226', 'kclark@meditrack.com', 'pharmacist', 'Katherine', 'Clark'),
('lhill', 'hashed_password_238', 'lhill@meditrack.com', 'physician', 'Liam', 'Hill'),
('mmorgan', 'hashed_password_250', 'mmorgan@meditrack.com', 'nurse', 'Mia', 'Morgan'),
('nking', 'hashed_password_262', 'nking@meditrack.com', 'admin', 'Noah', 'King'),
('oparker', 'hashed_password_274', 'oparker@meditrack.com', 'physician', 'Olivia', 'Parker'),
('qreed', 'hashed_password_286', 'qreed@meditrack.com', 'nurse', 'Quinn', 'Reed'),
('rturner', 'hashed_password_298', 'rturner@meditrack.com', 'pharmacist', 'Rachel', 'Turner'),
('scarter', 'hashed_password_310', 'scarter@meditrack.com', 'physician', 'Samuel', 'Carter'),
('tbailey', 'hashed_password_322', 'tbailey@meditrack.com', 'nurse', 'Taylor', 'Bailey'),
('uward', 'hashed_password_334', 'uward@meditrack.com', 'admin', 'Uma', 'Ward'),
('vfox', 'hashed_password_346', 'vfox@meditrack.com', 'physician', 'Victor', 'Fox'),
('wgray', 'hashed_password_358', 'wgray@meditrack.com', 'nurse', 'Wendy', 'Gray'),
('xstone', 'hashed_password_370', 'xstone@meditrack.com', 'pharmacist', 'Xavier', 'Stone'),
('ybell', 'hashed_password_382', 'ybell@meditrack.com', 'physician', 'Yvonne', 'Bell'),
('zcole', 'hashed_password_394', 'zcole@meditrack.com', 'nurse', 'Zachary', 'Cole'),
('arussell', 'hashed_password_406', 'arussell@meditrack.com', 'admin', 'Amelia', 'Russell'),
('bharris', 'hashed_password_418', 'bharris@meditrack.com', 'physician', 'Benjamin', 'Harris'),
('cprice', 'hashed_password_430', 'cprice@meditrack.com', 'nurse', 'Charlotte', 'Price'),
('dsimmons', 'hashed_password_442', 'dsimmons@meditrack.com', 'pharmacist', 'Daniel', 'Simmons'),
('emitchell', 'hashed_password_454', 'emitchell@meditrack.com', 'physician', 'Ella', 'Mitchell'),
('fperry', 'hashed_password_466', 'fperry@meditrack.com', 'nurse', 'Felix', 'Perry'),
('gwood', 'hashed_password_478', 'gwood@meditrack.com', 'admin', 'Gabriella', 'Wood'),
('hhayes', 'hashed_password_490', 'hhayes@meditrack.com', 'physician', 'Harper', 'Hayes'),
('iross', 'hashed_password_502', 'iross@meditrack.com', 'nurse', 'Isaac', 'Ross'),
('jcox', 'hashed_password_514', 'jcox@meditrack.com', 'pharmacist', 'Jasmine', 'Cox'),
('kellis', 'hashed_password_526', 'kellis@meditrack.com', 'physician', 'Kevin', 'Ellis'),
('lfisher', 'hashed_password_538', 'lfisher@meditrack.com', 'nurse', 'Lily', 'Fisher'),
('mgordon', 'hashed_password_550', 'mgordon@meditrack.com', 'admin', 'Mason', 'Gordon'),
('nwebb', 'hashed_password_562', 'nwebb@meditrack.com', 'physician', 'Natalie', 'Webb');