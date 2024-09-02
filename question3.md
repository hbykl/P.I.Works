# SQL Questions
## Write the SQL queries to display the total amount earned by each employee's name and surname.
SELECT E.FirstName, E.LastName, SUM(P.Value) AS Total 
FROM Employee E
JOIN Payments P ON E.EmployeeID = P.EmployeeID
GROUP BY E.EmployeeID;

## Display all employees that have their names starting with the J letter.
SELECT * FROM Employee WHERE FirstName LIKE 'J%';