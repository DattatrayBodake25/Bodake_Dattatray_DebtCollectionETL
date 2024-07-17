-- create a new database named 'debt_collection'
CREATE DATABASE debt_collection;

-- Use the created database
USE debt_collection;

-- create table named "borrowers"
CREATE TABLE borrowers (
    name VARCHAR(255),
    date_of_birth DATE,
    gender VARCHAR(50),
    marital_status VARCHAR(50),
    phone_number VARCHAR(20),
    email_address VARCHAR(255),
    mailing_address TEXT,
    language_preference VARCHAR(50),
    geographical_location VARCHAR(100),
    credit_score INT,
    loan_type VARCHAR(50),
    loan_amount DECIMAL(15, 2),
    loan_term INT,
    interest_rate DECIMAL(5, 2),
    loan_purpose VARCHAR(255),
    emi DECIMAL(15, 2),
    ip_address VARCHAR(50),
    geolocation VARCHAR(100),
    repayment_history TEXT,
    days_left_to_pay_current_emi INT,
    delayed_payment VARCHAR(3)
);

-- showing tabes in database 
SHOW tables;

-- select the all rows from borrowers table
SELECT * FROM borrowers;

-- Basic Analysis SQL Script
-- A. What is the average loan amount for borrowers who are more than 5 days past due?
SELECT AVG(loan_amount) AS average_loan_amount
FROM borrowers
WHERE delayed_payment = 'Yes' AND days_left_to_pay_current_emi > 5;   -- output is --> average_loan_amount = 55252.487861

-- B. Who are the top 10 borrowers with the highest outstanding balance?
SELECT Name, Loan_Amount - SUM(EMI) AS Outstanding_Balance
FROM borrowers
GROUP BY Name, Loan_Amount
ORDER BY Outstanding_Balance DESC
LIMIT 10;


-- C. List of all borrowers with good repayment history
SELECT Name, Repayment_History
FROM Borrowers
WHERE Delayed_Payment = 'No';

-- D. Brief analysis wrt loan type
SELECT Loan_Type,
       COUNT(*) AS Number_of_Borrowers,
       AVG(Credit_Score) AS Average_Credit_Score,
       AVG(Loan_Amount) AS Average_Loan_Amount,
       AVG(Interest_Rate) AS Average_Interest_Rate
FROM Borrowers
GROUP BY Loan_Type;

-- Loan Purpose Analysis by Loan Type
SELECT Loan_Type,
       Loan_Purpose,
       COUNT(*) AS Number_of_Borrowers
FROM Borrowers
GROUP BY Loan_Type, Loan_Purpose
ORDER BY Loan_Type, Number_of_Borrowers DESC;

-- Geographical Analysis of Borrowers by Loan Type
SELECT Loan_Type,
       Geographical_Location,
       COUNT(*) AS Number_of_Borrowers
FROM Borrowers
GROUP BY Loan_Type, Geographical_Location
ORDER BY Loan_Type, Number_of_Borrowers DESC;

-- Loan Term Analysis by Loan Type
SELECT Loan_Type,
       Loan_Term,
       COUNT(*) AS Number_of_Borrowers
FROM Borrowers
GROUP BY Loan_Type, Loan_Term
ORDER BY Loan_Type, Loan_Term;