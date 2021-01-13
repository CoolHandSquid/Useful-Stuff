#!/usr/bin/python3
import sqlite3

conn    = sqlite3.connect("TireFire.db")
c       = conn.cursor()

#Create Table
#c.execute("""CREATE TABLE Main (
#            Name text,
#            Port text,
#            Description text
#    )""")
#c.execute
###Datatypes: NULL, INTEGER, REAL, TEXT, BLOB

#Add A Record
#c.execute("""INSERT INTO Main VALUES ('FTP', '21', 'File Transfer Protocol')""")

#Add Many Records At Once
#protocols   = [
#        ('SMTP', '25', 'Simple Mail Transfer Protocol'),
#        ('DNS', '53', 'Domain Name Service'),
#        ('Kerberos', '88', 'AD Domain Authentication Service')
#        ]
#c.executemany("""INSERT INTO Main VALUES (?,?,?)""", protocols)

#Query The Database
#c.execute("SELECT * FROM Main")
#c.fetchone()#Fetch the first item in table
#c.fetchmany(3)#Fetch first 3 items in table
#c.fetchall()#Fetch all items in table
#print(c.fetchall())#You can call individual parts of the tuple with [2]

#Cool Query Things
#c.execute("SELECT rowid, * FROM Main")#Prints the row id as the first collum (starting at 1)
#c.execute("SELECT * FROM Main WHERE Name = 'DNS'")#Duh
#c.execute("SELECT * FROM Main")#< > <= >= = Work for INTEGER and REAL
#c.execute("SELECT * FROM Main WHERE Description LIKE '%Domain%'")#LIKE with % can be used similar to a regex *
#items   = c.fetchall()
#for item in items:
#    print(item)

#Update Records
#c.execute("""UPDATE Main SET Port = '21' WHERE NAME = 'FTP'""")
#c.execute("""UPDATE Main SET Port = '22' WHERE rowid = 1""")
#c.execute("""SELECT * FROM Main""")
#print(c.fetchall())

#Delete Records
#c.execute("""DELETE FROM Main WHERE rowid = 1""")
#c.execute("SELECT * FROM Main")
#print(c.fetchall())

#Query The DB - ORDER BY
#c.execute("""SELECT rowid, * FROM Main ORDER BY Port DESC""")
#ASC    = Ascending
#DESC   = Descending
#for i in c.fetchall():
#    print(i)

#Query The Db - AND/OR
#c.execute("Select rowid, * FROM Main WHERE Name LIKE 'Kerb%' OR Port = '21'")
#for i in c.fetchall():
#    print(i)

#Query The DB - LIMIT
#c.execute("Select rowid, * FROM Main Limit 3")
#for i in c.fetchall():
#    print(i)

#DROP (Delete) A Table
#c.execute("DROP TABLE Main")



conn.commit()
conn.close()
