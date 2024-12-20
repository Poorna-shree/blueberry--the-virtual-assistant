"""
Module to manage database commands for a Jarvis-like application.
This script creates tables for system and web commands and adds sample data.
"""

import sqlite3

# Connect to SQLite database
con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

# Create the sys_command table if it doesn't exist
SQL_QUERY_SYS_COMMAND = """
CREATE TABLE IF NOT EXISTS sys_command (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    path VARCHAR(1000)
)
"""
cursor.execute(SQL_QUERY_SYS_COMMAND)

# Uncomment below to add sample data for sys_command
#INSERT_SYS_COMMAND = """
#INSERT INTO sys_command (name, path)
#VALUES ('telegram', 'C:\\Users\\CHINNU\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe')
#"""
#cursor.execute(INSERT_SYS_COMMAND)

# Commit changes after inserting data
#con.commit()

# Create the web_command table if it doesn't exist
SQL_QUERY_WEB_COMMAND = """
CREATE TABLE IF NOT EXISTS web_command (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    url VARCHAR(1000)
)
"""
cursor.execute(SQL_QUERY_WEB_COMMAND)

# Uncomment below to add sample data for web_command
INSERT_WEB_COMMAND = """
    INSERT INTO web_command (name, url)
    VALUES ('google', 'https://www.google.com/')
    """
cursor.execute(INSERT_WEB_COMMAND)

#Commit changes and close the connection
con.commit()
con.close()
