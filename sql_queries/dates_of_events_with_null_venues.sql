-- TASK: Provide date distribution of events of such trades whose all events have a null venue (anomaly)

WITH bad_events AS
--Get trade IDs of the trades that are open (OPEN_POSITION) and have at least one event that has a null venue.
(
SELECT ---+ parallel(16)
	DISTINCT xra.TRADE_ID_C
FROM CR_OWNER.XYZ_REPORT_ATTR xra
INNER JOIN CR_OWNER.XYZ_OPEN_POSITION xop
	ON xra.TRADE_ID_C = xop.REPLACE(UPPER(xop.TRADE_REF_C, 'ABCDEF:', '')
--....

WHERE xra.YYY_EVENT_C != 'YYY CCC'
	AND xra.TRADING_VENUE_C IS NULL -- Event attribute. 
	--A trade has multiple events. Some of the events may have this attribute NULL (should not). Further follow conditions that specify cases 
	--when it is not OK for an event to have a null venue.
	AND xra.HH_TYPE_C NOT IN ('Event1', 'Event2')
	AND EXTRACTVALUE(XMLTYPE(ue.MESSAGE_C),'//xxx:party[@id="Broker"]/xxx:partyName', 'xmlns:xxx="...."') != 'xyzxyz name'
	AND EXTRACTVALUE(XMLTYPE(ue.MESSAGE_C),'//xxx:party[@id="Broker"]/xxx:partyId'[@partyScheme = "..."]', 'xmlns:xxx="...."') != '123456'
/*....
*/
), 

venues_per_trade AS
--Check what venue values the trades from bad_events have (only null or also valid values).
(
SELECT --+ parallel(16)
	DISTINCT xra.TRADE_ID_C, xra.TRADING_VENUE_C 
FROM CR_OWNER.XYZ_REPORT_ATTR xra
INNER JOIN bad_events be
		ON be.TRADE_ID_C = xra.TRADE_ID_C
),

not_null_venues AS
-- Get trades that have at least one event with a venue specified.
(
SELECT --+ parallel(16)
	DISTINCT TRADE_ID_C
FROM venues_per_trade
WHERE TRADING_VENUE_C IS NOT NULL
),

all_null_venues 
-- Get trades whose all events have null venues
(
SELECT --+ parallel(16)
	DISTINCT TRADE_ID_C
FROM venues_per_trade
MINUS 
SELECT --+ parallel(16)
	DISTINCT TRADE_ID_C
FROM not_null_venues
)

-- Get the number of trades whose venue values are all null per trade execution date and trade event dates.
SELECT --+ parallel(16)
	TO_CHAR(err.TRADE_DATE_D, 'YYYY-MM') AS "Trade Execution Date"
	, TO_CHAR(err.LOAD_DATE_D, 'YYYY-MM') AS "Event Load Date"
	, COUNT(DISTINCT xra.TRADE_ID_C) AS "Trade Number"
FROM all_null_venues anv
INNER JOIN CR_OWNER.XYZ_REPORT_ATTR xra
	on anv.TRADE_ID_C = xra.TRADE_ID_C
GROUP BY
	TO_CHAR(err.TRADE_DATE_D, 'YYYY-MM')
	, TO_CHAR(err.LOAD_DATE_D, 'YYYY-MM')
ORDER BY 1 DESC, 2 DESC
;
