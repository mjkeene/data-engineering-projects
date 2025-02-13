-- Create a new virtual warehouse, and two new databases, raw and analytics.
create warehouse transforming;
create database raw;
create database analytics;
create schema raw.jaffle_shop;
create schema raw.stripe;

-- Create customers table in raw database and jaffle_shop schema
create table raw.jaffle_shop.customers
(
  id integer,
  first_name varchar,
  last_name varchar
);

-- Load data into the customers table
copy into raw.jaffle_shop.customers (id, first_name, last_name)
from 's3://dbt-tutorial-public/jaffle_shop_customers.csv'
file_format = (
    type = 'CSV'
    field_delimiter = ','
    skip_header = 1
);

-- Create orders table in jaffle_shop schema
create table raw.jaffle_shop.orders
(
  id integer,
  user_id integer,
  order_date date,
  status varchar,
  _etl_loaded_at timestamp default current_timestamp
);

-- Load data into orders table
copy into raw.jaffle_shop.orders (id, user_id, order_date, status)
from 's3://dbt-tutorial-public/jaffle_shop_orders.csv'
file_format = (
    type = 'CSV'
    field_delimiter = ','
    skip_header = 1
);

-- Create payment table, this time in stripe schema
create table raw.stripe.payment
(
  id integer,
  orderid integer,
  paymentmethod varchar,
  status varchar,
  amount integer,
  created date,
  _batched_at timestamp default current_timestamp
);

-- Load the payments table
copy into raw.stripe.payment (id, orderid, paymentmethod, status, amount, created)
from 's3://dbt-tutorial-public/stripe_payments.csv'
file_format = (
    type = 'CSV'
    field_delimiter = ','
    skip_header = 1
);

-- Verify that each of these has output
select * from raw.jaffle_shop.customers limit 20;
select * from raw.jaffle_shop.orders limit 20;
select * from raw.stripe.payment limit 20;
