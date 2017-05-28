import sqlite3

DB_NAME = "Treasy_DB"

SQL_File_Name = "new_creabase.sql"

creabase = ""
with open(SQL_File_Name, 'r') as creaFile:
	creabase=creaFile.read().replace('\n',' ')

conn = sqlite3.connect(DB_NAME)
curs = conn.cursor()

sqlite3.complete_statement(creabase)
curs.executescript(creabase)

curs.close()
conn.close()