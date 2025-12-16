create database if not exists friends;
use friends;
select database();
create table friendinfo(
numbersf int auto_increment primary key,
name varchar(50),
number varchar(100),
bound tinyint(100),
location varchar(50)
);
select * from friendinfo;

insert into friendinfo(name,number,bound,location)
values('Tushar',4815645891,95,'bhopal'),
('rani',1245878956,100,'betul'),
('suraj',1245878949,95,'jharkhand');
alter table friendinfo modify number varchar(100);
alter table friendinfo add column socialmedia varchar(100);
alter table friendinfo rename column location to loc;