show databases;
use universal_data;
select * from customers_10000;
select * from customers_10000 order by Company desc;
select * from customers_10000 order by Subscription_Date;
select * from customers_10000 order by City asc;

update customers_10000 
set First_Name = 'yash', City = 'bhopal'
where Customer_Id ='EB54EF1154C3A78';