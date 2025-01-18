# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_add_car.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_add_car(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(370, 419)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-30, -50, 511, 541))
        self.widget.setStyleSheet(u"background-color:rgb(43, 42, 51);\n"
"color: white;\n"
"border: 1px  solid rgba(225,255,255,40);\n"
"border-radius: 7px;")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 70, 221, 16))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 90, 221, 16))
        self.btn_add_cars = QPushButton(self.widget)
        self.btn_add_cars.setObjectName(u"btn_add_cars")
        self.btn_add_cars.setEnabled(True)
        self.btn_add_cars.setGeometry(QRect(230, 430, 71, 23))
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
        self.btn_end = QPushButton(self.widget)
        self.btn_end.setObjectName(u"btn_end")
        self.btn_end.setEnabled(True)
        self.btn_end.setGeometry(QRect(310, 430, 71, 23))
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
        self.btn_add_cars_2 = QPushButton(self.widget)
        self.btn_add_cars_2.setObjectName(u"btn_add_cars_2")
        self.btn_add_cars_2.setEnabled(True)
        self.btn_add_cars_2.setGeometry(QRect(240, 150, 100, 23))
        self.btn_add_cars_2.setMaximumSize(QSize(100, 60))
        self.btn_add_cars_2.setStyleSheet(u"QPushButton{\n"
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
        self.btn_add_cars_2.setIconSize(QSize(24, 24))
        self.editline = QFrame(self.widget)
        self.editline.setObjectName(u"editline")
        self.editline.setGeometry(QRect(40, 180, 110, 152))
        self.editline.setStyleSheet(u"border:")
        self.verticalLayout = QVBoxLayout(self.editline)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineMake = QLineEdit(self.editline)
        self.lineMake.setObjectName(u"lineMake")

        self.verticalLayout.addWidget(self.lineMake)

        self.lineModel = QLineEdit(self.editline)
        self.lineModel.setObjectName(u"lineModel")

        self.verticalLayout.addWidget(self.lineModel)

        self.lineYear = QLineEdit(self.editline)
        self.lineYear.setObjectName(u"lineYear")

        self.verticalLayout.addWidget(self.lineYear)

        self.linePrice = QLineEdit(self.editline)
        self.linePrice.setObjectName(u"linePrice")

        self.verticalLayout.addWidget(self.linePrice)

        self.lineImage_path = QLineEdit(self.editline)
        self.lineImage_path.setObjectName(u"lineImage_path")

        self.verticalLayout.addWidget(self.lineImage_path)

        self.labelImage = QLabel(self.widget)
        self.labelImage.setObjectName(u"labelImage")
        self.labelImage.setGeometry(QRect(190, 180, 201, 211))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430 \u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u043c\u0430\u0448\u0438\u043d\u044b", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Make, Model, Year,   Price, image_path", None))
        self.btn_add_cars.setText(QCoreApplication.translate("Dialog", u"Add_cars", None))
        self.btn_end.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.btn_add_cars_2.setText(QCoreApplication.translate("Dialog", u"Load_image_path", None))
        self.labelImage.setText("")
    # retranslateUi

