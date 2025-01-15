import sqlite3

db = sqlite3.connect('db/Car.db')

if __name__ == "__main__":
  db.execute('''
CREATE TABLE "users" (
	"id_users"	INTEGER,
	"login"	TEXT NOT NULL UNIQUE,
	"password"	TEXT NOT NULL,
	"dol"	INTEGER, 
	PRIMARY KEY("id_users"),
	FOREIGN KEY("dol") REFERENCES "dol"("id")
); 
''')  
  
  
  db.execute('''
   CREATE TABLE "dol" (
	"id"	INTEGER,
	"dol"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);        
''')