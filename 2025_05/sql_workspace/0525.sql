use sakila;
select concat(first_name, ' ',last_name) as 배우이름 from actor;-- 1

select * from actor a where a.last_name in ('BERRY', 'HOFFMAN', 'DENCH' );
select * from actor a where a.last_name = 'BERRY' or a.last_name = 'HOFFMAN'or a.last_name ='DENCH'-- 2

select actor_id from actor a where a.first_name='SCARLETT';-- 3

select concat(first_name, ' ',last_name) as 배우이름 from actor a where a.actor_id in (2,18,34,56,77,88,120, 199, 192, 191);-- 4

select * from customer c where c.email='KATHLEEN.ADAMS@sakilacustomer.org'-- 5

select * from customer c where c.store_id=1 and last_name='MILLER';-- 6

select category_id from category c where c.name='Comedy';-- 7

select * from film f where f.rental_duration>7; -- 8

select * from film f where f.replacement_cost between 20 and 25; -- 9

select concat(first_name, ' ',last_name) as custname, rental_date from rental r -- 10
join customer c on c.customer_id=r.customer_id limit 10;

select concat(first_name, ' ',last_name) as custname, email from customer c 
order by create_date desc limit 5; -- 11

select title from film f
join film_category fc on fc.film_id=f.film_id
join category c on c.category_id=fc.category_id
where c.name='comedy';-- 12

select concat(first_name, ' ',last_name) as custname, rental_date 
from customer c
join rental r on r.customer_id=c.customer_id limit 10; -- 13

select concat(first_name, ' ',last_name) as custname, title
from film f join film_category fc on f.film_id=fc.film_id;
-- 14. 'Action' 장르의 영화를 빌린 고객 이름과 영화 제목을 조회하세요.

select concat(first_name, ' ',last_name) as custname, email from customer c
join address a on a.address_id=c.address_id
where a.district='Alberta';-- 15

select title, concat(first_name, ' ',last_name) as actorName from film f
join film_actor fa on fa.film_id=f.film_id
join actor a on a.actor_id=fa.actor_id
limit 10;-- 16

select first_name as custname,count(*) from customer c
join rental r on r.customer_id=c.customer_id
group by c.first_name;




