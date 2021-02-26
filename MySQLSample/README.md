# MySQLSample
You can refer to it to use MySQL on the server we prepared.

***show_databases.py*** is a simple program that connects to mysql and executes sql "show databases" to list the databases.

For other CRUD runs, please check them out on your own.


## Dependencies 
```
mysql-connector-python==8.0.23
```
On the server we prepared, you can already use this mysql-connector-python.

So, there is no need to ***pip install mysql-connector-python***.

If you want to use a python mysql library other than mysql-connector-python, please let the TA know.


## Execution
First, you need to change the following few places in the program.
```
user='', # Usernames of the MySQL user on your team
password='', # Password of the MySQL user on your team
database='' # Name of the database you are using.
```

As in all other cases, please use ***python3*** command instead of ***python*** command on the server we prepared.
```
python3 show_databases.py
```
