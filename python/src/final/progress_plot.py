import sqlite3

# Connect to the database
conn = sqlite3.connect('../database/planner.db')
cur = conn.cursor()



# Close the database connection
conn.close()
