use test;

CREATE TABLE news (
   link varchar(200) NOT NULL, 
   title VARCHAR(100) NOT NULL, 
   content  TEXT not null,
   crawl_time DATETIME not null, 
   PRIMARY KEY (link)
) DEFAULT CHARSET=utf8;


SELECT 
    * FROM news;
    
delete from news;



