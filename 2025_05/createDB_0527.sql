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

insert into tb_member(user_id, password,user_name,email,phone,regdate)
values('test1','1234','홍길동','hong@naver.com','010-1234-1234',now());

select * from tb_member;