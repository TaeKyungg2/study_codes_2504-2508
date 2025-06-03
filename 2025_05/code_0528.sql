-- only root can make DB, account
create database project1;

-- create uesr.
create user 'user03'@'localhost' identified by '1234';

-- Give privilege of project1 for user03.
grant all privileges on project1.* to 'user03'@'localhost';
use project1;
create table tb_member(
	member_id bigint auto_increment primary key,
	user_id varchar(40),
	password varchar(300), -- use md5 Encryption algorithm and save.
	user_name varchar(40),
	email varchar(40),
	phone varchar(40),
	regdate datetime
);
use project1;
insert into tb_member(user_id, password,user_name,email,phone,regdate)
values('test1','1234','홍길동','hong@naver.com','010-1234-1234',now());

select * from tb_member;
use mydb2;
select * from tb_score;
create table tb_score(
	id bigint primary key auto_increment,
	sname varchar(20),
	kor int ,
	eng int,
	mat int,
	total int generated always as (kor+eng+mat) stored,
	average float generated always as ((kor+eng+mat)/3) stored,
	regdate datetime default CURRENT_TIMESTAMP
);

drop table tb_score;
DELIMITER $$
create trigger dat
before insert on tb_score
	FOR EACH ROW
	set new.grade = case when average between 90 and 100 then "A"
						when average between 80 and 89 then "B"
						when average between 70 and 79 then "C"
						when average between 60 and 69 then "D"
						else "E"
					end;
$$
delimiter;
select count(*) as stuCount
from tb_score;
select count(*) c,t.grade
from tb_score t 
group by t.grade;


ALTER TABLE tb_score ADD COLUMN grade varchar(1);



select * from tb_score;
ALTER TABLE tb_score ADD COLUMN grade varchar(2);
use mydb2;
create table test1(
	id int primary key,
	field varchar(10))

create table test2 as select * from test1;
select * from test1;
select * from text2;
select max(id) from test1;

use sakila;
select * from(select concat(c.first_name,' ',c.last_name) as name, a.address,a.district,a.postal_code
from customer c
join address a on a.address_id=c.address_id) as x  where x.name="MARY SMITH";

select '모든 사람', count(*)
from (select concat(c.first_name,' ',c.last_name) as name, a.address,a.district as di,a.postal_code
from customer c
join address a on a.address_id=c.address_id)as x
union
select count(*),x.di
from (select concat(c.first_name,' ',c.last_name) as name, a.address,a.district as di,a.postal_code
from customer c
join address a on a.address_id=c.address_id)as x
group by x.di;