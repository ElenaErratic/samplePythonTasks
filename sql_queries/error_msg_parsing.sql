/*TASK: Count the occurrences of all error types per month across different asset classes (types of traded objects).
The incoming error messages have no delimiters, may contain several occurrences of different error types or the same error type. Example:
"org.xml.sax.SAXParseException; lineNumber 63; columnNumber: 46; cvc-complex-type.2.4.a: Invalid content was found starting with element ''. One of '{}' is expected.
org.xml.sax.SAXParseException; lineNumber 64; columnNumber: 47; cvc-complex-type.2.4.b: The content of element '' is not complete. One of '{}' is expected."

The procedure 
	per each asset class
	1) extract XSD error descriptions, 
	2) match them with manually verified descriptions and count the occurrences,
	for all asset classes
	3) aggregate the results per each asset class in one uniform report.

Report:
Asset Class			Date 		Month 	XSD Error		Number or errors
Bonds				2022-06 	June	....			26
Bonds				2022-05		May	....			15
...
Listed Derivatives		2022-06		June	....			55
....
*/


WITH ld_error_bounds (LOAD_DATE_D, str, start_pos, end_pos) AS
(
SELECT LOAD_DATE_D
	, CAST(ERROR_C AS VARCHAR(2000))
	, -1
	, INSTR(ERROR_C, 'columnNumber', 1)
FROM LD_OWNER.XYZ_REPORT
WHERE LOAD_DATE_D >= TO_DATE('2021-12-01', 'YYYY-MM-DD')
	AND ERROR_C IS NOT NULL
	
UNION ALL
SELECT LOAD_DATE_D
	, str
	, end_pos + 2
	, INSTR(str, 'columnNumber', end_pos + 2)
FROM ld_error_bounds
WHERE end_pos > 0
ORDER BY LOAD_DATE_D
),

ld_errors AS
(
SELECT LOAD_DATE_D
	, CASE end_pos
	WHEN 0
	THEN SUBSTR(str, start_pos)
	ELSE SUBSTR(str, start_pos, end_pos - start_pos)
	END AS SUBSTRINGS
FROM ld_error_bounds
),

ld AS
(
SELECT 'Listed Derivatives' AS "Asset Class"
	, TO_CHAR(err.LOAD_DATE_D, 'YYYY-MM') AS "Date"
	, TO_CHAR(err.LOAD_DATE_D, 'Month') AS "Month"
	, CASE WHEN err.SUBSTRINGS LIKE '%cvc-complex-type2.4.b.%' THEN 'cvc-complex-type.2.4.b. The content of element is not complete'
		WHEN err.SUBSTRINGS LIKE '%cvc-complex-type2.4.a.%' THEN 'cvc-complex-type.2.4.a. Invalid content was found starting with element' 
		-- ....
		ELSE 'Other' END AS "XSD Error"
	, COUNT(err.SUBSTRINGS) AS "Number of errors"
		
FROM ld_errors err
WHERE LENGTH(err.SUBSTRINGS) > 1
GROUP BY 
	'Listed Derivatives' AS "Asset Class"
	, TO_CHAR(err.LOAD_DATE_D, 'YYYY-MM')
	, TO_CHAR(err.LOAD_DATE_D, 'Month')
	, CASE WHEN err.SUBSTRINGS LIKE '%cvc-complex-type2.4.b.%' THEN 'cvc-complex-type.2.4.b. The content of element is not complete'
		WHEN err.SUBSTRINGS LIKE '%cvc-complex-type2.4.a.%' THEN 'cvc-complex-type.2.4.a. Invalid content was found starting with element' 
		-- ....
		ELSE 'Other' END 
),

ir_error_bounds AS 
----- ....


SELECT * FROM ld
UNION
SELECT * FROM ir
UNION
---...
ORDER BY 1, 2 DESC, 5 DESC
;
