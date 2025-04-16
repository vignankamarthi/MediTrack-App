-- Sample data for SOCIAL_DETERMINANTS table
-- Create 30-40 rows as specified in requirements

USE meditrack;

-- Insert sample social determinants here
-- Example:
-- INSERT INTO SOCIAL_DETERMINANTS (determinant_id, determinant_name, category, description)
-- VALUES (1, 'Housing Instability', 'Economic Stability', 'Lack of stable housing or risk of losing housing');

INSERT INTO SOCIAL_DETERMINANTS (determinant_id, determinant_name, category, description) VALUES
(1, 'Housing Instability', 'Economic Stability', 'Lack of stable housing or risk of losing housing'),
(2, 'Food Insecurity', 'Economic Stability', 'Limited or uncertain access to adequate food'),
(3, 'Unemployment', 'Economic Stability', 'Lack of stable employment or job loss'),
(4, 'Low Income', 'Economic Stability', 'Household income below poverty threshold'),
(5, 'Transportation Barriers', 'Economic Stability', 'Lack of reliable transportation for medical or daily needs'),
(6, 'Limited Education', 'Education Access', 'Less than high school education or equivalent'),
(7, 'Language Barriers', 'Education Access', 'Limited proficiency in primary language of healthcare system'),
(8, 'Low Health Literacy', 'Education Access', 'Difficulty understanding health information or instructions'),
(9, 'Lack of Internet Access', 'Education Access', 'No reliable access to internet for telehealth or information'),
(10, 'Social Isolation', 'Social Context', 'Limited social connections or support networks'),
(11, 'Domestic Violence', 'Social Context', 'Exposure to abuse or violence in the home'),
(12, 'Discrimination', 'Social Context', 'Experiences of bias based on race, gender, or other factors'),
(13, 'Incarceration History', 'Social Context', 'Past or current involvement with the criminal justice system'),
(14, 'Community Violence', 'Social Context', 'Exposure to violence or crime in the community'),
(15, 'Substance Use', 'Health Behaviors', 'Use of tobacco, alcohol, or illicit drugs'),
(16, 'Physical Inactivity', 'Health Behaviors', 'Lack of regular physical exercise or activity'),
(17, 'Poor Nutrition', 'Health Behaviors', 'Diet lacking in essential nutrients or balanced meals'),
(18, 'Uninsured Status', 'Healthcare Access', 'Lack of health insurance coverage'),
(19, 'Underinsured Status', 'Healthcare Access', 'Inadequate insurance coverage for medical needs'),
(20, 'Limited Healthcare Access', 'Healthcare Access', 'Difficulty accessing healthcare facilities or providers'),
(21, 'Mental Health Stigma', 'Healthcare Access', 'Reluctance to seek mental health care due to stigma'),
(22, 'Environmental Pollution', 'Physical Environment', 'Exposure to air, water, or soil pollutants'),
(23, 'Poor Housing Conditions', 'Physical Environment', 'Living in substandard or unsafe housing'),
(24, 'Lack of Green Spaces', 'Physical Environment', 'Limited access to parks or recreational areas'),
(25, 'Neighborhood Safety Concerns', 'Physical Environment', 'Perceived or actual lack of safety in community'),
(26, 'Childcare Barriers', 'Economic Stability', 'Lack of affordable or reliable childcare'),
(27, 'Financial Stress', 'Economic Stability', 'Stress due to debt or financial insecurity'),
(28, 'Cultural Barriers', 'Social Context', 'Cultural beliefs conflicting with medical recommendations'),
(29, 'Immigration Status', 'Social Context', 'Challenges related to undocumented or uncertain legal status'),
(30, 'Caregiver Burden', 'Social Context', 'Stress or strain from caring for family or dependents'),
(31, 'Medication Affordability', 'Healthcare Access', 'Difficulty affording prescribed medications'),
(32, 'Disability Barriers', 'Healthcare Access', 'Physical or cognitive limitations affecting care access'),
(33, 'Workplace Hazards', 'Economic Stability', 'Exposure to unsafe or unhealthy work conditions'),
(34, 'Lack of Social Services', 'Social Context', 'Limited access to community or government support programs'),
(35, 'Alcohol Dependency', 'Health Behaviors', 'Chronic reliance on alcohol affecting health'),
(36, 'Homelessness', 'Economic Stability', 'Lack of any fixed or stable residence'),
(37, 'Utility Insecurity', 'Economic Stability', 'Difficulty paying for electricity, water, or heat'),
(38, 'Exposure to Lead', 'Physical Environment', 'Risk of lead poisoning from environment or housing'),
(39, 'Religious Beliefs', 'Social Context', 'Religious practices impacting healthcare decisions'),
(40, 'Limited Public Transit', 'Physical Environment', 'Inadequate public transportation options for mobility');