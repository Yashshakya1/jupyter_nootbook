CREATE database SHOPDB;
USE SHOPDB;

create table customers(
CustomersID int auto_increment primary key,
name varchar(100),
email varchar(100) unique,
address varchar(200)  
);

select * from customers;

INSERT INTO customers(name,email,address)
VALUES('YASH','YASHSHAKYA787@GMAIL.COM','MANGALWARA GAIN MANDIR ROAD HOUSE NO 13 GALI NO 1'),
('HARSH','YASHSHAKYA40613@GMAIL.COM','MANGALWARA'),
('PINLKY','YASHSHAKYA787@GMAIL.COM','MANGALWARA GAIN MANDIR ROAD HOUSE NO 13 GALI NO 1');
select NAME FROM CUSTOMERS;
select distinct name,address FROM CUSTOMERS;

