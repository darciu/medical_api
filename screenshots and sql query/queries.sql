--- Count average cost of prescriptions (Gross Cost) of all records loaded into the database
select avg(gross_cost) as avg_cost from kinesso_task.public.csv
;

--- Count average number of products (Total Items) of all the records loaded into the database
select avg(total_items) as avg_items from kinesso_task.public.csv
;

--- Count average price from all records loaded into the database for the 0601060D0CCAAA0 BNF Code
select avg(gross_cost) as avg_price from kinesso_task.public.csv
where bnf_code = '0601060D0CCAAA0'
;

--- Count number of all distinct codes (BNF Code)
select count(distinct bnf_code) as cnt from kinesso_task.public.csv
