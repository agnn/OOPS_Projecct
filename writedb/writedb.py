import mysql.connector as conn
from logging_class import  lg

mydb = conn.connect(host = "localhost", user = "root", passwd = "Failsafeauto#1")

cursor = mydb.cursor()


def create_table():
    'function to created a new named table , just for project purpose'
    try:
        s="create table oopsprojectdb.student_records(userid varchar(80),name varchar(80),date_of_birth varchar(80),gender varchar(80), contact_number varchar(30), email_id varchar(30), course_enrolled int(30), internship int(30))"
        cursor.execute(s)
        lg.info("table created")
    except Exception as e:
        lg.info(e)

try:
    cursor.execute("show databases")
    existingdb = (cursor.fetchall())
    #print(existingdb)

    check = False
    for i in existingdb:
        if i == ('oopsprojectdb',):
            lg.info("Database already exist")
            check = True
            break
    if check == False :
        cursor.execute("create database oopsprojectdb")
        lg.info("Database created")

except Exception as e:

    lg.error(e)


def insert_values(*values):
    'function to enter student record in to database'

    l=list(values)
    lg.info(l)
    try:
        s = f"insert into oopsprojectdb.student_records values('{l[0]}','{l[1]}','{l[2]}','{l[3]}',{l[4]},'{l[5]}',{l[6]},{l[7]})"
        lg.info(f"record entered successfully {l[0]},'{l[1]}','{l[2]}','{l[3]}',{l[4]},'{l[5]}',{l[6]},{l[7]}")
        cursor.execute(s)
        mydb.commit()

    except Exception as e:

        lg.error(e)

#create_table()