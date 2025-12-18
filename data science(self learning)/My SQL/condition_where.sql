create database universal_data;
use universal_data;
select * from 100_friends_dataset;
select * from 100_friends_dataset where name like '%5'; 
select * from 100_friends_dataset where name like '_l%';
select * from 100_friends_dataset where name like '%5';
select * from 100_friends_dataset where name = 'friend_18' and location like'%city_9%';