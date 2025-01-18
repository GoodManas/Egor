# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_register(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(333, 436)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-30, -30, 611, 631))
        self.widget.setStyleSheet(u"border: 1px  solid rgba(225,255,255,40);\n"
"border-radius: 7px;")
        self.lineEditLogin_2 = QLineEdit(self.widget)
        self.lineEditLogin_2.setObjectName(u"lineEditLogin_2")
        self.lineEditLogin_2.setGeometry(QRect(140, 130, 91, 20))
        self.lineEditLogin_2.setStyleSheet(u"background-color:rgba(225,255,255,0);\n"
"border: 0px  solid rgba(225,255,255,0);\n"
"color:black;")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(20, 20, 401, 541))
        self.widget_2.setStyleSheet(u"background-color:rgb(43, 42, 51);")
        self.Login = QLabel(self.widget_2)
        self.Login.setObjectName(u"Login")
        self.Login.setGeometry(QRect(110, 140, 131, 21))
        self.Login.setStyleSheet(u"background-color:rgba(225,255,255,100);")
        self.lineEditLogin = QLineEdit(self.widget_2)
        self.lineEditLogin.setObjectName(u"lineEditLogin")
        self.lineEditLogin.setGeometry(QRect(150, 140, 91, 20))
        self.lineEditLogin.setStyleSheet(u"background-color:rgba(225,255,255,0);\n"
"border: 0px  solid rgba(225,255,255,0);")
        self.Password = QLabel(self.widget_2)
        self.Password.setObjectName(u"Password")
        self.Password.setGeometry(QRect(110, 170, 131, 21))
        self.Password.setStyleSheet(u"background-color:rgba(225,255,255,100);")
        self.lineEditPass = QLineEdit(self.widget_2)
        self.lineEditPass.setObjectName(u"lineEditPass")
        self.lineEditPass.setGeometry(QRect(160, 170, 81, 20))
        self.lineEditPass.setStyleSheet(u"background-color:rgba(225,255,255,0);\n"
"border: 0px  solid rgba(225,255,255,0);")
        self.Gmail = QLabel(self.widget_2)
        self.Gmail.setObjectName(u"Gmail")
        self.Gmail.setGeometry(QRect(110, 200, 131, 21))
        self.Gmail.setStyleSheet(u"background-color:rgba(225,255,255,100);")
        self.lineEditGmail = QLineEdit(self.widget_2)
        self.lineEditGmail.setObjectName(u"lineEditGmail")
        self.lineEditGmail.setGeometry(QRect(150, 200, 81, 20))
        self.lineEditGmail.setStyleSheet(u"background-color:rgba(225,255,255,0);\n"
"border: 0px  solid rgba(225,255,255,0);")
        self.Number = QLabel(self.widget_2)
        self.Number.setObjectName(u"Number")
        self.Number.setGeometry(QRect(110, 230, 131, 21))
        self.Number.setStyleSheet(u"background-color:rgba(225,255,255,100);")
        self.lineEditNumber = QLineEdit(self.widget_2)
        self.lineEditNumber.setObjectName(u"lineEditNumber")
        self.lineEditNumber.setGeometry(QRect(160, 230, 81, 20))
        self.lineEditNumber.setStyleSheet(u"background-color:rgba(225,255,255,0);\n"
"border: 0px  solid rgba(225,255,255,0);")
        self.Password_2 = QLabel(self.widget_2)
        self.Password_2.setObjectName(u"Password_2")
        self.Password_2.setGeometry(QRect(20, 20, 131, 21))
        self.Password_2.setStyleSheet(u"background-color:rgba(225,255,255,100);")
        self.btn_save = QPushButton(self.widget_2)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setEnabled(True)
        self.btn_save.setGeometry(QRect(130, 260, 79, 23))
        self.btn_save.setMaximumSize(QSize(100, 60))
        self.btn_save.setStyleSheet(u"QPushButton{\n"
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
        self.btn_save.setIcon(icon)
        self.btn_save.setIconSize(QSize(24, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Login.setText(QCoreApplication.translate("Dialog", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.Password.setText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.lineEditPass.setText("")
        self.Gmail.setText(QCoreApplication.translate("Dialog", u"Gmail:", None))
        self.lineEditGmail.setText("")
        self.Number.setText(QCoreApplication.translate("Dialog", u"Number:", None))
        self.lineEditNumber.setText("")
        self.Password_2.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.btn_save.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

