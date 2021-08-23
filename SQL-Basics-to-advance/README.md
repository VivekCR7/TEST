
# SQL scratch to advance

This Article will give all you wanted to know about databases and how to write queries
we are going to see simple queries to some advance and complext queries. Now the main agenda
of this Article is to make you comfortable in writing complex queries. In the end there will
be some resources and pratice set where you can practice queries.

before moving to the queries, we need to see some basic terminologies.

<br>

## What is Database?

The **database** is an organized collection of structured data to make it easily accessible,
manageable and update. In simple words, you can say, a database in a place where the data
is stored.
You can take library as an example where, library is the **database** and the books are the data.
Books of different genere which are organized and stored in there respective section is what database
is organizing and storing of data.

<br>

## What is Database Management System (DBMS)?

A Database Management System (DBMS) is a software that is used to manage the Database.
A DBMS basically serves as an interface between the database and its end-users or programs,
allowing users to retrieve, update, and manage how the information is organized and optimized.
A DBMS also facilitates oversight and control of databases, enabling a variety of administrative
operations such as performance monitoring, tuning, and backup and recovery.

<br>

## What is structured query language (SQL) ?

Structured Query language SQL is pronounced as “S-Q-L” or sometimes as “See-Quel”  which is the standard language for dealing with Relational Databases.

It is effectively used to insert, search, update, delete, modify database records. It doesn’t mean SQL cannot do things beyond that. 
In fact, it can do a lot more other things as well. SQL is regularly used not only by database administrators but also by the developers
to write data integration scripts and data analysts. 

Now that you guys have understood what SQL is. We can start working on Queries.

I am going to use postgresSQL, hope you have installed it. If not, setup postgreSQL using
below links.

* [Setup postgres on mac](https://www.sqlshack.com/setting-up-a-postgresql-database-on-mac/)
* [Setup postgres on linux](https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart)

<br>

#s Dataset

We are going to use the dataset from pgexercises. It's a perfect dataset for practicing
simple queries to complex queries.

* [Download dataset]

start the psql server

```bash
~ psql
```
create database named exercises where we are going to load our dataset

```
your_name=# create database exercises;
your_name=# \q
```

```bash
~ psql exercises < "path-to-your-downloaded-data"
```

Dataset is loaded and ready to work on.

<br>

# Queries

Now, If you are reading this, means you have setup the postgresSQL
and also loaded the .sql data in your system.

We are going to use terminal for writing Queries.

open psql server in terminal

```bash
~ psql
```

list the databases

```sql
your_name=# \l
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges
-----------+----------+----------+-------------+-------------+--------
 exercises | your_name | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
```

you can see, exercises database is there we just have to switch to that database then we can
access the tables.

switch databases

```sql
\c exercises
exercises=# \dn

  List of schemas
  Name  |  Owner
--------+----------
 cd     | your_name
 public | postgres
```

now here cd is a schema, and below image shows the structure of the table and there relations.

![](dataset/Screenshot%202021-08-23%20at%209.28.00%20PM.png)


Now, we can practice some of the basic Queries

<br>


### SELECT statement

The SELECT statement is used to select data from a database.

* select particular column

```sql
> select telephone from cd.members
  limit 10;

    telephone
----------------
  (000) 000-0000
  555-555-5555
  555-555-5555
  (844) 693-0723
  (833) 942-4710
  (844) 078-4130
  (822) 354-9973
  (833) 776-4001
  (811) 433-2547
  (833) 160-3900
(10 rows)

```

here, **SELECT** statement is used to retrieve the particular data or column
from a table. above statement also has **LIMIT** which specifies the number of 
rows to be shown, it is used when there is large dataset


* select multiple column

```sql
> select firstname, surname from cd.members
  limit 10;

  firstname | surname
  -----------+----------
  GUEST     | GUEST
  Darren    | Smith
  Tracy     | Smith
  Tim       | Rownam
  Janice    | Joplette
  Gerald    | Butters
  Burton    | Tracy
  Nancy     | Dare
  Tim       | Boothe
  Ponder    | Stibbons
(10 rows)

```

we can use specify multiple column sperated by '**,**' for selecting multiple column.

* select all columns

```sql
> select * from cd.bookings
  limit 10;

   bookid | facid | memid |      starttime      | slots
--------+-------+-------+---------------------+-------
      0 |     3 |     1 | 2012-07-03 11:00:00 |     2
      1 |     4 |     1 | 2012-07-03 08:00:00 |     2
      2 |     6 |     0 | 2012-07-03 18:00:00 |     2
      3 |     7 |     1 | 2012-07-03 19:00:00 |     2
      4 |     8 |     1 | 2012-07-03 10:00:00 |     1
      5 |     8 |     1 | 2012-07-03 15:00:00 |     1
      6 |     0 |     2 | 2012-07-04 09:00:00 |     3
      7 |     0 |     2 | 2012-07-04 15:00:00 |     3
      8 |     4 |     3 | 2012-07-04 13:30:00 |     2
      9 |     4 |     0 | 2012-07-04 15:00:00 |     2
(10 rows)
```

we can use "*" for selecting all the data from a particular table

<br>

### WHERE clause

**WHERE** clause is applied to each row of data by checking
specific column values to determine whether it should be
included in the results or not.

* example of where clause

```sql
> select * from cd.facilities
  where monthlymaintenance < 50;

  facid |     name      | membercost | guestcost | initialoutlay | monthlymaintenance
  -------+---------------+------------+-----------+---------------+--------------------
      3 | Table Tennis  |          0 |         5 |           320 |                 10
      7 | Snooker Table |          0 |         5 |           450 |                 15
      8 | Pool Table    |          0 |         5 |           400 |                 15
```

as you can see all the entries with monthlymaintenance less than 50 is retrieved


* we can use logic operators like **AND** and **OR** for multiple conditions

```sql
> select * from cd.facilities
  where membercost > 0 and
  initialoutlay > 1000;

 facid |      name      | membercost | guestcost | initialoutlay | monthlymaintenance
-------+----------------+------------+-----------+---------------+--------------------
     0 | Tennis Court 1 |          5 |        25 |         10000 |                200
     1 | Tennis Court 2 |          5 |        25 |          8000 |                200
     4 | Massage Room 1 |         35 |        80 |          4000 |               3000
     5 | Massage Room 2 |         35 |        80 |          4000 |               3000
     6 | Squash Court   |        3.5 |      17.5 |          5000 |                 80
```

<br>

### BETWEEN / NOT BETWEEN

As name defines it is widely used for extracting data in range.

```sql
> select * from cd.bookings
  where bookid between 3 and 5;

  bookid | facid | memid |      starttime      | slots
--------+-------+-------+---------------------+-------
      3 |     7 |     1 | 2012-07-03 19:00:00 |     2
      4 |     8 |     1 | 2012-07-03 10:00:00 |     1
      5 |     8 |     1 | 2012-07-03 15:00:00 |     1
```

here we get the column from range 3 and 5 of bookid. Similarly we can use not between

```sql
> select * from cd.bookings
  where bookid not between 3 and 5;
  limit 10;


   bookid | facid | memid |      starttime      | slots
--------+-------+-------+---------------------+-------
      0 |     3 |     1 | 2012-07-03 11:00:00 |     2
      1 |     4 |     1 | 2012-07-03 08:00:00 |     2
      2 |     6 |     0 | 2012-07-03 18:00:00 |     2
      6 |     0 |     2 | 2012-07-04 09:00:00 |     3
      7 |     0 |     2 | 2012-07-04 15:00:00 |     3
      8 |     4 |     3 | 2012-07-04 13:30:00 |     2
      9 |     4 |     0 | 2012-07-04 15:00:00 |     2
     10 |     4 |     0 | 2012-07-04 17:30:00 |     2
     11 |     6 |     0 | 2012-07-04 12:30:00 |     2
     12 |     6 |     0 | 2012-07-04 14:00:00 |     2
```
<br>

### IN/ NOT IN

As named, it is used to get data if it is present in some list or according the user conditions

```sql
> select * from cd.bookings
  where bookid in (1,2,15,5);

   bookid | facid | memid |      starttime      | slots
--------+-------+-------+---------------------+-------
      1 |     4 |     1 | 2012-07-03 08:00:00 |     2
      2 |     6 |     0 | 2012-07-03 18:00:00 |     2
      5 |     8 |     1 | 2012-07-03 15:00:00 |     1
```

the above Query listed all the entries if the book id is in that list.

Similarly we can do it for NOT IN.

```sql
> select * from cd.bookings
  where bookid not in (1,2,15,5,7,9,10)
  limit 10;

   bookid | facid | memid |      starttime      | slots
--------+-------+-------+---------------------+-------
      0 |     3 |     1 | 2012-07-03 11:00:00 |     2
      3 |     7 |     1 | 2012-07-03 19:00:00 |     2
      4 |     8 |     1 | 2012-07-03 10:00:00 |     1
      6 |     0 |     2 | 2012-07-04 09:00:00 |     3
      8 |     4 |     3 | 2012-07-04 13:30:00 |     2
     11 |     6 |     0 | 2012-07-04 12:30:00 |     2
     12 |     6 |     0 | 2012-07-04 14:00:00 |     2
     13 |     6 |     1 | 2012-07-04 15:30:00 |     2
     14 |     7 |     2 | 2012-07-04 14:00:00 |     2
     16 |     8 |     3 | 2012-07-04 18:00:00 |     1

```

<br>

### LIKE operator

**LIKE** operator is used to perform conditions on the strings. "%" operators is for multiple
and " _ " operators is for one.

```sql
> select firstname from cd.members
  where firstname like 'T%';

   firstname
  -----------
    Tracy
    Tim
    Tim
    Timothy
```

Here, in above example I received the firstname which starts from "T", "%% operator is used so that multiple character
can come after "T". this we can perform operations on strings

<br>

### Sorting (order by)

**ORDER BY** is used to order the column in ascending or descending, by default it's ascending or you can use
'asc' or 'desc' for ascending and descending similarly.

```sql
> select firstname, surname from cd.members
  order by firstname desc
  limit 10;

   firstname | surname
  -----------+----------
    Tracy     | Smith
    Timothy   | Baker
    Tim       | Boothe
    Tim       | Rownam
    Ramnaresh | Sarwin
    Ponder    | Stibbons
    Nancy     | Dare
    Millicent | Purview
    Matthew   | Genting
    John      | Hunt
```

here the name has been sorted descending and top 10 entries are retrived using "LIMIT" keyword

we can also use "OFFSET" keyword to get the limited data

* get the data of id from 3 to 5 using offset

```sql
> select memid,firstname, surname from cd.members
  limit 3 offset 3;

   memid | firstname | surname
-------+-----------+----------
     3 | Tim       | Rownam
     4 | Janice    | Joplette
     5 | Gerald    | Butters
```

offset allows to start from that number and limit helps to get the particular number of rows.

<br>

### JOINS

A **JOIN** clause is used to combine rows from two or more tables, based on a related column between them.

* Inner JOIN

  Inner join helps to combine the 2 tables. it will return if there is a proper match.
  it won't return column with null values
  by defaul **JOIN** clause is Inner join

```sql
> select bks.facid, fac.name, bks.slots from cd.bookings bks 
  join cd.facilities fac on bks.facid = fac.facid
  limit 10;

  facid |      name      | slots
-------+----------------+-------
    0 | Tennis Court 1 |     3
    0 | Tennis Court 1 |     3
    0 | Tennis Court 1 |     3
    0 | Tennis Court 1 |     3
    0 | Tennis Court 1 |     3
    0 | Tennis Court 1 |     3
    0 | Tennis Court 1 |     3
    0 | Tennis Court 1 |     3
    0 | Tennis Court 1 |     3
    0 | Tennis Court 1 |     3

```

In above example, 'bks' and 'fac' is the alias given to the table so that it gets
easy to recognize which table's column we are trying to access and we inner join the 
two tables on the facid.

* LEFT JOIN

  left join is used to get all the data from left table even if there isn't a match with 
  right table. if there is a match then it's ok or else the cell is shown NULL.

* RIGHT JOIN

  right join is used to get all the data from the right table even if there isn't a match
  with the left table.

* FULL JOIN

  full join gets all the data matched as well as unmatched. also known as Outer Join


unfortunately, we don't have such conditions to show that in practical but below is the link you can visualize
that how joins work in SQL.

[Learn JOINS from here](https://joins.spathon.com/)

<br>

### Expressions

We can use expression like multiplication and calculations while select the column and renamed
it and create another column

```sql
> select name, membercost+guestcost as total_cost from cd.facilities
  limit 10;

        name       | total_cost
  -----------------+------------
    Tennis Court 1  |         30
    Tennis Court 2  |         30
    Badminton Court |       15.5
    Table Tennis    |          5
    Massage Room 1  |        115
    Massage Room 2  |        115
    Squash Court    |       21.0
    Snooker Table   |          5
    Pool Table      |          5
```

so, in above example we add the membercost and guestcost and created new column as total_cost using "AS" for naming
and limit the first 10 entries.
this is how we can perform multiple expressions and output the data.

<br>

### Aggregations

In addition to the simple expressions, SQL also supports the use of
aggregate expressions (or functions) that allow you to summarize information
about a group of rows of data.

some common aggregate functions are, Count, Sum, Min, Max which makes our work
fast and effective.

```sql
> select count(*) from cd.facilities;

   count
  -------
      9
(1 row)
```

above example shows, how many facilities exist - simply produce a total count.


```sql
> select facid, sum(slots) as "Total Slots"
	from cd.bookings
	where
		starttime >= '2012-09-01'
		and starttime < '2012-10-01'
	group by facid
  order by sum(slots);  


   facid | Total Slots
  -------+-------------
      5 |         122
      3 |         422
      7 |         426
      8 |         471
      6 |         540
      2 |         570
      1 |         588
      0 |         591
      4 |         648  
```

above example, gives the total number of slots booked per facility in the
month of september 2012 and sorted by the number of slots.

<br>

## Author

[@Vivek Dubey](https://www.linkedin.com/in/vivek-dubey-cr7/)



