import sys
import os
import MySQLdb as mdb

from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QWidget
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QByteArray, QRect, Qt
from PySide6.QtWidgets import QMainWindow 
from api.qwerclass import *


from ui.main2 import Ui_Main
from ui.image import Ui_Image


get_data = QwerSql.get_data()


class Register(QMainWindow):
    def __init__(self):
        super(Register, self).__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.onClicked)
        self.ui.pushButton_2.clicked.connect(self.end)
        


    def create_image_widget(res_data, parent=None):
        
        if hasattr(res_data, 'get_data'):  # Если есть метод get_data()
            res_data = res_data.get_data()  # Получаем список данных
        elif hasattr(res_data, '__dict__'): # Если можно преобразовать в dict
            res_data = list(res_data.__dict__.values())
    
    # Проверяем, что res_data теперь итерируемый объект
        if not isinstance(res_data, (list, tuple)):
            raise ValueError("res_data должен быть списком или кортежем")
        if parent is not None and not isinstance(parent, QWidget):
            parent = None  
    
        widget = QWidget(parent) 
        height = 20 
    
        for item in res_data:
            img_id, _, img_bytes = item  
        
            
            qimage = QImage.fromData(QByteArray(img_bytes))
            qpixmap = QPixmap.fromImage(qimage)
        
            
            file_path = f"save_img/{img_id}.jpg"
            qpixmap.save(file_path, "JPG")
        
            
            label = QLabel(widget)
            label.setGeometry(QRect(10, height, 500, 280))
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setText("")
            label.setPixmap(QPixmap(file_path).scaled(170, 170))
            label.setObjectName(f"{img_id}")
        
            height += 230  
    
        return widget

    def open_ui_image(self):
        image = QDialog(self)
        self.image = Ui_Image ()
        self.image.setupUi(image) 
        
        self.image.pushButton.clicked.connect(self.create_image_widget)
      
        
        image.exec()

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
            self.open_ui_image()
        else:
            QMessageBox.about(self,'Ошибка аутентификации', 'Неверно введен логин или пароль:')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Register()
    window.show()   
    sys.exit(app.exec())