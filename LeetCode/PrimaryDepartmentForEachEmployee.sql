SELECT employee_id, (CASE WHEN COUNT(DISTINCT department_id) = 1 THEN MIN(department_id) ELSE
      MAX(CASE WHEN primary_flag = 'Y' THEN department_id END) END) AS department_id
FROM Employee
GROUP BY employee_id
