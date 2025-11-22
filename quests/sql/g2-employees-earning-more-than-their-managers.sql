select e.name as Employee
from employee e
join employee m
on m.id = e.managerId and e.salary > m.salary
