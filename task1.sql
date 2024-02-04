CREATE TABLE Employees (
    Name VARCHAR(50),
    Position VARCHAR(50),
    Department VARCHAR(50),
    Salary DECIMAL(10, 2)
);


INSERT INTO Employees (Name, Position, Department, Salary)
VALUES ('Alex', 'Manager', 'Sales', 7000.00),
        ('John', 'Manager', 'Sales', 6000.00),
       ('Jane', 'Analyst', 'Finance', 4500.00),
       ('Mike', 'Developer', 'IT', 5500.00);


UPDATE Employees SET Position = 'Senior Manager' WHERE Name = 'John';


ALTER TABLE Employees ADD HireDate DATE;


UPDATE Employees SET HireDate = '2022-01-01' WHERE Name = 'John';
UPDATE Employees SET HireDate = '2022-02-01' WHERE Name = 'Jane';
UPDATE Employees SET HireDate = '2024-02-01' WHERE Name = 'Mike';
UPDATE Employees SET HireDate = '2024-03-02' WHERE Name = 'Alex';

SELECT * FROM Employees WHERE Position = 'Manager';

SELECT * FROM Employees WHERE Salary > 5000.00;


SELECT * FROM Employees WHERE Department = 'Sales';

SELECT AVG(Salary) FROM Employees;

DROP TABLE Employees;