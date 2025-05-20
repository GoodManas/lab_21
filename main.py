import sys
import os
import MySQLdb as mdb

from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QWidget
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from qwerclass import *

from ui.auth import Ui_Auth
from ui.main2 import Ui_Main




class Register(QMainWindow):
    def __init__(self):
        super(Register, self).__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.onClicked)
        self.ui.pushButton_2.clicked.connect(self.end)

    def open_ui_auth(self):
        
        dialog = QDialog(self)  
        self.dialog = Ui_Auth()  
        self.dialog.setupUi(dialog)

    def end(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.close()

    def onClicked(self):
        login = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        data = QwerSql().auth(login,password)
        print('Тест. Получено: ', data)
        
        if data:
            print('Тест. Open Window')
            self.open_ui_auth()
        else:
            QMessageBox.about(self,'Ошибка аутентификации', 'Неверно введен логин или пароль:')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Register()
    window.show()   
    sys.exit(app.exec())