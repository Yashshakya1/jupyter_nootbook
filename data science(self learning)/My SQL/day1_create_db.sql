create database if not exists MacbookM4;
use MacbookM4;
select database();

create table product_Details(
ProductId Int auto_increment primary key,
Name varchar(100),
VARIANT int,
colour text(50)
);

select * from product_Details;

insert into product_Details(Name,VARIANT,colour)
values('macbookm4 air',512,'sky blue');

alter table product_Details add column appleCare varchar(100);
alter table product_Details modify colour tinytext;
alter table product_Details rename column colour to color;





