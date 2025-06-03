use w3schools;
select customername from customers as c 
where c.customerid not
in(
select customerid
from orders
);

select concat(firstname,' ',lastname) 
from employees as e
where e.employeeid=
(select employeeid from (select max(c) from
(select employeeid,count(employeeid) as c from orders
group by employeeid) as k
)as c);


select count(employeeid)
from(select employeeid from orders group by employeeid 
having count(employeeid)>=5 )as a;
