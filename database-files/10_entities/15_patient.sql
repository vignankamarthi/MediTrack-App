-- Sample data for PATIENT table
-- Create 30-40 rows as specified in requirements

USE meditrack;

-- Insert sample patients here
-- Example:
-- INSERT INTO PATIENT (patient_id, first_name, last_name, DOB, gender, contact_number, email, address, insurance_provider, insurance_id, emergency_contact_name, emergency_contact_number, managing_user_id)
-- VALUES (101, 'John', 'Doe', '1980-05-15', 'Male', '555-987-6543', 'john.doe@email.com', '123 Main St, Anytown, USA', 'HealthPlus', 'HP98765', 'Jane Doe', '555-789-0123', 1);

INSERT INTO PATIENT (patient_id, first_name, last_name, DOB, gender, contact_number, email, address, insurance_provider, insurance_id, emergency_contact_name, emergency_contact_number, managing_user_id) VALUES
(101, 'John', 'Doe', '1980-05-15', 'Male', '555-987-6543', 'john.doe@email.com', '123 Main St, Anytown, USA', 'HealthPlus', 'HP98765', 'Jane Doe', '555-789-0123', 1),
(102, 'Sarah', 'Smith', '1992-08-22', 'Female', '555-876-5432', 'sarah.smith@email.com', '456 Oak Ave, Anytown, USA', 'MediCare', 'MC12345', 'Tom Smith', '555-678-9012', 2),
(103, 'Michael', 'Brown', '1975-03-10', 'Male', '555-765-4321', 'michael.brown@email.com', '789 Pine Rd, Anytown, USA', 'BlueShield', 'BS67890', 'Lisa Brown', '555-567-8901', 4),
(104, 'Emily', 'Davis', '1988-11-30', 'Female', '555-654-3210', 'emily.davis@email.com', '101 Elm St, Anytown, USA', 'HealthPlus', 'HP54321', 'Mark Davis', '555-456-7890', 6),
(105, 'William', 'Johnson', '1965-07-19', 'Male', '555-543-2109', 'william.johnson@email.com', '202 Cedar Ln, Anytown, USA', 'MediCare', 'MC98765', 'Susan Johnson', '555-345-6789', 7),
(106, 'Olivia', 'Taylor', '1995-01-25', 'Female', '555-432-1098', 'olivia.taylor@email.com', '303 Birch Dr, Anytown, USA', 'BlueShield', 'BS23456', 'James Taylor', '555-234-5678', 9),
(107, 'Ethan', 'Wilson', '1983-09-12', 'Male', '555-321-0987', 'ethan.wilson@email.com', '404 Maple Ct, Anytown, USA', 'HealthPlus', 'HP67890', 'Amy Wilson', '555-123-4567', 10),
(108, 'Ava', 'Martinez', '1978-04-07', 'Female', '555-210-9876', 'ava.martinez@email.com', '505 Spruce Way, Anytown, USA', 'MediCare', 'MC34567', 'Carlos Martinez', '555-012-3456', 12),
(109, 'Liam', 'Anderson', '1990-06-18', 'Male', '555-109-8765', 'liam.anderson@email.com', '606 Walnut St, Anytown, USA', 'BlueShield', 'BS78901', 'Emma Anderson', '555-901-2345', 13),
(110, 'Sophia', 'Thomas', '1987-12-03', 'Female', '555-098-7654', 'sophia.thomas@email.com', '707 Chestnut Blvd, Anytown, USA', 'HealthPlus', 'HP01234', 'David Thomas', '555-890-1234', 15),
(111, 'Noah', 'Jackson', '1970-02-14', 'Male', '555-987-6542', 'noah.jackson@email.com', '808 Sycamore Ave, Anytown, USA', 'MediCare', 'MC45678', 'Rachel Jackson', '555-789-0124', 16),
(112, 'Isabella', 'White', '1993-10-09', 'Female', '555-876-5431', 'isabella.white@email.com', '909 Magnolia Dr, Anytown, USA', 'BlueShield', 'BS89012', 'Paul White', '555-678-9013', 17),
(113, 'Mason', 'Harris', '1982-05-27', 'Male', '555-765-4320', 'mason.harris@email.com', '1010 Laurel Rd, Anytown, USA', 'HealthPlus', 'HP23456', 'Laura Harris', '555-567-8902', 19),
(114, 'Mia', 'Lewis', '1997-07-04', 'Female', '555-654-3219', 'mia.lewis@email.com', '1111 Poplar St, Anytown, USA', 'MediCare', 'MC56789', 'Steven Lewis', '555-456-7891', 20),
(115, 'James', 'Walker', '1973-03-22', 'Male', '555-543-2108', 'james.walker@email.com', '1212 Willow Ln, Anytown, USA', 'BlueShield', 'BS01234', 'Karen Walker', '555-345-6780', 22),
(116, 'Charlotte', 'Hall', '1989-08-16', 'Female', '555-432-1097', 'charlotte.hall@email.com', '1313 Cedar Ct, Anytown, USA', 'HealthPlus', 'HP34567', 'Robert Hall', '555-234-5679', 23),
(117, 'Benjamin', 'Allen', '1984-11-28', 'Male', '555-321-0986', 'benjamin.allen@email.com', '1414 Pine Way, Anytown, USA', 'MediCare', 'MC67890', 'Megan Allen', '555-123-4568', 25),
(118, 'Amelia', 'Young', '1991-01-13', 'Female', '555-210-9875', 'amelia.young@email.com', '1515 Oak Blvd, Anytown, USA', 'BlueShield', 'BS12345', 'Daniel Young', '555-012-3457', 26),
(119, 'Lucas', 'King', '1977-06-05', 'Male', '555-109-8764', 'lucas.king@email.com', '1616 Elm Dr, Anytown, USA', 'HealthPlus', 'HP45678', 'Rebecca King', '555-901-2346', 28),
(120, 'Harper', 'Wright', '1994-09-20', 'Female', '555-098-7653', 'harper.wright@email.com', '1717 Maple St, Anytown, USA', 'MediCare', 'MC78901', 'Thomas Wright', '555-890-1235', 29),
(121, 'Henry', 'Scott', '1981-04-11', 'Male', '555-987-6541', 'henry.scott@email.com', '1818 Birch Rd, Anytown, USA', 'BlueShield', 'BS23456', 'Christine Scott', '555-789-0125', 31),
(122, 'Evelyn', 'Green', '1986-12-29', 'Female', '555-876-5430', 'evelyn.green@email.com', '1919 Spruce Ln, Anytown, USA', 'HealthPlus', 'HP56789', 'Joseph Green', '555-678-9014', 32),
(123, 'Alexander', 'Adams', '1979-02-08', 'Male', '555-765-4329', 'alexander.adams@email.com', '2020 Walnut Ct, Anytown, USA', 'MediCare', 'MC89012', 'Michelle Adams', '555-567-8903', 34),
(124, 'Abigail', 'Baker', '1996-05-17', 'Female', '555-654-3218', 'abigail.baker@email.com', '2121 Chestnut Way, Anytown, USA', 'BlueShield', 'BS34567', 'Richard Baker', '555-456-7892', 35),
(125, 'Daniel', 'Gonzalez', '1985-10-02', 'Male', '555-543-2107', 'daniel.gonzalez@email.com', '2222 Sycamore St, Anytown, USA', 'HealthPlus', 'HP67890', 'Sofia Gonzalez', '555-345-6781', 37),
(126, 'Sofia', 'Nelson', '1990-07-26', 'Female', '555-432-1096', 'sofia.nelson@email.com', '2323 Magnolia Blvd, Anytown, USA', 'MediCare', 'MC01234', 'Edward Nelson', '555-234-5670', 38),
(127, 'Matthew', 'Carter', '1976-03-14', 'Male', '555-321-0985', 'matthew.carter@email.com', '2424 Laurel Dr, Anytown, USA', 'BlueShield', 'BS45678', 'Jennifer Carter', '555-123-4569', 40),
(128, 'Aria', 'Mitchell', '1998-08-31', 'Female', '555-210-9874', 'aria.mitchell@email.com', '2525 Poplar Rd, Anytown, USA', 'HealthPlus', 'HP78901', 'George Mitchell', '555-012-3458', 1),
(129, 'Joseph', 'Perez', '1983-01-06', 'Male', '555-109-8763', 'joseph.perez@email.com', '2626 Willow Ct, Anytown, USA', 'MediCare', 'MC12345', 'Maria Perez', '555-901-2347', 2),
(130, 'Scarlett', 'Roberts', '1992-11-23', 'Female', '555-098-7652', 'scarlett.roberts@email.com', '2727 Cedar Way, Anytown, USA', 'BlueShield', 'BS56789', 'Andrew Roberts', '555-890-1236', 4),
(131, 'David', 'Turner', '1974-06-09', 'Male', '555-987-6540', 'david.turner@email.com', '2828 Pine St, Anytown, USA', 'HealthPlus', 'HP89012', 'Patricia Turner', '555-789-0126', 6),
(132, 'Chloe', 'Phillips', '1989-04-15', 'Female', '555-876-5429', 'chloe.phillips@email.com', '2929 Oak Ln, Anytown, USA', 'MediCare', 'MC23456', 'Brian Phillips', '555-678-9015', 7),
(133, 'Samuel', 'Campbell', '1980-09-28', 'Male', '555-765-4328', 'samuel.campbell@email.com', '3030 Elm Blvd, Anytown, USA', 'BlueShield', 'BS67890', 'Nancy Campbell', '555-567-8904', 9),
(134, 'Victoria', 'Parker', '1995-02-12', 'Female', '555-654-3217', 'victoria.parker@email.com', '3131 Maple Dr, Anytown, USA', 'HealthPlus', 'HP01234', 'Charles Parker', '555-456-7893', 10),
(135, 'Jackson', 'Evans', '1978-07-21', 'Male', '555-543-2106', 'jackson.evans@email.com', '3232 Birch Rd, Anytown, USA', 'MediCare', 'MC34567', 'Deborah Evans', '555-345-6782', 12),
(136, 'Luna', 'Edwards', '1993-12-04', 'Female', '555-432-1095', 'luna.edwards@email.com', '3333 Spruce St, Anytown, USA', 'BlueShield', 'BS78901', 'Frank Edwards', '555-234-5671', 13),
(137, 'Gabriel', 'Collins', '1987-05-30', 'Male', '555-321-0984', 'gabriel.collins@email.com', '3434 Walnut Ct, Anytown, USA', 'HealthPlus', 'HP12345', 'Katherine Collins', '555-123-4570', 15),
(138, 'Penelope', 'Stewart', '1991-10-19', 'Female', '555-210-9873', 'penelope.stewart@email.com', '3535 Chestnut Way, Anytown, USA', 'MediCare', 'MC45678', 'Philip Stewart', '555-012-3459', 16),
(139, 'Logan', 'Sanchez', '1975-03-07', 'Male', '555-109-8762', 'logan.sanchez@email.com', '3636 Sycamore Ln, Anytown, USA', 'BlueShield', 'BS89012', 'Teresa Sanchez', '555-901-2348', 17),
(140, 'Layla', 'Morris', '1990-06-25', 'Female', '555-098-7651', 'layla.morris@email.com', '3737 Magnolia St, Anytown, USA', 'HealthPlus', 'HP23456', 'Scott Morris', '555-890-1237', 19);