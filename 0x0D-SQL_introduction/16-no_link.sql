-- List all records excluding null values
SELECT score, name FROM second_table
	WHERE name IS NOT NULL AND name!=""
	ORDER BY score DESC;
