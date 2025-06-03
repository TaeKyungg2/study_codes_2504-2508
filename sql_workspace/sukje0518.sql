use world;
select Name,Population from country where continent='asia';
select name,population from country where population >=100000000;
select name, indepyear from country where indepyear>=1900;
select name, population from city where population>=5000000;
select name from country where governmentform ='republic';
select counrtycode,language where language='spanish';
select name,population from city where countrycode='KOR';
select language from countrylanguage where isofficial='T';
select name,gnp from country where gnp is not null;
select * from country where name like '%united%';
/*
country 테이블에서 아시아(Asia)에 있는 나라들의 이름과 인구를 출력하라.
country 테이블에서 인구가 1억 이상인 나라들의 이름과 인구를 출력하라.
country 테이블에서 독립 연도가 1900년 이후인 나라의 이름과 독립 연도를 출력하라.
city 테이블에서 인구가 500만 이상인 도시의 이름과 인구를 출력하라.
country 테이블에서 국가 형태(GovernmentForm)가 'Republic'인 나라들의 이름을 출력하라.
countrylanguage 테이블에서 스페인어(Spanish)를 사용하는 나라들의 나라 코드와 언어를 출력하라.
city 테이블에서 'South Korea'의 국가 코드(KOR)를 가진 도시들의 이름과 인구를 출력하라.
countrylanguage 테이블에서 공용어(Official)로 지정된 언어들만 출력하라.
country 테이블에서 GNP(국민총생산)가 NULL이 아닌 나라의 이름과 GNP를 출력하라.
country 테이블에서 국가명에 'United'가 포함된 나라들을 출력하라.