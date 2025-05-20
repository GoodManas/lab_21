# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Main(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(517, 446)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-10, -30, 681, 621))
        self.widget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 125, 255), stop:0.427447 rgba(41, 21, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 100, 201, 81))
        font = QFont()
        font.setFamilies([u"Rage"])
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color:rgba(255,255,255,0);\n"
"border:1 px solid rgba(255,255,255,40);\n"
"border-radius: 7 px;")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 190, 91, 41))
        font1 = QFont()
        font1.setFamilies([u"Rage"])
        font1.setPointSize(25)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color:rgba(255,255,255,0);\n"
"border:1 px solid rgba(255,255,255,40);\n"
"border-radius: 7 px;")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 240, 501, 21))
        self.lineEdit.setStyleSheet(u"background-color:rgba(255,255,255,100);\n"
"border:1 px solid rgba(255,255,255,40);\n"
"border-radius: 7 px;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 270, 121, 41))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-color:rgba(255,255,255,0);\n"
"border:1 px solid rgba(255,255,255,40);\n"
"border-radius: 7 px;")
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 320, 501, 21))
        self.lineEdit_2.setStyleSheet(u"background-color:rgba(255,255,255,100);\n"
"border:1 px solid rgba(255,255,255,40);\n"
"border-radius: 7 px;")
        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 410, 501, 41))
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color:rgba(255,255,255,100);\n"
"border:1 px solid rgba(255,255,255,40);\n"
"border-radius: 7 px;")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background-color:rgba(255,255,255,100);\n"
"border:1 px solid rgba(255,255,255,40);\n"
"border-radius: 7 px;")

        self.verticalLayout.addWidget(self.pushButton_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Book Shop", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Login", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0437\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

