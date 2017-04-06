# create ratings
CREATE TABLE `ratings` (
  `user_id` int(11) NOT NULL,
  `movie_id` int(11) NOT NULL,
  `rating` double NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

# add composite primary key
alter table ratings add constraint pk_rating primary key (user_id, movie_id);

# 혹은 이렇게 primary key 지정 가능
CREATE TABLE `ratings` (
  `user_id` int(11) NOT NULL,
  `movie_id` int(11) NOT NULL,
  `rating` double NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  constraint pk_rating primary key (user_id, movie_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

# create movies
CREATE TABLE `movies` (
  `movie_id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `genre` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`movie_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

# 혹은 이렇게 primary key 지정 가능
CREATE TABLE `ratings_train` (
  `user_id` int(11) NOT NULL,
  `movie_id` int(11) NOT NULL,
  `rating` double NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  constraint pk_rating primary key (user_id, movie_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `ratings_test` (
  `user_id` int(11) NOT NULL,
  `movie_id` int(11) NOT NULL,
  `rating` double NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  constraint pk_rating primary key (user_id, movie_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

# ratings.csv load
load data local infile '/Users/aaronbyun/Desktop/dss4/day 20 recommendation/ml-latest-small/ratings.csv'
	into table ratings
    columns terminated by ','
    lines terminated by '\n'
    ignore 1 lines 
    (user_id, movie_id, rating, @var1) set timestamp = FROM_UNIXTIME(@var1);
    
# movies.csv load
load data local infile '/Users/aaronbyun/Desktop/dss/week9/ml-latest-small/movies.csv'
	into table movies
    columns terminated by ','
    lines terminated by '\n'
    ignore 1 lines;
    
    
load data local infile '/Users/aaronbyun/Desktop/dss/week10/ml-100k/ua.base'
	into table ratings_train
    columns terminated by '\t'
    lines terminated by '\n'
    ignore 1 lines 
    (user_id, movie_id, rating, @var1) set timestamp = FROM_UNIXTIME(@var1);
    

load data local infile '/Users/aaronbyun/Desktop/dss/week10/ml-100k/ua.test'
	into table ratings_test
    columns terminated by '\t'
    lines terminated by '\n'
    ignore 1 lines 
    (user_id, movie_id, rating, @var1) set timestamp = FROM_UNIXTIME(@var1);

# similarity    
CREATE TABLE `similarity` (
  `user_id1` int(11) NOT NULL,
  `user_id2` int(11) NOT NULL,
  `similarity` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

# add composite primary key
alter table similarity add constraint pk_similarity primary key (user_id1, user_id2);
    
select * from ratings;
select * from movies;
select * from similarity;



select * from salary;

# max salary
select max(salary) from salary;

# 2nd max salary
select max(salary)	
	from salary 
    where salary not in (select max(salary) from salary);

# 2nd max salary
SELECT *
FROM salary Emp1
WHERE (1) = (
SELECT COUNT(DISTINCT(Emp2.salary))
FROM salary Emp2
WHERE Emp2.salary > Emp1.salary);










select * 
	from salary s1
    where 2 = (select count(distinct(s2.salary))
						from salary s2
                        where s2.salary > s1.salary);



select *
	from salary
    order by salary desc
    limit 2, 1;
    
    
    











select * 
	from students s1
    where 1 = (select count(distinct(score)) from students s2
				where s2.score > s1.score)











