import random

count = 1

while count <= 10:
    print("INSERT INTO students(students_name, students_email)")
    print("VALUES ('" + "student" + str(count) + "', " + " '" + "student" + str(count) + "@university.edu');")
    count += 1

count = 1

while count <= 10:
    print("INSERT INTO professors(professors_name, professors_email)")
    print("VALUES ('" + "professor" + str(count) + "', " + " '" + "professor" + str(count) + "@university.edu');")
    count += 1


count = 1
students_id = random.randint(1, 10)
professors_id = random.randint(1, 10)

while count <= 10:
    print("INSERT INTO courses(courses_title, courses_students_id, courses_professors_id)")
    students_id = random.randint(1, 10)
    professors_id = random.randint(1, 10)
    print("VALUES ('English', " + str(students_id) + ", " + str(professors_id) + ");" )

    count += 1

while count in range(11, 21):
    print("INSERT INTO courses(courses_title, courses_students_id, courses_professors_id)")
    students_id = random.randint(1, 10)
    professors_id = random.randint(1, 10)
    print("VALUES ('Math', " + str(students_id) + ", " + str(professors_id) + ");" )

    count += 1

while count in range(21, 31):
    print("INSERT INTO courses(courses_title, courses_students_id, courses_professors_id)")
    students_id = random.randint(1, 10)
    professors_id = random.randint(1, 10)
    print("VALUES ('History', " + str(students_id) + ", " + str(professors_id) + ");" )

    count += 1

while count in range(31, 41):
    print("INSERT INTO courses(courses_title, courses_students_id, courses_professors_id)")
    students_id = random.randint(1, 10)
    professors_id = random.randint(1, 10)
    print("VALUES ('Economics', " + str(students_id) + ", " + str(professors_id) + ");" )

    count += 1

while count in range(41, 51):
    print("INSERT INTO courses(courses_title, courses_students_id, courses_professors_id)")
    students_id = random.randint(1, 10)
    professors_id = random.randint(1, 10)
    print("VALUES ('Biology', " + str(students_id) + ", " + str(professors_id) + ");" )

    count += 1

count = 1
students_id = random.randint(1, 10)
professors_id = random.randint(1, 10)
courses_id = random.randint(1, 50)

while count <= 100:
    print("INSERT INTO grades(grades_students_id, grades_professors_id, grades_courses_id, grades_letter)")
    students_id = random.randint(1, 10)
    professors_id = random.randint(1, 10)
    courses_id = random.randint(1, 50)
    print("VALUES (" + str(students_id) + ", " + str(professors_id) + ", " + str(courses_id) + ", " + str((round(random.uniform(0.5, 1), 2))) + ");")

    count += 1
