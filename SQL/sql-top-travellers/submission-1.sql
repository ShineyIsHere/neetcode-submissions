-- Write your query below
select users.name, COALESCE(SUM(rides.distance),0) as travelled_distance
FROM users
LEFT JOIN rides
ON users.id = rides.user_id
GROUP BY users.id
ORDER BY COALESCE(SUM(rides.distance),0) DESC, users.name ASC;