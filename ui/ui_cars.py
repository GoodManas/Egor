# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_cars.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
import res_rc

class Ui_Cars(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 640)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"border: 1px  solid rgba(225,255,255,40);\n"
"border-radius: 7px;")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-180, -70, 1471, 1021))
        self.widget.setStyleSheet(u"background-color:rgb(43, 42, 51);")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(490, 80, 151, 16))
        self.label_2.setStyleSheet(u"color: white;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(210, 120, 101, 41))
        self.label_3.setStyleSheet(u"color: white;")
        self.btn_end = QPushButton(self.widget)
        self.btn_end.setObjectName(u"btn_end")
        self.btn_end.setGeometry(QRect(870, 670, 97, 23))
        self.btn_end.setMaximumSize(QSize(400, 60))
        self.btn_end.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color:rgba(255,255,255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60)\n"
"}")
        self.btn_end.setIconSize(QSize(24, 24))
        self.buy_ToyotaCamry = QPushButton(self.widget)
        self.buy_ToyotaCamry.setObjectName(u"buy_ToyotaCamry")
        self.buy_ToyotaCamry.setGeometry(QRect(200, 310, 51, 31))
        self.buy_ToyotaCamry.setMaximumSize(QSize(400, 60))
        self.buy_ToyotaCamry.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color:rgba(255,255,255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60)\n"
"}")
        self.buy_ToyotaCamry.setIconSize(QSize(24, 24))
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(260, 310, 91, 31))
        self.label_4.setStyleSheet(u"color: white;")
        self.buy_Honda = QPushButton(self.widget)
        self.buy_Honda.setObjectName(u"buy_Honda")
        self.buy_Honda.setGeometry(QRect(500, 310, 51, 31))
        self.buy_Honda.setMaximumSize(QSize(400, 60))
        self.buy_Honda.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color:rgba(255,255,255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60)\n"
"}")
        self.buy_Honda.setIconSize(QSize(24, 24))
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(560, 310, 91, 31))
        self.label_5.setStyleSheet(u"color: white;")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(460, 180, 261, 101))
        self.label_6.setStyleSheet(u"background-color:rgba(225,255,255,0);\n"
"border: 0px  solid rgba(225,255,255,40);\n"
"color: light;\n"
"")
        self.label_6.setPixmap(QPixmap(u":/icons/icon/car6.png"))
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(190, 190, 201, 121))
        self.label_7.setStyleSheet(u"background-color:rgba(225,255,255,0);\n"
"border: 0px  solid rgba(225,255,255,40);\n"
"color: light;\n"
"")
        self.label_7.setPixmap(QPixmap(u":/icons/icon/camry.png"))
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(210, 400, 261, 101))
        self.label_8.setStyleSheet(u"background-color:rgba(225,255,255,0);\n"
"border: 0px  solid rgba(225,255,255,40);\n"
"color: light;\n"
"")
        self.label_8.setPixmap(QPixmap(u":/icons/icon/NISSAN.png"))
        self.btn_Nissan = QPushButton(self.widget)
        self.btn_Nissan.setObjectName(u"btn_Nissan")
        self.btn_Nissan.setGeometry(QRect(220, 510, 51, 31))
        self.btn_Nissan.setMaximumSize(QSize(400, 60))
        self.btn_Nissan.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color:rgba(255,255,255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60)\n"
"}")
        self.btn_Nissan.setIconSize(QSize(24, 24))
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(280, 510, 91, 31))
        self.label_9.setStyleSheet(u"color: white;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0440\u044b\u0439 \u0434\u0435\u043d\u044c \u043f\u043e\u043a\u0443\u043f\u0430\u0442\u0435\u043b\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u043e\u043b\u043e\u0433 \u043c\u0430\u0448\u0438\u043d", None))
        self.btn_end.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.buy_ToyotaCamry.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0443\u043f\u0438\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Toyota Camry", None))
        self.buy_Honda.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0443\u043f\u0438\u0442\u044c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Honda Accord", None))
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_8.setText("")
        self.btn_Nissan.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0443\u043f\u0438\u0442\u044c", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Nissan Altima", None))
    # retranslateUi

