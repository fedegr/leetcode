with feb_orders as (
    select product_id, sum(unit) unit
    from orders
    where extract(year from order_date) = 2020 and extract(month from order_date) = 2
    group by product_id
)
select product_name, unit
from feb_orders o
join products p
    on o.product_id = p.product_id
    and o.unit >= 100
