mysql> UPDATE Renters SET num_loans = 6 WHERE id = 1;
Query OK, 1 row affected (0.007 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT * FROM Renters WHERE id = 1;
+----+--------------+-----------+
| id | name         | num_loans |
+----+--------------+-----------+
|  1 | Jacob Dreier |         6 |
+----+--------------+-----------+

