WITH ranked_salary AS (
   SELECT d.name AS Department, e.name AS Employee, Salary, DENSE_RANK() OVER(PARTITION BY d.id ORDER BY Salary DESC) AS ranking
   FROM Employee e
   JOIN Department d
   ON e.departmentID = d.id
)
SELECT Department, Employee, Salary
FROM ranked_salary
WHERE ranking <= 3
