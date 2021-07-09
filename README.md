# Billing_System
A simple billing system with tkinter and mysql to dispaly item info and/or purchase  it.

Make sure a database and table exist

A mysql commandline is available when 'fetcher.py' is run with 'mysqlcmd.py' in the same directory.

SQL COMMANDS:

1.CREATE DATABASE my_data;
2.USE my_data;
3.CREATE TABLE PRODUCT_INFO(Item_name VARCHAR(20),Item_id int PRIMARY KEY, Cost int,Rating_5 DECIMAL(2,1));
4.INSERT INTO PRODUCT_INFO VALUES('Pilot',1,70,4.5); and more items of your choice.
