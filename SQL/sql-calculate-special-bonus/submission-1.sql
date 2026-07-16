-- Write your query below
SELECT employee_id, 
    case
        when employee_id % 2 <> 0 AND name NOT LIKE 'M%' then salary
        else 0
    end as bonus
FROM employees
ORDER BY employee_id;
    