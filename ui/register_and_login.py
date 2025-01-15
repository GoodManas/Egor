# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(594, 384)
        MainWindow.setMinimumSize(QSize(594, 384))
        MainWindow.setMaximumSize(QSize(594, 384))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"border: 1px  solid rgba(225,255,255,40);\n"
"border-radius: 7px;")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-40, -50, 741, 741))
        self.widget.setStyleSheet(u"background-color:rgb(43, 42, 51);")
        self.Login = QLabel(self.widget)
        self.Login.setObjectName(u"Login")
        self.Login.setGeometry(QRect(270, 180, 131, 21))
        self.Login.setStyleSheet(u"background-color:rgba(225,255,255,100);")
        self.lineEditLogin = QLineEdit(self.widget)
        self.lineEditLogin.setObjectName(u"lineEditLogin")
        self.lineEditLogin.setGeometry(QRect(310, 180, 91, 20))
        self.lineEditLogin.setStyleSheet(u"background-color:rgba(225,255,255,0);\n"
"border: 0px  solid rgba(225,255,255,0);")
        self.lineEditPass = QLineEdit(self.widget)
        self.lineEditPass.setObjectName(u"lineEditPass")
        self.lineEditPass.setGeometry(QRect(320, 210, 81, 20))
        self.lineEditPass.setStyleSheet(u"background-color:rgba(225,255,255,0);\n"
"border: 0px  solid rgba(225,255,255,0);")
        self.Password = QLabel(self.widget)
        self.Password.setObjectName(u"Password")
        self.Password.setGeometry(QRect(270, 210, 131, 21))
        self.Password.setStyleSheet(u"background-color:rgba(225,255,255,100);")
        self.register_and_login = QFrame(self.widget)
        self.register_and_login.setObjectName(u"register_and_login")
        self.register_and_login.setGeometry(QRect(250, 240, 181, 41))
        self.register_and_login.setStyleSheet(u"background-color:rgba(225,255,255,0);\n"
"border: 0px  solid rgba(225,255,255,40);\n"
"color: light;\n"
"")
        self.horizontalLayout = QHBoxLayout(self.register_and_login)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_login = QPushButton(self.register_and_login)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setEnabled(True)
        self.btn_login.setMaximumSize(QSize(100, 60))
        self.btn_login.setStyleSheet(u"QPushButton{\n"
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
        icon = QIcon()
        icon.addFile(u":/icons/icon/login_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24 (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_login.setIcon(icon)
        self.btn_login.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_login)

        self.btn_register = QPushButton(self.register_and_login)
        self.btn_register.setObjectName(u"btn_register")
        self.btn_register.setMaximumSize(QSize(400, 60))
        self.btn_register.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color:rgba(255,255,255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60)\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon/key_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24 (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_register.setIcon(icon1)
        self.btn_register.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_register)

        self.register_and_login.raise_()
        self.Login.raise_()
        self.lineEditLogin.raise_()
        self.Password.raise_()
        self.lineEditPass.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Register_and_login", None))
        self.Login.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.lineEditPass.setText("")
        self.Password.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
        self.btn_register.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi

