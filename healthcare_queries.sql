 
-- Create healthcare table
CREATE TABLE healthcare (
    Name VARCHAR(255),
    Age INT,
    Gender VARCHAR(10),
    Blood_Type VARCHAR(5),
    Medical_Condition VARCHAR(100),
    Date_of_Admission DATE,
    Doctor VARCHAR(255),
    Hospital VARCHAR(255),
    Insurance_Provider VARCHAR(255),
    Billing_Amount DECIMAL(15,2),
    Room_Number INT,
    Admission_Type VARCHAR(50),
    Discharge_Date DATE,
    Medication VARCHAR(255),
    Test_Results VARCHAR(50)
);

-- What is the total number of male and female patients?
SELECT Gender, COUNT(*) AS count 
FROM healthcare
GROUP BY Gender;

-- Which gender has the highest number of patients in each age group?
SELECT Gender,
       CASE 
           WHEN Age BETWEEN 0 AND 5 THEN '0-5'
           WHEN Age BETWEEN 6 AND 12 THEN '6-12'
           WHEN Age BETWEEN 13 AND 18 THEN '13-18'
           WHEN Age BETWEEN 19 AND 30 THEN '19-30'
           WHEN Age BETWEEN 31 AND 50 THEN '31-50'
           WHEN Age BETWEEN 51 AND 64 THEN '51-64'
           ELSE '65+' 
       END AS Age_Group,
       COUNT(*) AS Total_Patients
FROM healthcare
GROUP BY Gender, Age_Group
ORDER BY Gender, Age_Group;

-- Which diseases are associated with the highest or lowest average age? 
-- Which diseases have a broader age range of impact? Or do most diseases primarily affect a specific age group?
SELECT Medical_Condition, ROUND(AVG(Age), 0) AS Average_Age
FROM healthcare
GROUP BY Medical_Condition
ORDER BY Average_Age DESC;

-- What are the most common medical symptoms among patients
SELECT Medical_Condition, COUNT(*) AS count
FROM healthcare
GROUP BY Medical_Condition
ORDER BY count DESC;

-- Which medical conditions are more common among males and females? 
-- Is the overall number of medical conditions higher in males or females, or is it evenly distributed?
SELECT Gender, Medical_Condition, COUNT(*) AS count
FROM healthcare
GROUP BY Gender, Medical_Condition
ORDER BY Gender, count DESC;

-- Which age group has the highest number of cases for each medical condition?
SELECT Medical_Condition,
       CASE 
           WHEN Age BETWEEN 0 AND 5 THEN '0-5'
           WHEN Age BETWEEN 6 AND 12 THEN '6-12'
           WHEN Age BETWEEN 13 AND 18 THEN '13-18'
           WHEN Age BETWEEN 19 AND 30 THEN '19-30'
           WHEN Age BETWEEN 31 AND 50 THEN '31-50'
           WHEN Age BETWEEN 51 AND 64 THEN '51-64'
           ELSE '65+' 
       END AS Age_Group,
       COUNT(*) AS Total_Patients
FROM healthcare
GROUP BY Medical_Condition, Age_Group
ORDER BY Medical_Condition, Age_Group;

-- What is the most prescribed medication for each medical condition?
SELECT medical_condition, medication, COUNT(*) AS prescribed_count
FROM healthcare
GROUP BY medical_condition, medication
ORDER BY prescribed_count DESC;

-- What is the most common medical conditions by blood type?
SELECT blood_type, medical_condition, COUNT(*) AS total_patients
FROM healthcare
GROUP BY blood_type, medical_condition
ORDER BY total_patients DESC;

-- What are the most common medical conditions each year?
SELECT 
    YEAR(Date_of_Admission) AS Year,
    Medical_Condition, 
    COUNT(*) AS Condition_Count
FROM healthcare
GROUP BY YEAR(Date_of_Admission), Medical_Condition
ORDER BY Year,Condition_Count;

-- Which medical condition had the highest billing amount each year?
SELECT 
    YEAR(Discharge_Date) AS Year, 
    Medical_Condition, 
    ROUND(MAX(Billing_Amount), 2) AS Max_Billing

FROM healthcare
GROUP BY YEAR(Discharge_Date), Medical_Condition
ORDER BY Year DESC, Max_Billing DESC;