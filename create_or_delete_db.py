# This is to create or destroy each of the instances of the 
import sqlite3
from datetime import datetime

conn = sqlite3.connect("country_news.db")

c = conn.cursor()


# Only ran this once

"""
c.execute("""
#CREATE TABLE country (
    #iso TEXT PRIMARY KEY,
    #today_date TEXT NOT NULL,
    #news TEXT
#)
""")

conn.commit()
conn.close()
"""

