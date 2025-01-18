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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTableView,
    QWidget)
import res_rc


class Ui_Cars(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(802, 640)
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
        self.tableView_2 = QTableView(self.widget)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setGeometry(QRect(190, 170, 781, 321))
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
        self.btn_exel = QPushButton(self.widget)
        self.btn_exel.setObjectName(u"btn_exel")
        self.btn_exel.setEnabled(True)
        self.btn_exel.setGeometry(QRect(190, 120, 100, 41))
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
        self.btn_end_2 = QPushButton(self.widget)
        self.btn_end_2.setObjectName(u"btn_end_2")
        self.btn_end_2.setGeometry(QRect(220, 560, 111, 23))
        self.btn_end_2.setMaximumSize(QSize(400, 60))
        self.btn_end_2.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color:rgba(255,255,255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60)\n"
"}")
        self.btn_end_2.setIconSize(QSize(24, 24))
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(220, 510, 271, 21))
        self.label_3.setStyleSheet(u"color: white;")
        self.lineEditLogin = QLineEdit(self.widget)
        self.lineEditLogin.setObjectName(u"lineEditLogin")
        self.lineEditLogin.setGeometry(QRect(340, 560, 41, 20))
        self.lineEditLogin.setStyleSheet(u"background-color:rgba(225,255,255,0);\n"
"border: 0px  solid rgba(225,255,255,0);\n"
"color:black;")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(340, 560, 41, 21))
        self.widget_2.setStyleSheet(u"background-color:rgba(225,255,255,100);")
        self.widget_2.raise_()
        self.label_2.raise_()
        self.btn_end.raise_()
        self.tableView_2.raise_()
        self.btn_exel.raise_()
        self.btn_end_2.raise_()
        self.label_3.raise_()
        self.lineEditLogin.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0440\u044b\u0439 \u0434\u0435\u043d\u044c \u043f\u043e\u043a\u0443\u043f\u0430\u0442\u0435\u043b\u044c", None))
        self.btn_end.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.btn_exel.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u043e\u043b\u043e\u0433 \u043c\u0430\u0448\u0438\u043d", None))
        self.btn_end_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043c\u0430\u0448\u0438\u043d\u0443", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 ID \u043c\u0430\u0448\u0438\u043d\u044b \u043a\u043e\u0442\u043e\u0440\u0443\u044e \u0445\u043e\u0442\u0438\u0442\u0435 \u043a\u0443\u043f\u0438\u0442\u044c ", None))
    # retranslateUi

