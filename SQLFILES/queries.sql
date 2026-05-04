mysql> SELECT * FROM Renters;
+----+------------------+-----------+
| id | name             | num_loans |
+----+------------------+-----------+
|  1 | Jacob Dreier     |         5 |
|  2 | Owen Milota      |         3 |
|  3 | Timoty Siebrecht |         8 |
|  4 | Aiden Sundermann |         2 |
|  5 | Pascal Davis     |         1 |
|  6 | Grace Person     |         6 |
|  7 | Evan Santos      |        13 |
|  8 | Carson Rickard   |         4 |
|  9 | Ronan Hubbard    |         6 |
| 10 | Jacob Casey      |         1 |
+----+------------------+-----------+
10 rows in set (0.000 sec)


mysql> UPDATE Renters SET num_loans = 6 WHERE id = 1;
Query OK, 1 row affected (0.007 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT * FROM Renters WHERE id = 1;
+----+--------------+-----------+
| id | name         | num_loans |
+----+--------------+-----------+
|  1 | Jacob Dreier |         6 |
+----+--------------+-----------+


mysql> DELETE FROM Renters WHERE id = 4;
Query OK, 1 row affected (0.004 sec)

mysql> SELECT * FROM Renters;
+----+------------------+-----------+
| id | name             | num_loans |
+----+------------------+-----------+
|  1 | Jacob Dreier     |         5 |
|  2 | Owen Milota      |         3 |
|  3 | Timoty Siebrecht |         8 |
|  5 | Pascal Davis     |         1 |
|  6 | Grace Person     |         6 |
|  7 | Evan Santos      |        13 |
|  8 | Carson Rickard   |         4 |
|  9 | Ronan Hubbard    |         6 |
| 10 | Jacob Casey      |         1 |
+----+------------------+-----------+
9 rows in set (0.000 sec)


mysql> SELECT * FROM Active_Loans;
+----+-----------+----------+---------+----------------+-----------------+
| id | renter_id | media_id | home_id | check_out_date | loan_expiration |
+----+-----------+----------+---------+----------------+-----------------+
|  1 |         1 |        1 |       3 | 2024-01-10     | 2024-02-10      |
|  2 |         2 |        2 |       4 | 2024-02-15     | 2024-03-15      |
|  3 |         3 |        3 |       7 | 2024-03-01     | 2024-04-01      |
|  5 |         5 |        5 |       6 | 2024-04-01     | 2024-05-01      |
|  6 |         6 |        6 |       2 | 2024-04-10     | 2024-05-10      |
|  7 |         7 |        7 |       8 | 2024-05-01     | 2024-06-01      |
|  8 |         8 |        8 |       9 | 2024-05-15     | 2024-06-15      |
|  9 |         9 |        9 |      10 | 2024-06-01     | 2024-07-01      |
| 10 |        10 |       10 |       1 | 2024-06-10     | 2024-07-10      |
+----+-----------+----------+---------+----------------+-----------------+
9 rows in set (0.000 sec)


mysql> SELECT * FROM Media_Types;
+----+-------------+----------+
| id | type        | category |
+----+-------------+----------+
|  1 | DVD         | Movie    |
|  2 | Blu-Ray     | Movie    |
|  3 | VHS         | Movie    |
|  4 | CD          | Music    |
|  5 | Vinyl       | Music    |
|  6 | Cassette    | Music    |
|  7 | VCD         | Movie    |
|  8 | LaserDisk   | Movie    |
|  9 | 8-TrackTape | Music    |
| 10 | BetaMax     | Movie    |
+----+-------------+----------+
10 rows in set (0.000 sec)


mysql> SELECT * FROM Media_Names;
+----+-------------+------------------------------------+--------------+----------+---------+
| id | location_id | name                               | acquiry_date | quantity | type_id |
+----+-------------+------------------------------------+--------------+----------+---------+
|  1 |           3 | Tomorrowland                       | 2020-03-15   |        3 |       1 |
|  2 |           4 | Startrek into darkness             | 2023-07-20   |        4 |       2 |
|  3 |           7 | Wallace & Grommit: A Grand Day Out | 1995-04-20   |        1 |       3 |
|  4 |           5 | 90125                              | 2022-04-08   |        5 |       4 |
|  5 |           6 | Interstellar Album                 | 2026-01-29   |        1 |       5 |
|  6 |           2 | Top Gun Soundtrack                 | 2021-02-15   |        2 |       6 |
|  7 |           8 | The Simpsons Greatest Hits         | 2019-05-18   |        3 |       7 |
|  8 |           9 | Back to the Future                 | 1990-07-23   |        3 |       8 |
|  9 |          10 | Elvis Burning Love                 | 2001-04-07   |        3 |       9 |
| 10 |           1 | A Christmas Carol                  | 1999-02-27   |        3 |      10 |
+----+-------------+------------------------------------+--------------+----------+---------+
10 rows in set (0.000 sec)

    mysql> INSERT INTO Renters (name, num_loans) VALUES
    -> ('Aiden Sundermann', 2);
Query OK, 1 row affected (0.005 sec)

mysql> SELECT * FROM Renters;
+----+------------------+-----------+
| id | name             | num_loans |
+----+------------------+-----------+
|  1 | Jacob Dreier     |         5 |
|  2 | Owen Milota      |         3 |
|  3 | Timoty Siebrecht |         8 |
|  5 | Pascal Davis     |         1 |
|  6 | Grace Person     |         6 |
|  7 | Evan Santos      |        13 |
|  8 | Carson Rickard   |         4 |
|  9 | Ronan Hubbard    |         6 |
| 10 | Jacob Casey      |         1 |
| 11 | Aiden Sundermann |         2 |
+----+------------------+-----------+
10 rows in set (0.000 sec)

mysql> SELECT * FROM Locations;
+----+-----------+------------------------------------------+
| id | name      | address                                  |
+----+-----------+------------------------------------------+
| 10 | Arvada    | 7525 W 57th Ave, Arvada, CO 80002        |
|  1 | Belmar    | 555 S Allison Pkwy, Lakewood, CO 80226   |
|  5 | Columbine | 7706 W Bowles Ave, Littleton, CO 80123   |
|  9 | Cortez    | 202 N Park St, Cortez, CO 81321          |
|  3 | Denver    | 10 W 14th Ave, Denver, CO 80204          |
|  8 | Durango   | 1900 E 3rd Ave, Durango, CO 81301        |
|  6 | Englewood | 1000 Englewood Pkwy, Englewood, CO 80110 |
|  4 | Evergreen | 5000 County Hwy 73, Evergreen, CO 80439  |
|  2 | Golden    | 1019 10th St, Golden, CO 80401           |
|  7 | Pueblo    | 1315 E 7th St, Pueblo, CO 81001          |
+----+-----------+------------------------------------------+
10 rows in set (0.001 sec)