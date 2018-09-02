/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

SELECT CONCAT(NAME, '(' || SUBSTR(OCCUPATION, 1, 1) || ')' ) FROM OCCUPATIONS ORDER BY NAME;
SELECT 'There are a total of ' || COUNT(OCCUPATION) AS NUMOF, LOWER(OCCUPATION) || 's.' FROM OCCUPATIONS GROUP BY OCCUPATION ORDER BY NUMOF, OCCUPATION;
