SELECT * 


FROM read_csv_auto('{csv_path}') 

WHERE price < 10 

LIMIT 5;