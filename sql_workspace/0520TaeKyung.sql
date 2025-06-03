#w3school 말고 sakila 로 몇문제 풀어버렸는데 더 어려우니까 봐주세요
use sakila;
select * from customer c
join address a on a.address_id=c.address_id
join city ci on ci.city_id=a.city_id
join country co on ci.country_id=co.country_id
where co.country='germany'; -- 1

select c.customer_id,concat(c.first_name,' ',c.last_name) as name,co.country from customer c
join address a on a.address_id=c.address_id
join city ci on ci.city_id=a.city_id
join country co on ci.country_id=co.country_id
where co.country in('Austria', 'USA', 'Poland', 'Denmark')-- 2

select co.country, count(*) as customer_count from customer c
join address a on a.address_id=c.address_id
join city ci on ci.city_id=a.city_id
join country co on ci.country_id=co.country_id
group by co.country;-- 3

select co.country, count(*) as customer_count from customer c
join address a on a.address_id=c.address_id
join city ci on ci.city_id=a.city_id
join country co on ci.country_id=co.country_id
group by co.country
having count(*)>=5;-- 4

select count(*) as B_count from customer c
join address a on a.address_id=c.address_id
join city ci on ci.city_id=a.city_id
join country co on ci.country_id=co.country_id
where co.country like 'B%';-- 5

select concat(c.first_name,' ',c.last_name)as customer_name,ci.city,co.country  from customer c
join address a on a.address_id=c.address_id
join city ci on ci.city_id=a.city_id
join country co on ci.country_id=co.country_id
where ci.city='london';-- 6

use w3schools;

select o.orderid,c.customername from orders o
join customers c on c.customerid=o.customerid
where o.orderdate between '1996-07-01' and '1996-09-30';-- 7

select o.orderid,c.customername from orders o
join customers c on c.customerid=o.customerid
where o.orderdate between '1996-07-01' and '1996-09-30'
order by c.customername;-- 8

select k.pd,k.quantity,pro.price from (select p.productname as pd,sum(od.quantity) as quantity from shippers s
join orders o on o.shipperid=s.shipperid
join orderdetails od on od.orderid=o.orderid
join products p on od.productid=p.productid
where s.shippername='federal shipping'
group by p.productname) as k
join products pro on pro.productname=k.pd;-- 9
-- 1. Customers 테이블에서 나라가 Germany인 나라의 정보 전체 
-- 2. Customers 테이블에서 나라가 Austria, USA, Poland, Denmark
--    에 사는 고객리스트 
-- 3. 각자 나라별로 고객이 몇명씩 있는지 확인 
-- 4. 나라별로 고객이 5명 이상인 나라 목록만 조회 
-- 5. 나라이름이 B로 시작하는 나라들의 고객 전체 합 
-- 6. 나라는 UK 도시명은 London 에 있는 고객들 이름 목록 
-- 7. 주문날짜가 '1996-07-01'~'1996-09-30' 일까지의 주문아이디와 
--  고객이름 
-- 8.  위의 7번 문제를 고객이름 오름차순으로 정렬하여 출력하기
-- 9.  배달자가 Federal Shipping 인 경우의 상품명 가격 수량 만 