/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/


SELECT * FROM
(SELECT CITY, LENGTH(CITY) AS CLEN  FROM STATION ORDER BY CLEN ASC, CITY ASC)
WHERE ROWNUM = 1
UNION
SELECT * FROM
(SELECT CITY, LENGTH(CITY) AS CLEN  FROM STATION ORDER BY CLEN DESC, CITY ASC)
WHERE ROWNUM = 1;
