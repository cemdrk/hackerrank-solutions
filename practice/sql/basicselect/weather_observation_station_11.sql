/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
select * from
(
    SELECT DISTINCT CITY FROM STATION WHERE REGEXP_LIKE(UPPER(CITY), '[^AEIOU]$')
    UNION
    SELECT DISTINCT CITY FROM STATION WHERE REGEXP_LIKE(UPPER(CITY), '^[^AEIOU]')
);
