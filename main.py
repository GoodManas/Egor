import sys 
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem
from api.user import register, login, get_all_users, exel



from ui.register_and_login import Ui_MainWindow
from ui.ui_admin_panel import Ui_Admin


class Register_and_Login(QMainWindow):
    def __init__(self):
        super(Register_and_Login, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui_admin = Ui_Admin()
        self.ui.setupUi(self)
        
        self.ui.btn_login.clicked.connect(self.auth)
        self.ui.btn_register.clicked.connect(self.reg)
        self.base_lane_edit = [self.ui.lineEditLogin, self.ui.lineEditPass]
        
    def auth(self):
        name = self.ui.lineEditLogin.text()
        passw = self.ui.lineEditPass.text()
        user = login(name, passw)  
        print(user)
        
        try:
            user = login(name, passw)  
            print(user)
            
            position_id = user['dol']  
        
            
                    
            if position_id == 1:  
                self.open_ui_ADMIN()
            elif position_id == 2:  
                self.open_ui_POKUPATEL()
            else:
                QMessageBox.warning(self, "Ошибка", "Неизвестная должность")
    
        except Exception as e: 
            print("Error occurred:", str(e))
            QMessageBox.warning(self, "Ошибка", str(e))   
    
    def open_ui_ADMIN(self):
        print('открылось окно с админомм')
        
        windows = QMainWindow(self)  
        self.windows = Ui_Admin()  
        self.windows.setupUi(windows) 
        
        
        self.windows.btn_login_4.clicked.connect(self.show_users)
        self.windows.btn_login_5.clicked.connect(self.Exel)
        self.windows.btn_login_6.clicked.connect(self.end)
        self.base_lane_edit = [self.ui.lineEditLogin, self.ui.lineEditPass]
        
        windows.show()
    
    def show_users(self):
       
        users = get_all_users()
        
        #модель для QTableView
        model = QStandardItemModel(len(users), 5)  # Измените количество столбцов в соответствии с вашей таблицей
        model.setHorizontalHeaderLabels(["id", "login", "password", "dol"])  # Замените на ваши реальные названия столбцов
        
        for row_idx, row_data in enumerate(users):
            for col_idx, item in enumerate(row_data):
                model.setItem(row_idx, col_idx, QStandardItem(str(item)))  
        
        self.windows.tableView_2.setModel(model)
        
        
    def reg(self):
        name = self.ui.lineEditLogin.text()
        passw = self.ui.lineEditPass.text()
        register(name, passw)
        print('Autor')  
    
    def Exel(self):
        exel()       
        
    def end(self):
        self.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Register_and_Login()
    window.show()   
    sys.exit(app.exec())