/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

SELECT
    CASE
        WHEN (A + B <= C) OR (A + C <= B ) OR (B + C <= A) THEN 'Not A Triangle'
        WHEN A=B AND B=C THEN 'Equilateral'
        WHEN (A=B AND A <> C) OR (A=C AND A<>B) OR (B=C AND A<>B) THEN 'Isosceles'
        ELSE 'Scalene'
   END
FROM TRIANGLES;
