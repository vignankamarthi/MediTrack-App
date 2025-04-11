-- Main schema file for MediTrack application

-- Create database and set it as current database
DROP DATABASE IF EXISTS meditrack;
CREATE DATABASE meditrack;
USE meditrack;

-- Creating the BASE ENTITIES

-- 1. SYSTEM_USERS table
DROP TABLE IF EXISTS SYSTEM_USERS;
CREATE TABLE SYSTEM_USERS
(
    user_id    INT AUTO_INCREMENT PRIMARY KEY,
    user_name  VARCHAR(50)  NOT NULL UNIQUE,
    password   VARCHAR(255) NOT NULL,
    email      VARCHAR(100) NOT NULL UNIQUE,
    role       VARCHAR(50)  NOT NULL,
    is_active  BOOLEAN   DEFAULT TRUE,
    first_name VARCHAR(50)  NOT NULL,
    last_name  VARCHAR(50)  NOT NULL,
    last_login TIMESTAMP    NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 2. PERMISSIONS table
DROP TABLE IF EXISTS PERMISSIONS;
CREATE TABLE PERMISSIONS
(
    permission_id   INT AUTO_INCREMENT PRIMARY KEY,
    permission_name VARCHAR(100) NOT NULL,
    description     TEXT,
    user_id         INT,
    is_active       BOOLEAN   DEFAULT TRUE,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES SYSTEM_USERS (user_id)
);


-- 3. AUDIT_LOGS table
DROP TABLE IF EXISTS AUDIT_LOGS;
CREATE TABLE AUDIT_LOGS
(
    log_id           INT AUTO_INCREMENT PRIMARY KEY,
    user_id          INT,
    action_type      VARCHAR(50) NOT NULL,
    table_affected   VARCHAR(50) NOT NULL,
    record_id        INT         NOT NULL,
    details          TEXT,
    ip_address       VARCHAR(45) NOT NULL,
    action_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES SYSTEM_USERS (user_id)
);

-- 4. HEALTHCARE_PROVIDER table
DROP TABLE IF EXISTS HEALTHCARE_PROVIDER;
CREATE TABLE HEALTHCARE_PROVIDER
(
    provider_id    INT PRIMARY KEY,
    first_name     VARCHAR(50) NOT NULL,
    last_name      VARCHAR(50) NOT NULL,
    specialization VARCHAR(100),
    license_number VARCHAR(50) UNIQUE,
    contact_number VARCHAR(20),
    email          VARCHAR(100) UNIQUE,
    department     VARCHAR(100),
    is_active      BOOLEAN   DEFAULT TRUE,
    created_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 5. PATIENT table
DROP TABLE IF EXISTS PATIENT;
CREATE TABLE PATIENT
(
    patient_id               INT PRIMARY KEY,
    first_name               VARCHAR(50) NOT NULL,
    last_name                VARCHAR(50) NOT NULL,
    DOB                      DATE        NOT NULL,
    gender                   VARCHAR(20),
    contact_number           VARCHAR(20),
    email                    VARCHAR(100),
    address                  TEXT,
    insurance_provider       VARCHAR(100),
    insurance_id             VARCHAR(50),
    emergency_contact_name   VARCHAR(100),
    emergency_contact_number VARCHAR(20),
    managing_user_id         INT,
    created_at               TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at               TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (managing_user_id) REFERENCES SYSTEM_USERS (user_id)
);

-- 6. MEDICAL_CONDITION table
DROP TABLE IF EXISTS MEDICAL_CONDITION;
CREATE TABLE MEDICAL_CONDITION
(
    condition_id   INT PRIMARY KEY,
    condition_name VARCHAR(100) NOT NULL,
    description    TEXT,
    icd_code       VARCHAR(20),
    is_chronic     BOOLEAN   DEFAULT FALSE,
    created_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 7. TREATMENT table
DROP TABLE IF EXISTS TREATMENT;
CREATE TABLE TREATMENT
(
    treatment_id      INT PRIMARY KEY,
    treatment_name    VARCHAR(100) NOT NULL,
    description       TEXT,
    procedure_code    VARCHAR(20),
    standard_duration INT COMMENT 'Duration in minutes',
    is_deprecated     BOOLEAN   DEFAULT FALSE,
    created_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 8. TREATMENT_OUTCOMES table
DROP TABLE IF EXISTS TREATMENT_OUTCOMES;
CREATE TABLE TREATMENT_OUTCOMES
(
    outcome_id   INT AUTO_INCREMENT PRIMARY KEY,
    treatment_id INT,
    outcome_name VARCHAR(100) NOT NULL,
    description  TEXT,
    is_positive  BOOLEAN,
    created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (treatment_id) REFERENCES TREATMENT (treatment_id)
);

-- 9. CLINICAL_PROTOCOL table
DROP TABLE IF EXISTS CLINICAL_PROTOCOL;
CREATE TABLE CLINICAL_PROTOCOL
(
    protocol_id     INT PRIMARY KEY,
    protocol_name   VARCHAR(100) NOT NULL,
    description     TEXT,
    version         VARCHAR(20)  NOT NULL,
    effective_date  DATE         NOT NULL,
    expiration_date DATE,
    is_active       BOOLEAN   DEFAULT TRUE,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 10. MEDICATIONS table
DROP TABLE IF EXISTS MEDICATIONS;
CREATE TABLE MEDICATIONS
(
    medication_id    INT PRIMARY KEY,
    medication_name  VARCHAR(100) NOT NULL,
    generic_name     VARCHAR(100),
    medication_class VARCHAR(100),
    dosage_form      VARCHAR(50)  NOT NULL,
    strength         VARCHAR(50)  NOT NULL,
    manufacturer     VARCHAR(100),
    ndc_code         VARCHAR(20) UNIQUE,
    is_controlled    BOOLEAN   DEFAULT FALSE,
    control_class    VARCHAR(10),
    created_at       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at       TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 11. PRESCRIPTIONS table
DROP TABLE IF EXISTS PRESCRIPTIONS;
CREATE TABLE PRESCRIPTIONS
(
    prescription_id   INT PRIMARY KEY,
    prescriber_id     INT  NOT NULL,
    prescription_date DATE NOT NULL,
    duration          INT COMMENT 'Duration in days',
    refills           INT       DEFAULT 0,
    instructions      TEXT,
    is_active         BOOLEAN   DEFAULT TRUE,
    created_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 12. PATIENT_EDUCATION table
DROP TABLE IF EXISTS PATIENT_EDUCATION;
CREATE TABLE PATIENT_EDUCATION
(
    record_id           INT AUTO_INCREMENT PRIMARY KEY,
    provider_id         INT NOT NULL,
    comprehension_level VARCHAR(20),
    notes               TEXT,
    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 13. SYMPTOMS table
DROP TABLE IF EXISTS SYMPTOMS;
CREATE TABLE SYMPTOMS
(
    symptom_id    INT AUTO_INCREMENT PRIMARY KEY,
    symptom_name  VARCHAR(100) NOT NULL,
    description   TEXT,
    severity_code VARCHAR(20),
    created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 14. CARE_TASKS table
DROP TABLE IF EXISTS CARE_TASKS;
CREATE TABLE CARE_TASKS
(
    task_id            INT AUTO_INCREMENT PRIMARY KEY,
    task_name          VARCHAR(100) NOT NULL,
    description        TEXT,
    priority           VARCHAR(20)  NOT NULL,
    estimated_duration INT COMMENT 'Duration in minutes',
    created_at         TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at         TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 15. CARE_PATHWAY table
DROP TABLE IF EXISTS CARE_PATHWAY;
CREATE TABLE CARE_PATHWAY
(
    pathway_id        INT AUTO_INCREMENT PRIMARY KEY,
    pathway_name      VARCHAR(100) NOT NULL,
    description       TEXT,
    standard_duration INT COMMENT 'Duration in days',
    is_active         BOOLEAN   DEFAULT TRUE,
    created_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 16. SOCIAL_DETERMINANTS table
DROP TABLE IF EXISTS SOCIAL_DETERMINANTS;
CREATE TABLE SOCIAL_DETERMINANTS
(
    determinant_id   INT AUTO_INCREMENT PRIMARY KEY,
    determinant_name VARCHAR(100) NOT NULL,
    category         VARCHAR(50),
    description      TEXT,
    created_at       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at       TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 17. LAB_RESULTS table
DROP TABLE IF EXISTS LAB_RESULTS;
CREATE TABLE LAB_RESULTS
(
    result_id       INT AUTO_INCREMENT PRIMARY KEY,
    patient_id      INT          NOT NULL,
    test_name       VARCHAR(100) NOT NULL,
    test_date       DATE         NOT NULL,
    result_date     DATE         NOT NULL,
    result_value    VARCHAR(100) NOT NULL,
    reference_range VARCHAR(100),
    unit_of_measure VARCHAR(50),
    is_abnormal     BOOLEAN,
    lab_notes       TEXT,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


-- Creating the BRIDGE TABLES

-- Bridge Tables for PATIENT relationships
-- 1. PATIENT to MEDICAL_CONDITION
DROP TABLE IF EXISTS patient_condition_record;
CREATE TABLE patient_condition_record
(
    patient_id     INT NOT NULL,
    condition_id   INT NOT NULL,
    diagnosis_date DATE,
    is_active      BOOLEAN DEFAULT TRUE,
    PRIMARY KEY (patient_id, condition_id),
    FOREIGN KEY (patient_id) REFERENCES PATIENT (patient_id),
    FOREIGN KEY (condition_id) REFERENCES MEDICAL_CONDITION (condition_id)
);

-- 2. PATIENT to TREATMENT
DROP TABLE IF EXISTS patient_treatment_record;
CREATE TABLE patient_treatment_record
(
    patient_id   INT NOT NULL,
    treatment_id INT NOT NULL,
    start_date   DATE,
    end_date     DATE,
    status       VARCHAR(50),
    PRIMARY KEY (patient_id, treatment_id),
    FOREIGN KEY (patient_id) REFERENCES PATIENT (patient_id),
    FOREIGN KEY (treatment_id) REFERENCES TREATMENT (treatment_id)
);

-- 3. PATIENT to HEALTHCARE_PROVIDER
DROP TABLE IF EXISTS patient_provider_record;
CREATE TABLE patient_provider_record
(
    patient_id        INT NOT NULL,
    provider_id       INT NOT NULL,
    relationship_type VARCHAR(50),
    is_primary        BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (patient_id, provider_id),
    FOREIGN KEY (patient_id) REFERENCES PATIENT (patient_id),
    FOREIGN KEY (provider_id) REFERENCES HEALTHCARE_PROVIDER (provider_id)
);

-- 4. PATIENT to PATIENT_EDUCATION
DROP TABLE IF EXISTS patient_education_record;
CREATE TABLE patient_education_record
(
    patient_id     INT NOT NULL,
    education_id   INT NOT NULL,
    education_date DATE,
    PRIMARY KEY (patient_id, education_id),
    FOREIGN KEY (patient_id) REFERENCES PATIENT (patient_id),
    FOREIGN KEY (education_id) REFERENCES PATIENT_EDUCATION (record_id)
);

-- 5. PATIENT to SOCIAL_DETERMINANTS
DROP TABLE IF EXISTS patient_social_record;
CREATE TABLE patient_social_record
(
    patient_id     INT NOT NULL,
    determinant_id INT NOT NULL,
    impact_level   VARCHAR(10),
    PRIMARY KEY (patient_id, determinant_id),
    FOREIGN KEY (patient_id) REFERENCES PATIENT (patient_id),
    FOREIGN KEY (determinant_id) REFERENCES SOCIAL_DETERMINANTS (determinant_id)
);

-- 6. PATIENT to CARE_PATHWAY
DROP TABLE IF EXISTS patient_pathway_record;
CREATE TABLE patient_pathway_record
(
    patient_id INT NOT NULL,
    pathway_id INT NOT NULL,
    PRIMARY KEY (patient_id, pathway_id),
    FOREIGN KEY (patient_id) REFERENCES PATIENT (patient_id),
    FOREIGN KEY (pathway_id) REFERENCES CARE_PATHWAY (pathway_id)
);

-- 7. PATIENT to SYMPTOMS
DROP TABLE IF EXISTS patient_symptom_record;
CREATE TABLE patient_symptom_record
(
    patient_id INT NOT NULL,
    symptom_id INT NOT NULL,
    severity   VARCHAR(10),
    PRIMARY KEY (patient_id, symptom_id),
    FOREIGN KEY (patient_id) REFERENCES PATIENT (patient_id),
    FOREIGN KEY (symptom_id) REFERENCES SYMPTOMS (symptom_id)
);

-- 8. PATIENT to TREATMENT_OUTCOMES
DROP TABLE IF EXISTS patient_outcome_record;
CREATE TABLE patient_outcome_record
(
    patient_id INT NOT NULL,
    outcome_id INT NOT NULL,
    PRIMARY KEY (patient_id, outcome_id),
    FOREIGN KEY (patient_id) REFERENCES PATIENT (patient_id),
    FOREIGN KEY (outcome_id) REFERENCES TREATMENT_OUTCOMES (outcome_id)
);

-- 9. PATIENT to PRESCRIPTIONS
DROP TABLE IF EXISTS prescription_patient_record;
CREATE TABLE prescription_patient_record
(
    patient_id      INT NOT NULL,
    prescription_id INT NOT NULL,
    PRIMARY KEY (patient_id, prescription_id),
    FOREIGN KEY (patient_id) REFERENCES PATIENT (patient_id),
    FOREIGN KEY (prescription_id) REFERENCES PRESCRIPTIONS (prescription_id)
);

-- 10. PATIENT to AUDIT_LOGS
DROP TABLE IF EXISTS audit_patient_record;
CREATE TABLE audit_patient_record
(
    patient_id INT NOT NULL,
    log_id     INT NOT NULL,
    PRIMARY KEY (patient_id, log_id),
    FOREIGN KEY (patient_id) REFERENCES PATIENT (patient_id),
    FOREIGN KEY (log_id) REFERENCES AUDIT_LOGS (log_id)
);

-- 11. PATIENT to MEDICATIONS
DROP TABLE IF EXISTS medication_record;
CREATE TABLE medication_record
(
    patient_id    INT NOT NULL,
    medication_id INT NOT NULL,
    dosage        VARCHAR(50),
    frequency     VARCHAR(50),
    PRIMARY KEY (patient_id, medication_id),
    FOREIGN KEY (patient_id) REFERENCES PATIENT (patient_id),
    FOREIGN KEY (medication_id) REFERENCES MEDICATIONS (medication_id)
);

-- Bridge Tables for TREATMENT relationships
-- 12. TREATMENT to HEALTHCARE_PROVIDER
DROP TABLE IF EXISTS provider_treatment_record;
CREATE TABLE provider_treatment_record
(
    provider_id  INT NOT NULL,
    treatment_id INT NOT NULL,
    PRIMARY KEY (provider_id, treatment_id),
    FOREIGN KEY (provider_id) REFERENCES HEALTHCARE_PROVIDER (provider_id),
    FOREIGN KEY (treatment_id) REFERENCES TREATMENT (treatment_id)
);

-- 13. TREATMENT to MEDICAL_CONDITION
DROP TABLE IF EXISTS condition_treatment_protocol;
CREATE TABLE condition_treatment_protocol
(
    condition_id         INT NOT NULL,
    treatment_id         INT NOT NULL,
    effectiveness_rating INT,
    PRIMARY KEY (condition_id, treatment_id),
    FOREIGN KEY (condition_id) REFERENCES MEDICAL_CONDITION (condition_id),
    FOREIGN KEY (treatment_id) REFERENCES TREATMENT (treatment_id)
);

-- Bridge Tables for HEALTHCARE_PROVIDER relationships
-- 14. HEALTHCARE_PROVIDER to CLINICAL_PROTOCOL
DROP TABLE IF EXISTS provider_protocol_record;
CREATE TABLE provider_protocol_record
(
    provider_id INT NOT NULL,
    protocol_id INT NOT NULL,
    PRIMARY KEY (provider_id, protocol_id),
    FOREIGN KEY (provider_id) REFERENCES HEALTHCARE_PROVIDER (provider_id),
    FOREIGN KEY (protocol_id) REFERENCES CLINICAL_PROTOCOL (protocol_id)
);

-- 15. HEALTHCARE_PROVIDER to MEDICATIONS
DROP TABLE IF EXISTS provider_medication_record;
CREATE TABLE provider_medication_record
(
    provider_id   INT NOT NULL,
    medication_id INT NOT NULL,
    PRIMARY KEY (provider_id, medication_id),
    FOREIGN KEY (provider_id) REFERENCES HEALTHCARE_PROVIDER (provider_id),
    FOREIGN KEY (medication_id) REFERENCES MEDICATIONS (medication_id)
);

-- 16. HEALTHCARE_PROVIDER to PERMISSIONS
DROP TABLE IF EXISTS permission_provider_record;
CREATE TABLE permission_provider_record
(
    provider_id   INT NOT NULL,
    permission_id INT NOT NULL,
    granted_date  DATE,
    PRIMARY KEY (provider_id, permission_id),
    FOREIGN KEY (provider_id) REFERENCES HEALTHCARE_PROVIDER (provider_id),
    FOREIGN KEY (permission_id) REFERENCES PERMISSIONS (permission_id)
);

-- Bridge Tables for TREATMENT_OUTCOMES relationships
-- 17. TREATMENT_OUTCOMES to PATIENT_EDUCATION
DROP TABLE IF EXISTS outcome_education_record;
CREATE TABLE outcome_education_record
(
    outcome_id   INT NOT NULL,
    education_id INT NOT NULL,
    PRIMARY KEY (outcome_id, education_id),
    FOREIGN KEY (outcome_id) REFERENCES TREATMENT_OUTCOMES (outcome_id),
    FOREIGN KEY (education_id) REFERENCES PATIENT_EDUCATION (record_id)
);

-- 18. TREATMENT_OUTCOMES to PRESCRIPTIONS
DROP TABLE IF EXISTS prescription_outcome_record;
CREATE TABLE prescription_outcome_record
(
    outcome_id      INT NOT NULL,
    prescription_id INT NOT NULL,
    effectiveness   VARCHAR(50),
    PRIMARY KEY (outcome_id, prescription_id),
    FOREIGN KEY (outcome_id) REFERENCES TREATMENT_OUTCOMES (outcome_id),
    FOREIGN KEY (prescription_id) REFERENCES PRESCRIPTIONS (prescription_id)
);

-- Bridge Tables for MEDICATIONS relationships
-- 19. MEDICATIONS to PRESCRIPTIONS
DROP TABLE IF EXISTS medication_prescription_record;
CREATE TABLE medication_prescription_record
(
    medication_id   INT NOT NULL,
    prescription_id INT NOT NULL,
    dosage          VARCHAR(50),
    route           VARCHAR(50),
    PRIMARY KEY (medication_id, prescription_id),
    FOREIGN KEY (medication_id) REFERENCES MEDICATIONS (medication_id),
    FOREIGN KEY (prescription_id) REFERENCES PRESCRIPTIONS (prescription_id)
);

-- 20. MEDICATIONS to LAB_RESULTS
DROP TABLE IF EXISTS medication_administration;
CREATE TABLE medication_administration
(
    medication_id     INT NOT NULL,
    result_id         INT NOT NULL,
    administered_date DATE,
    PRIMARY KEY (medication_id, result_id),
    FOREIGN KEY (medication_id) REFERENCES MEDICATIONS (medication_id),
    FOREIGN KEY (result_id) REFERENCES LAB_RESULTS (result_id)
);

-- Bridge Tables for CARE_PATHWAY relationships
-- 21. CARE_PATHWAY to CARE_TASKS
DROP TABLE IF EXISTS pathway_task_record;
CREATE TABLE pathway_task_record
(
    pathway_id     INT NOT NULL,
    task_id        INT NOT NULL,
    sequence_order INT,
    PRIMARY KEY (pathway_id, task_id),
    FOREIGN KEY (pathway_id) REFERENCES CARE_PATHWAY (pathway_id),
    FOREIGN KEY (task_id) REFERENCES CARE_TASKS (task_id)
);

-- 22. CARE_PATHWAY to SOCIAL_DETERMINANTS
DROP TABLE IF EXISTS pathway_social_record;
CREATE TABLE pathway_social_record
(
    pathway_id     INT NOT NULL,
    determinant_id INT NOT NULL,
    impact_level   VARCHAR(20),
    PRIMARY KEY (pathway_id, determinant_id),
    FOREIGN KEY (pathway_id) REFERENCES CARE_PATHWAY (pathway_id),
    FOREIGN KEY (determinant_id) REFERENCES SOCIAL_DETERMINANTS (determinant_id)
);

-- Bridge Tables for SYMPTOMS relationships
-- 23. SYMPTOMS to CARE_TASKS
DROP TABLE IF EXISTS symptom_task_record;
CREATE TABLE symptom_task_record
(
    symptom_id INT NOT NULL,
    task_id    INT NOT NULL,
    PRIMARY KEY (symptom_id, task_id),
    FOREIGN KEY (symptom_id) REFERENCES SYMPTOMS (symptom_id),
    FOREIGN KEY (task_id) REFERENCES CARE_TASKS (task_id)
);

-- Bridge Tables for SOCIAL_DETERMINANTS relationships
-- 24. SOCIAL_DETERMINANTS to LAB_RESULTS
DROP TABLE IF EXISTS social_lab_record;
CREATE TABLE social_lab_record
(
    determinant_id       INT NOT NULL,
    result_id            INT NOT NULL,
    correlation_strength INT,
    PRIMARY KEY (determinant_id, result_id),
    FOREIGN KEY (determinant_id) REFERENCES SOCIAL_DETERMINANTS (determinant_id),
    FOREIGN KEY (result_id) REFERENCES LAB_RESULTS (result_id)
);

-- Bridge Tables for SYSTEM_USERS relationships
-- 25. SYSTEM_USERS to AUDIT_LOGS
DROP TABLE IF EXISTS user_system_record;
CREATE TABLE user_system_record
(
    user_id       INT NOT NULL,
    log_id        INT NOT NULL,
    access_reason VARCHAR(50),
    PRIMARY KEY (user_id, log_id),
    FOREIGN KEY (user_id) REFERENCES SYSTEM_USERS (user_id),
    FOREIGN KEY (log_id) REFERENCES AUDIT_LOGS (log_id)
);
