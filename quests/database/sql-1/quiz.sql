select e.employee_id
from employees as e
left join employees as m
    on m.employee_id = e.manager_id
where e.salary < 30000 and not e.manager_id is null and m.employee_id is null 
order by employee_id
