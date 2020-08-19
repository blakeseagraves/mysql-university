USE university_schema;
 
-- Average grade that is given by each professor 
SELECT CAST(AVG(grades_letter) AS Decimal(3,2)) AS 'Average Grade' ,  professors_name AS 'Professor Name'
FROM grades 
JOIN professors
ON grades.grades_professors_id = professors_id
GROUP BY grades_professors_id;

-- Top grades for each student 
SELECT MAX(grades_letter) AS 'Highest Grade', students_name AS 'Student Name'
FROM grades
JOIN students
ON grades.grades_students_id = students_id
GROUP BY grades_students_id;

-- Group students by the course that they are enrolled in
SELECT courses_title AS 'Course Title', students_name AS 'Student Name'
FROM courses
JOIN students
ON courses.courses_students_id = students_id
ORDER BY courses_title;

-- Create a summary report of courses and their average grades, sorted by the most challenging course 
-- (course with the lowest average grade) to the easiest course
SELECT CAST(AVG(grades_letter) AS Decimal(3,2)) AS 'Average grade' , grades_courses_title AS 'Course Title'
FROM grades
GROUP BY grades_courses_title
ORDER BY grades_letter ASC;

-- Finding which student and professor have the most courses in common 
SELECT students_name AS 'Student Name', professors_name AS 'Professor Name', COUNT(*) AS 'Courses in Common'
FROM courses
JOIN students
ON courses.courses_students_id = students_id
JOIN professors
ON courses.courses_professors_id = professors_id
GROUP BY 1, 2
ORDER BY count(*) DESC;
