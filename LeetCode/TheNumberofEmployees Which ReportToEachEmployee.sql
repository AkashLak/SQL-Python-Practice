SELECT e1.employee_id, e1.name, COUNT(DISTINCT e2.employee_id) AS reports_count, ROUND(AVG(e2.age), 0) AS average_age
FROM Employees e1
JOIN Employees e2
ON e1.employee_id = e2.reports_to
GROUP BY e1.employee_id
HAVING COUNT(DISTINCT e2.employee_id) >= 1
ORDER BY e1.employee_id
