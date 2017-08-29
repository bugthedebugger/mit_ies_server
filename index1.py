#!/usr/bin/python3

# Turn on debug mode.
import cgitb
cgitb.enable()

# Print necessary headers.
print("Content-Type: text/html")
print()

# Connect to the database.
import pymysql
conn = pymysql.connect(
    db='iot',
    user='root',
    passwd='iot@karkhana',
    host='localhost')
c = conn.cursor()

# Insert some example data.
c.execute("INSERT INTO imu(steps, total) VALUES (1, 1)")
c.execute("INSERT INTO imu(steps, total) VALUES (2, 2)")
c.execute("INSERT INTO imu(steps, total) VALUES (3, 3)")
conn.commit()

# Print the contents of the database.
c.execute("SELECT * FROM imu")
print([(r[0], r[1]) for r in c.fetchall()])

