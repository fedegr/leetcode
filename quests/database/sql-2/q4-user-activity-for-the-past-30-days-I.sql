select
    activity_date as day,
    count(distinct user_id) as active_users
from 
    activity
where
     date_subtract(timestamp '2019-07-28', '30 days'::interval) <= activity_date and
    activity_date < timestamp '2019-07-28'
group by activity_date
