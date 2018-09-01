# Dbpy1.0-man Program 
Dbpy is a simple program to management database for server. This program is created because the experience of setting up the database on the server cli is very boring and includes one by one if you want to manage it.
 
The features of this Dbpy program are :
1. Show Database
2. Show Table
3. Create Database
4. Create Table
5. Delete Database
6. Dalete Tables

The packages needed to run this program are:
1. Mysql-server
2. Python
3. PIP / Python-pip (to install mysql-connector)
4. Mysql-connector (to Connect Mysql with Python)

How to use Dbpy on the server:
1. Clone or Download ZIP all files in this repository.
2. If Download ZIP then extract unzip dbpy1.0-man-master.zip.
3. Sqlpy1.0-master / cd.
4. chmod + x install.sh.
To change permissions so that the terminal can be executed.
5. run ./install.sh (This is used to install the required package except mysql-server, the database can use mysql-server or mariadb-server).
6. If the installation is successfull, then Sqlpy can be run.
7. run python dbpy1.0-man.py to start Dbpy-man.

The menu in Sqlpy:
1. Show Databases (to display all databases in mysql-server).
2. Show Tables (to display all tables in the database that are being used).
3. Create Database (to create a new database).
4. Create Table (to create a new table).
5. Login Database more (to change which database is used now).
6. Delete Database (to delete the database).
7. Delete Table (to delete the selected table in the database currently in use).
8. Exit. (for exit sqlpy)

NB: To develop Sqlpy can give suggestions and criticisms for me. Sqlpy includes an open source program that you can modify to suit your needs.
