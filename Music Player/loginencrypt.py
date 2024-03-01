import sqlite3 #creating databse to store passwords
import hashlib #library downloaded so as not to show the passwords in clear text when stored in database

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABL IF NOT EXISTS userdata (
            id INTEGER PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            
)


""")


