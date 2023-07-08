# Database Management Systems CMU 95-703

# Table of Contents

1. Introduction to Databases
2. Advanced SQL

# 1. Introduction to Databases

- ### **What is a Database?**
  Organized collection of inner-related data that models some aspect of the real world.

- ### **Database management system (DBMS) Evolution**
  - **File System (flat files)**: Data is stored in files, each application has its own files.
    - **Problems**: 
      - Data integrity  </br>
        How to ensure that data is consistent and accurate? </br>
        What if we needed to delete a record and its related records?</br>

      - Implementation</br>
        How to implement the functionality of the database efficiently?</br>
        what if we needed to build another application that uses the same data?</br>
        What if two threads need to access the same data at the same time? (Concurrency)</br>
      - Durability</br>
        How to ensure that the data is not lost?</br>
        What if the computer crashes while updating the data?</br>
        What if i want to replicate the data to another computer?</br>
    - **Database Management System (DBMS)**: </br>
      Software that manages the storage, retrieval, and updating of data in a computer system.</br>
      A general-purpose software system that facilitates the process of defining, constructing, and manipulating databases for various applications.</br>
      - **Advantages**:
        - Data independence
        - Efficient data access
        - Data integrity and security
        - Data administration
        - Concurrent access and crash recovery
        - Reduced application development time
      - **Disadvantages**:
        - Complexity
        - Size
        - Cost of DBMS
        - Cost of conversion
      ---------------------------------------------------------------------------
      - **Data models**: </br>
        A collection of concepts that can be used to describe the structure of a database.</br>
      - **Schema**: </br>
        The description of a particular collection of data, using a given data model.</br>

# 2. Advanced SQL

- ### What is SQL?

  SQL (Structured Query Language) is a language that provides an interface to relational database systems.
  it's high-level, declarative, and non-procedural language. which means that you specify what you want, not how to get it.

- ### Aggregate Functions

  functions that operate on a set of values and return a single value. </br>

  - **AVG**: returns the average value of a numeric column.
  - **COUNT**: returns the number of rows that match a specified criteria.
  - **MAX**: returns the maximum value in a column.
  - **MIN**: returns the minimum value in a column.
  - **SUM**: returns the sum of the values in a column.
  </br>
  for example: </br>
  
  ```sql
  SELECT COUNT(login) AS cnt 
  FROM students WHERE login LIKE '%@cs';
  ```
  </br>
  Notes: 
  </br>

  - **DISTINCT**: returns the number of unique values in a column.
  - COUNT, SUM, AVG, support DISTINCT.
  - If you want to use aggregate functions with normal values, 
    you have to use use GROUP BY.
  - **GROUP BY**: groups rows that have the same values into summary rows.
    ```sql
    SELECT AVG(s.gpa) , e.cid FROM students s, enroll e
    WHERE e.sid = s.sid
    GROUP BY e.cid;
    ```
  - If you want to filter the result of aggregate functions, 
    you have to use use HAVING. </br>
    if you add your filters in the WHERE clause, it will throw an error.
  - **HAVING**: specifies a search condition for a group or an aggregate.
    ```sql
    SELECT AVG(s.gpa) AS avg_gpa , e.cid FROM students s, enroll e
    WHERE e.sid = s.sid
    GROUP BY e.cid;
    HAVING AVG(avg_gpa) > 3.0;
    ```

- ### String Operations

  here is a table that summarizes the Case sensitivity of string in different DBMSs.

  | DBMS | Case Sensitive | String Quotation |
  | ---- | -------------- | ---------------- |
  | SQL-92 | Sensitive | Single Only |
  | PostgreSQL | Sensitive | Single Only |
  | MySQL | Insensitive | Single or Double |
  | SQLit | Sensitive | Single or Double |
  | DB2 | Sensitive | Single Only |
  | Oracle | Sensitive | Single Only |

  - **LIKE**: is used in a WHERE clause to search for a pattern in a column.
    ```sql  
    SELECT * FROM students WHERE login LIKE '%@cs';
    ```
    - **%**: matches any number of characters, even zero characters.
    - **_**: matches exactly one character.
    <!-- - **[ ]**: matches any one of the enclosed characters. -->
    <!-- - **[^]**: matches any one character that is not enclosed. -->
    ```sql
    SELECT * FROM students WHERE login LIKE '%@c_';
    ```
  - **ILIKE**: is used in a WHERE clause to search for a pattern in a column, 
    but it's case insensitive.
  - **SUBSTRING**: extracts a substring from a string.
    ```sql
    SELECT SUBSTRING('Hello World', 7, 5);
    ```
  - **CONCAT**: concatenates two strings.
    ```sql
    SELECT CONCAT('Hello', 'World');
    ```
  There are many other string functions, you can check them out [here](https://www.postgresql.org/docs/9.5/functions-string.html).

- ### Date and Time operation

  Operations to manipulate and modify date and time values.

  - **NOW**: returns the current date and time.
    ```sql
    SELECT NOW();
    ```
  - **EXTRACT**: extracts a field from a date or time value.
    ```sql
    SELECT EXTRACT(YEAR FROM NOW());
    ```

  There are many other date and time functions, you can check them out [here](https://www.postgresql.org/docs/9.5/functions-datetime.html).

- ### Output redirection

  store the result of a query in another table.
  - new table
  ```sql
  CREATE TABLE CourseIds (
    Select DISTINCT cid FROM enroll
  );
  ```
  - existing table
  ```sql
  INSERT INTO CourseIds
    (Select DISTINCT cid FROM enroll);
  ```
  **Note**: </br>
  - If you want to store the result of a query in another table, 
    the columns of the result must match the columns of the table.

- ### Output control

  how to control the output of a query. like the number of rows, the order of rows, etc.

  - **LIMIT**: limits the number of rows returned by a query.
    ```sql
    SELECT * FROM students LIMIT 10;
    ```
  - **ORDER BY**: sorts the result of a query by a specified column.
    ```sql
    SELECT * FROM students ORDER BY gpa DESC;
    ```
  **Notes**: </br>
  - **ORDER BY** is ordered by ascending by default.
  - **ORDER BY** can be used with multiple columns.
    ```sql
    SELECT * FROM students ORDER BY gpa DESC, login ASC;
    ```

- ### Nested queries
  Queries that have other queries inside them.
  they are often difficult to optimize, so you should avoid them if possible.

  ```sql
  SELECT * FROM students WHERE sid IN (
    SELECT sid FROM enroll WHERE cid = '15-213'
  );
  ```

  - Example: </br>
    Find the names of students who are enrolled in 15-213.
    ```sql
    SELECT name FROM students WHERE sid IN (
      SELECT sid FROM enroll WHERE cid = '15-213'
    );
    ```
  
  - Expressions 
    - **IN**: returns true if a value matches any value in a list.
      ```sql
      SELECT * FROM students WHERE sid IN (
        SELECT sid FROM enroll WHERE cid = '15-213'
      );
      ```
    - **ALL**: returns true if all values are true.
      ```sql
      SELECT * FROM students WHERE gpa > ALL (
        SELECT gpa FROM students WHERE login LIKE '%@cs'
      );
      ```
      this query will return the students who have the highest gpa. among the students who have a cs email.
    - **ANY**: returns true if any of the subquery values meet the condition.
      ```sql
      SELECT * FROM students WHERE gpa > ANY (
        SELECT gpa FROM students WHERE login LIKE '%@cs'
      );
      ```
      this query will return the students who have a gpa higher than any student who has a cs email.
    - **EXISTS**: returns true if the subquery returns one or more records.
      ```sql
      SELECT * FROM students WHERE EXISTS (
        SELECT * FROM enroll WHERE sid = students.sid AND cid = '15-213'
      );
      ```

- ### Common Table Expressions (CTE)

  A temporary result set that is defined within the execution scope of a single SQL statement.
  They are similar to a derived table in that they are not stored as an object and they are only valid for the duration of the query.
  Unlike a derived table, a CTE can be self-referencing and can be referenced multiple times in the same query.

  ```sql
  WITH CourseIds AS (
    SELECT DISTINCT cid FROM enroll
  )
  SELECT * FROM CourseIds;
  ```

 - CTE - Recursive
    ```sql
    WITH RECURSIVE cteSource (num) AS (
      SELECT 1
      UNION ALL
      SELECT num + 1 FROM cteSource WHERE num < 100 
      )
    SELECT * FROM cteSource;
    ```