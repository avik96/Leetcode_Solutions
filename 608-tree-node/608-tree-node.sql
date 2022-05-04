# Write your MySQL query statement below
SELECT id, 
(CASE WHEN p_id IS NULL THEN 'Root'
        WHEN id IN (SELECT DISTINCT p_id FROM Tree) THEN 'Inner'
        ELSE 'Leaf' END
 ) as type
 FROM Tree
 ORDER BY id;