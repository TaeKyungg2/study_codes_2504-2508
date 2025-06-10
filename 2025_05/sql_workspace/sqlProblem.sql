select * from emp;
select * from emp where ename='smith'or ename='ford';
select * from emp where sal>=3000;
select * from emp where job='manager';
select * from emp where ename like 'A%'; # %:many char _ : one char
select * from emp where sal between 2000 and 5000; #enable mysql,oracle
select * from emp where deptno in(20,30);
select * from emp where sal<1000 or comm>500;
select * from emp where mgr is null;
select * from emp where job='clerk' and deptno='20';
select * from emp where ename like '%O%';
select * from emp where hiredate<'1981-01-01';
select empno from emp where empno in (7521,7565,7903);
select * from emp order by ename desc
#order by fieldname asc or desc(sort)
