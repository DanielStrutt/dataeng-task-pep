CREATE OR REPLACE VIEW steam_data.vw_price_categories AS
(

    WITH prices AS (

	SELECT 
	    appid,
	    CASE 
		    WHEN price = 0 THEN 1
	        WHEN price BETWEEN 0.01 AND 0.99 THEN 2
	        WHEN price BETWEEN 1.00 AND 1.99 THEN 3
	        WHEN price BETWEEN 2.00 AND 2.99 THEN 4
	        WHEN price BETWEEN 3.00 AND 3.99 THEN 5
	        WHEN price BETWEEN 4.00 AND 4.99 THEN 6
	        WHEN price BETWEEN 5.00 AND 5.99 THEN 7
	        WHEN price BETWEEN 6.00 AND 6.99 THEN 8
	        WHEN price BETWEEN 7.00 AND 7.99 THEN 9
	        WHEN price BETWEEN 8.00 AND 8.99 THEN 10
	        WHEN price BETWEEN 9.00 AND 9.99 THEN 11
	        WHEN price BETWEEN 10.00 AND 19.99 THEN 12
	        WHEN price BETWEEN 20.00 AND 29.99 THEN 13
	        WHEN price BETWEEN 30.00 AND 39.99 THEN 14
	        ELSE 15
	    END AS price_band_id
	    , CASE 
		    WHEN price = 0 THEN '0'
	        WHEN price BETWEEN 0.01 AND 0.99 THEN '0.01 - 0.99'
	        WHEN price BETWEEN 1.00 AND 1.99 THEN '1.00 - 1.99'
	        WHEN price BETWEEN 2.00 AND 2.99 THEN '2.00 - 2.99'
	        WHEN price BETWEEN 3.00 AND 3.99 THEN '3.00 - 3.99'
	        WHEN price BETWEEN 4.00 AND 4.99 THEN '4.00 - 4.99'
	        WHEN price BETWEEN 5.00 AND 5.99 THEN '5.00 - 5.99'
	        WHEN price BETWEEN 6.00 AND 6.99 THEN '6.00 - 6.99'
	        WHEN price BETWEEN 7.00 AND 7.99 THEN '7.00 - 7.99'
	        WHEN price BETWEEN 8.00 AND 8.99 THEN '8.00 - 8.99'
	        WHEN price BETWEEN 9.00 AND 9.99 THEN '9.00 - 9.99'
	        WHEN price BETWEEN 10.00 AND 19.99 THEN '10.00 - 19.99'
	        WHEN price BETWEEN 20.00 AND 29.99 THEN '20.00 - 29.99'
	        WHEN price BETWEEN 30.00 AND 39.99 THEN '30.00 - 39.99'
	        ELSE '40.00+'
	    END AS price_band
	FROM steam_data.main.steam_flattened

    )

    SELECT price_band
        , count(appid) AS games_count
        
    FROM prices

    GROUP BY price_band, price_band_id
        
    ORDER BY price_band_id ASC
);