/*Compare incoming and outgoing values (whether they comply with the applicable business rules) 

Incoming: CR_OWNER.MIS_ATTR - attributes extracted from upstream messages for the purposes of reporting

Outgoing: CR_OWNER.XYZ_REPORT.REPORT_C - report in a BLOB format
	JURISDICTION_C - code of the jurisdiction for which the report is generated. Multiple jurisdictions per this schema.

*/

SELECT --+ parallel(16)
	DISTINCT ma.TRADING_VENUE_C
	, CASE WHEN TO_CLOB(rep.REPORT_C) LIKE '%' || ma.TRADING_VENUE_C || '%' THEN 'MIC'
		WHEN TO_CLOB(rep.REPORT_C) LIKE '%XOFF%' THEN 'XOFF' 
		END "Reported Venue"
	, CASE WHEN ma.ISIN_C IS IS NOT NULL
		AND TO_CLOB(rep.REPORT_C) LIKE '%' || ma.ISIN_C || '%' 
		THEN 'Y'
		END "Instrument is reported"
FROM CR_OWNER.MIS_ATTR ma
INNER JOIN CR_OWNER.XYZ_REPORT rep
	ON rep.TRADE_EVENT_I=ma.TRADE_EVENT_I
WHERE rep.JURISDICTION_C = 'EMIR'
ORDER BY 1;