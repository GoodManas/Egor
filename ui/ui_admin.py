# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_admin.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTableView, QWidget)

class Ui_Admin(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(811, 620)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"border: 1px  solid rgba(225,255,255,40);\n"
"border-radius: 7px;")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-100, -110, 1191, 821))
        self.widget.setStyleSheet(u"background-color:rgb(43, 42, 51);\n"
"color: white;")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 110, 91, 51))
        self.label_2.setStyleSheet(u"background-color:rgba(225,255,255,0);\n"
"border: 0px  solid rgba(225,255,255,40);\n"
"color: white;")
        self.btn_otchet = QPushButton(self.widget)
        self.btn_otchet.setObjectName(u"btn_otchet")
        self.btn_otchet.setEnabled(True)
        self.btn_otchet.setGeometry(QRect(130, 200, 100, 31))
        self.btn_otchet.setMaximumSize(QSize(100, 60))
        self.btn_otchet.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color:rgba(255,255,255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60)\n"
"}\n"
"")
        self.btn_otchet.setIconSize(QSize(24, 24))
        self.btn_exel = QPushButton(self.widget)
        self.btn_exel.setObjectName(u"btn_exel")
        self.btn_exel.setEnabled(True)
        self.btn_exel.setGeometry(QRect(350, 200, 61, 31))
        self.btn_exel.setMaximumSize(QSize(100, 60))
        self.btn_exel.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color:rgba(255,255,255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60)\n"
"}\n"
"")
        self.btn_exel.setIconSize(QSize(24, 24))
        self.tableView_2 = QTableView(self.widget)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setGeometry(QRect(120, 250, 761, 401))
        self.tableView_2.setStyleSheet(u"QTableView{\n"
"background-color: rgba(43, 42, 51, 30);\n"
"border:1px solid rgba(255, 255, 255, 100);\n"
"border-botton-right-radius: 7px;\n"
"border-botton-left-radius: 7px;\n"
"}\n"
"QTableView::section{\n"
"background-color:rgb(196, 196, 199,40);\n"
"color: white;\n"
"border:none;\n"
"height:50px;\n"
"font-size:14px;\n"
"}\n"
"QTableView::item{\n"
"border-style:none;\n"
"border-botton:rgba(43, 42, 51, 40);\n"
"}\n"
"\n"
"QTableView::item::selected{\n"
"border:none;\n"
"color:rgba(43, 42, 51);\n"
"background-color: rgba(43, 42, 51, 50);\n"
"}\n"
"\n"
"")
        self.btn_end = QPushButton(self.widget)
        self.btn_end.setObjectName(u"btn_end")
        self.btn_end.setEnabled(True)
        self.btn_end.setGeometry(QRect(820, 690, 71, 23))
        self.btn_end.setMaximumSize(QSize(100, 60))
        self.btn_end.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color:rgba(255,255,255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60)\n"
"}\n"
"")
        self.btn_end.setIconSize(QSize(24, 24))
        self.btn_add_cars = QPushButton(self.widget)
        self.btn_add_cars.setObjectName(u"btn_add_cars")
        self.btn_add_cars.setEnabled(True)
        self.btn_add_cars.setGeometry(QRect(740, 690, 71, 23))
        self.btn_add_cars.setMaximumSize(QSize(100, 60))
        self.btn_add_cars.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color:rgba(255,255,255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60)\n"
"}\n"
"")
        self.btn_add_cars.setIconSize(QSize(24, 24))
        self.tableView_3 = QTableView(self.widget)
        self.tableView_3.setObjectName(u"tableView_3")
        self.tableView_3.setGeometry(QRect(920, 380, 761, 401))
        self.tableView_3.setStyleSheet(u"QTableView{\n"
"background-color: rgba(43, 42, 51, 30);\n"
"border:1px solid rgba(255, 255, 255, 100);\n"
"border-botton-right-radius: 7px;\n"
"border-botton-left-radius: 7px;\n"
"}\n"
"QTableView::section{\n"
"background-color:rgb(196, 196, 199,40);\n"
"color: white;\n"
"border:none;\n"
"height:50px;\n"
"font-size:14px;\n"
"}\n"
"QTableView::item{\n"
"border-style:none;\n"
"border-botton:rgba(43, 42, 51, 40);\n"
"}\n"
"\n"
"QTableView::item::selected{\n"
"border:none;\n"
"color:rgba(43, 42, 51);\n"
"background-color: rgba(43, 42, 51, 50);\n"
"}\n"
"\n"
"")
        self.btn_otchet_cars = QPushButton(self.widget)
        self.btn_otchet_cars.setObjectName(u"btn_otchet_cars")
        self.btn_otchet_cars.setEnabled(True)
        self.btn_otchet_cars.setGeometry(QRect(240, 200, 100, 31))
        self.btn_otchet_cars.setMaximumSize(QSize(100, 60))
        self.btn_otchet_cars.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color:rgba(255,255,255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60)\n"
"}\n"
"")
        self.btn_otchet_cars.setIconSize(QSize(24, 24))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440", None))
        self.btn_otchet.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0442 users", None))
        self.btn_exel.setText(QCoreApplication.translate("MainWindow", u"Exel", None))
        self.btn_end.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.btn_add_cars.setText(QCoreApplication.translate("MainWindow", u"Add_cars", None))
        self.btn_otchet_cars.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0442 cars", None))
    # retranslateUi

