-- This script will sum the fans based on their country of origin in the holberton.metal_bands table.
SELECT origin, SUM(fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
