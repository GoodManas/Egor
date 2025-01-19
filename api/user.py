from .db import db
import sqlite3
import pandas as pd


def login(login: str, passw: str):

    query = '''
        SELECT id_users, login, password, dol 
        FROM users 
        WHERE login = ? AND password = ?; 
    '''
    
    value = db.execute(query, (login, passw)).fetchone()

    if value:
        return {
            'id_users': value[0],
            'login': value[1],
            'dol': value[3],
        }
        
    raise Exception(f'Unauthorized: User with login "{login}" not found or wrong password')




def register(login, passw):
	value = db.execute(f'''
		SELECT * FROM users 
		WHERE login='{login}'; 
	''').fetchall()
	if value:
		raise Exception("User with this login already exists")

	db.execute(f"INSERT INTO users (login, password) VALUES ('{login}', '{passw}')")
	db.commit()
 
def get_all_users():  
    value = db.execute('SELECT * FROM users;').fetchall()
    return value

def get_all_car():
    value = db.execute('SELECT * FROM Cars;').fetchall()
    return value



def exel():
    try:
        conn = sqlite3.connect('db/Car.db')
        df = pd.read_sql('SELECT * FROM users', conn)
        df.to_excel(r'd:/games/result.xlsx', index=False)
        print("Файл успешно сохранен...")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        conn.close()    
    
def ADD_car(make, model, Year, Price, image_path):
        
    db.execute(f'''
        INSERT INTO Cars (Make, Model, Year, Price, image_path ) VALUES (?, ?, ?, ?, ?)
    ''', (make, model, Year, Price, image_path))
    print('successfully add_car')
    db.commit()

def SAVE(name, passw, Gmail, Number):
    db.execute(f'''
        INSERT INTO users (login, password, Gmail, Number ) VALUES (?, ?, ?, ?)
    ''', (name, passw, Gmail, Number))
    print('successfully user')
    db.commit()


if __name__ == "__main__":
    user_login = "admin"  
    user_password = "admin_password"
    try:
        user = login("admin", "admin_password")
        print("Logged in user data:", user)  
        user_login = user['login']
        print("User login:", user_login)  
        
    except Exception as e:  
        print(f"Error occurred: {e}")