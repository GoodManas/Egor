from .db import db
import sqlite3
import pandas as pd


def login(login: str, passw: str):

	value = db.execute(f'''
		SELECT id_users, login, password, dol, start_day FROM users 
		WHERE login='{login}' AND password='{passw}'; 
	''').fetchone()

	

	if value:
		return {
        	'id_users': value[0],
            'login': value[1],
            'dol': value[3],
            'start_day': value[4],
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