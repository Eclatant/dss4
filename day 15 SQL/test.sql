
# 데이터베이스 생성. 이미 있다면 삭제 후, 생성
DROP SCHEMA IF EXISTS test;
CREATE SCHEMA test;
USE test;


# 테이블 생성
CREATE TABLE students (
   ID INT(11) NOT NULL AUTO_INCREMENT, # ID 정수형. NULL값 허용하지 않음. 자동 증가하도록 설정
   Name CHAR(35) NOT NULL DEFAULT '', # Bame 문자열 35자. NULL값 허용하지 않음. 기본값 ''
   Age  int(11) NOT NULL DEFAULT 25,
   MajorCode VARCHAR(10), # MajorCode 문자열 10자.
  PRIMARY KEY (ID) # 프라이머리 키는 ID 필드
) DEFAULT CHARSET=utf8;

# students 테이블 조회
select * from students;

# 데이터 삽입
insert into students values(1, "Aaron", 31, 'CS');
insert into students values(2, "Bob", 30, 'BIO');
insert into students values(3, "Alice", 24, 'PHIL');

# ID필드가 auto increment로 되어있으므로, 아래와 같이 삭제하여 삽입 가능
insert into students(Name, MajorCode) values("홍길동", 'CHE');

insert into students values(5, "홍길똥", 32, 'EE');

insert into students(Name, Age, MajorCode) values("Amy", 27, 'CS');
insert into students(Name, Age, MajorCode) values("Jason", 22, 'CS');
insert into students(Name, Age, MajorCode) values("Bill", 20, 'EE');

# Name의 default값이 ''이므로 명시하지 않아도 가능
insert into students(MajorCode) values('EE');

# 조건에 부합하는 row의 field 업데이트
update students set Name = 'Tim' where Name = '';

# 조건에 부합하는 row 삭제
delete from students where Name = 'Tim';

# index 생성
create index students_name_idx ON students (Name);

# 이제 인덱스가 생성되었으므로 검색이 더 빨라짐
select * from students
	where Name = '홍길동';
    
# 아래 쿼리에는 인덱스가 영향을 미치지 않음
select * from students
	where Name = '홍길동'
    and MajorCode = 'CHE';
    
# 두개의 필드에 모두 인덱스를 걸어줘야 함.
create index students_name_major_idx ON students (Name, MajorCode);

select * from students
	where Name = '홍길동'
    and MajorCode = 'CHE';
    
    
# MajorCode 기준으로 내림차순 정렬
select * from students
	order by MajorCode DESC;
    
# MajorCode 오름차순, Name 내림차순 정렬
select * from students
	order by MajorCode, Name DESC;
    

# 전체 row의 개수를 알 수 있다.
select count(*)
	from students;
    
# 특정 조건 row의 개수를 알 수 있다.
select count(*)
	from students
    where MajorCode = 'CS';
    
# 정수형의 경우 데이터 합, 평균등의 계산이 가능하다.
#select sum(*)
#	from students;
    
select sum(Age)
	from students;
    
select avg(Age)
	from students;
    
# 각 필드에 산술 연산이 가능함.
select sum(Age) / 2 
	from students;
    
select Age, Age/2.5 
	from students;
    
    
# between 연산자 사용 가능
select * 
	from students 
    where Age between 20 and 30;
    
# NULL 비교
select * 
	from students 
    where Name = NULL; # (X)
    
select * 
	from students 
    where Name is NULL; # (O)
    
    
# 지정한 열에서 중복을 제거하여 데이터를 가져옴
select distinct MajorCode 
	from students;
    

# 집합 함수
# sum, avg, count, max, min
select max(Age), min(Age)
	from students;
    

# group by
# 특정 필드를 기준으로 데이터를 그룹화 시킴
select * 
	from students
    group by MajorCode;

# 주로 집합 함수와 함께 사용됨. 그룹별 집계가 가능
select MajorCode, max(Age), min(Age), avg(Age) 
	from students
    group by MajorCode;
    
# 그룹화 후 집합 함수를 조건으로 걸고 싶다면 where 사용이 불가능
select MajorCode, max(Age), min(Age), avg(Age) 
	from students
    group by MajorCode
    where avg(Age) <= 27; #(X)
    
select MajorCode, max(Age), min(Age), avg(Age) 
	from students
    where MajorCode = 'CS'
    group by MajorCode;    
    
select MajorCode, max(Age), min(Age), avg(Age) 
	from students
    group by MajorCode 
    having MajorCode = 'CS';
    
    
select MajorCode, max(Age), min(Age), avg(Age) 
	from students
    group by MajorCode
    having avg(Age) <= 27;
    
# subquery
select * 
	from students
where Age > 
(select avg(Age)
	from students);
    
select min(Age) 
	from (select *
		from students where Age > 26) as t;
            
            
select * from students;
# major table 생성
# ID, Code, Name, Description

insert into majors(Code, Name, Description) values('CS', 'Computer Science', 'CSCSCSCS');
insert into majors(Code, Name, Description) values('BIO', 'Biology', 'Biology hahaha');
#insert into majors(Code, Name, Description) values('PHIL', 'Philosophy', 'Good');
insert into majors(Code, Name, Description) values('CHE', 'Chemistry', 'Better');
insert into majors(Code, Name, Description) values('EE', 'Electrical Engineering', 'Best');
insert into majors(Code, Name, Description) values('ECO', 'Economics', 'Even Better');



select * from students;
select * from majors;

# 교차 조인
# 존재하는 모든 행에 대해 조인 함
select *
	from students s 
    cross join majors m;
    
# 혹은 아래와 같이 표현 가능
select *
	from students s, majors m;


# 내부조인 (inner join)
# 지정한 열의 값이 일치하는 행만 가져옴
select *
	from students s
    inner join majors m
    on s.MajorCode = m.Code;
    
select *
	from students s
	join majors m
    on s.MajorCode = m.Code;


# 외부조인 
# 내부조인과 달리 일치하지 않는 데이터도 가져오게 됨.

# 왼쪽 외부 조인 (left outer join or left join)
select *
	from students s
    left outer join majors m
    on s.MajorCode = m.Code;
    
select *
	from students s
    left join majors m
    on s.MajorCode = m.Code;
    
# 오른쪽 외부 조인 (right outer join or right join)
select *
	from students s
    right outer join majors m
    on s.MajorCode = m.Code;
    
select *
	from students s
    right join majors m
    on s.MajorCode = m.Code;
    

# 전체 외부 조인 (Mysql 지원하지 않음)
#select *
#	from students s
#    full outer join majors m
#    on s.MajorCode = m.Code;

# 굳이 결과를 받고 싶으면 아래와 같이 함.
select *
	from students s
    right join majors m
    on s.MajorCode = m.Code
	union    
select *
	from students s
    left join majors m
    on s.MajorCode = m.Code;
    

# 연습문제) courses 테이블과  scores 테이블을 만들고 적당한 데이터를 채우시오.

# course table 생성
# ID, Code, Name

# score table 생성
# ID, StudentID, CourseCode, Score 


# 연습문제)
# 1. 학생별 평균 점수를 구하시오
# 2. 전공별 평균 점수를 구하시오.
# 3. 가장 많은 코스를 듣는 학생과 가장 적은 코스를 듣는 학생은?
# 4. 전체 평균보다 낮은 점수를 기록한 학생의 이름과 나이를 출력하세요.



# 연습문제 )
# 1. 회원가입이 필요한 쇼핑몰 사이트에 필요한 테이블을 설계해보세요.
# 1.1 회원 테이블, 주문 테이블, 상품 테이블


# 테이블 버림
drop table students;
