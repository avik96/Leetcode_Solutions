# Write your MySQL query statement below
SELECT event_day AS day, emp_id, (SUM(out_time) - sum(in_time)) AS total_time
FROM Employees
GROUP BY day, emp_id;