import sqlite3

db = sqlite3.connect('db/Car.db')
cursor = db.cursor()


if __name__ == "__main__":
	db.execute('''
CREATE TABLE "users" (
	"id_users"	INTEGER,
	"login"	TEXT NOT NULL UNIQUE,
	"password"	TEXT NOT NULL,
	"dol" TEXT,
	"orders" INTEGER, 
	PRIMARY KEY("id_users"),
	FOREIGN KEY("orders") REFERENCES "orders"("id_orders")
	FOREIGN KEY("dol") REFERENCES "dol"("id_dol")
); 
''')  
	db.execute('''
   	CREATE TABLE "dol" (
	"id_dol"	INTEGER,
	"dol"	TEXT NOT NULL,
	PRIMARY KEY("id_dol" AUTOINCREMENT)
);  
''')
	db.execute('''
   	CREATE TABLE Cars (
    id_car INTEGER,
    Make VARCHAR(50) NOT NULL,
    Model VARCHAR(50) NOT NULL,
    Year INTEGER NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    Mileage INTEGER,
    Color VARCHAR(30),
    Engine VARCHAR(50),
    Transmission VARCHAR(20),
    Stock INT DEFAULT 0, -- Количество доступных автомобилей
    PRIMARY KEY ("id_car" AUTOINCREMENT)
);      
''')
	Cars = [
    ('Toyota', 'Camry', 2020, 24000.00, 15000, 'Black'),
    ('Honda', 'Accord', 2019, 22000.00, 20000, 'White'),
    ('Nissan', 'Altima', 2021, 26000.00, 5000, 'Blue')
]

 
	db.execute('''
   	CREATE TABLE "orders" (
	"id_orders"	INTEGER,
	"order"	TEXT,
	"id_cars"	INTEGER,
	"id_users"	INTEGER,
	PRIMARY KEY("id_orders" AUTOINCREMENT),
	FOREIGN KEY("id_cars") REFERENCES "Cars"("id_car"),
	FOREIGN KEY("id_users") REFERENCES "users"("id_users")
);
''')
	db.execute('''
CREATE TABLE Sales (
    id_sales INTEGER,
    id_car INT NOT NULL,
    id_users INT NOT NULL,
    SaleDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    SalePrice DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_car) REFERENCES Cars(id_car),
    FOREIGN KEY (id_users) REFERENCES users(id_users),
    PRIMARY KEY ("id_sales" AUTOINCREMENT)
);
''')
	cursor.executemany('''
INSERT INTO Cars (Make, Model, Year, Price, Mileage, Color) 
VALUES (?, ?, ?, ?, ?, ?);
''', Cars)            

db.commit()
