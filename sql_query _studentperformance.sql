
USE student_analysis;
CREATE TABLE student_data (
Student_ID INT,
Name VARCHAR(50),
Gender VARCHAR(10),
Math INT,
Science INT,
English INT,
Attendance INT,
Study_Hours INT
);
SELECT * FROM student_data;
SELECT Name, (Math + Science + English)/3 AS Average
FROM student_data
ORDER BY Average DESC
LIMIT 5;
SELECT AVG(Math + Science + English)/3
FROM student_data;