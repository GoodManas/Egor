import sys 
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QPixmap
from api.user import register, login, get_all_car, exel, ADD_car, get_all_users, SAVE



from ui.register_and_login import Ui_MainWindow
from ui.ui_admin import Ui_Admin
from ui.ui_add_car import Ui_add_car
from ui.ui_cars import Ui_Cars
from ui.register import Ui_register


class Register_and_Login(QMainWindow):
    def __init__(self):
        super(Register_and_Login, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui_admin = Ui_Admin()
        self.ui.setupUi(self)
        
        self.ui.btn_login.clicked.connect(self.auth)
        self.ui.btn_register.clicked.connect(self.open_register_ui)
        self.base_lane_edit = [self.ui.lineEditLogin, self.ui.lineEditPass]
        
        
    def auth(self):
        name = self.ui.lineEditLogin.text()
        passw = self.ui.lineEditPass.text()
    
        try:
            user = login(name, passw)  
            print(user)
            
            position_id = int(user['dol']) 
            
            print("position_id:", position_id)
        
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
        
        
        self.windows.btn_otchet.clicked.connect(self.show_users)
        self.windows.btn_otchet_cars.clicked.connect(self.show_car)
        self.windows.btn_exel.clicked.connect(self.Exel)
        self.windows.btn_end.clicked.connect(self.end)
        self.windows.btn_add_cars.clicked.connect(self.open_ui_add_car)
       
        
        windows.show()
    
    def open_register_ui (self):
        register = QDialog(self)  
        self.register = Ui_register()  
        self.register.setupUi(register)
        
       
        self.register.btn_save.clicked.connect(self.save)
        
        register.exec()
        
    def open_ui_add_car(self):
        print('открылось окно с админомм')
        
        car = QDialog(self)  
        self.car = Ui_add_car()  
        self.car.setupUi(car) 
        
       
        
        self.car.btn_add_cars.clicked.connect(self.add_car)
        self.car.btn_add_cars_2.clicked.connect(self.load_image)
        self.car.btn_end.clicked.connect(self.end)
        
        
        car.exec()
    
    def add_car(self):
        make = self.car.lineMake.text()
        model = self.car.lineModel.text()
        Year = self.car.lineYear.text()
        Price = self.car.linePrice.text()
        image_path = self.image_path
        
        print(make, model, Year, Price, image_path)
    
        if make and model and Year and Price and image_path:  # Проверяем, что все поля заполнены
            ADD_car(make, model, Year, Price, image_path)
        else:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля.") 
        
        
    def load_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "", "Images (*.png *.jpg *.jpeg);;All Files (*)", options=options)
        if file_name:
            
            self.image_path = file_name    
            
            pixmap = QPixmap(file_name)
            self.car.labelImage.setPixmap(pixmap.scaled(200, 200))
    
    def show_users(self):
       
        users = get_all_users()
        
        #модель для QTableView
        model = QStandardItemModel(len(users), 4)  # Измените количество столбцов в соответствии с вашей таблицей
        model.setHorizontalHeaderLabels(["id", "Login", "Password", "role" ])  # Замените на ваши реальные названия столбцов
        
        for row_idx, row_data in enumerate(users):
            for col_idx, item in enumerate(row_data):
                model.setItem(row_idx, col_idx, QStandardItem(str(item)))  
        
        self.windows.tableView_2.setModel(model)
    
    def show_car(self):
       
        users = get_all_car()
        
        #модель для QTableView
        model = QStandardItemModel(len(users), 5)  # Измените количество столбцов в соответствии с вашей таблицей
        model.setHorizontalHeaderLabels(["id", "Make", "Model", "Year", "Price" ])  # Замените на ваши реальные названия столбцов
        
        for row_idx, row_data in enumerate(users):
            for col_idx, item in enumerate(row_data):
                model.setItem(row_idx, col_idx, QStandardItem(str(item)))  
        
        self.windows.tableView_2.setModel(model)     
        
    def open_ui_POKUPATEL(self):
        windows = QMainWindow(self)  
        self.windows = Ui_Cars()  
        self.windows.setupUi(windows)
        
        self.windows.btn_end.clicked.connect(self.end)
        self.windows.btn_exel.clicked.connect(self.show_car)
        #доделать показ машины еу
        
        windows.show()
        
                
    def reg(self):
        name = self.ui.lineEditLogin.text()
        passw = self.ui.lineEditPass.text()
        register(name, passw)
        print('Autor')  
    
    def Exel(self):
        exel()       
        
    def end(self):
        self.close()
    
    def save(self):
        name = self.register.lineEditLogin.text()
        passw = self.register.lineEditPass.text()
        Gmail = self.register.lineEditGmail.text()
        Number = self.register.lineEditNumber.text()
        
        if name and passw and Gmail and Number:  # Проверяем, что все поля заполнены
            SAVE(name, passw, Gmail, Number)
        else:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля.") 

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Register_and_Login()
    window.show()  
    sys.exit(app.exec())