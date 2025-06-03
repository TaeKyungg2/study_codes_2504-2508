create user 'user02'@'localhost' #only  localhost can access;
identified by '1234';
grant all privileges on db.* to 'user02'@'localhost';
#mysql 8부터 문제 있을 경우 pip install cryptography