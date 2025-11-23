select
    substr(trans_date::text,1, 7) as month,
    country,
    count(id) as trans_count,
    sum(case when state = 'approved' then 1 else 0 end) approved_count,
    sum(amount) trans_total_amount,
    sum(case when state = 'approved' then amount else 0 end) as approved_total_amount
from transactions
group by 
    substr(trans_date::text,1, 7),
    country
