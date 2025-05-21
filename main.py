from PySide6 import QtWidgets, QtCore, QtGui
import os
import pymysql
from datetime import datetime

# соединение с базой данных
con = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="Ali_21"
)

def get_patients():
    with con.cursor() as cursor:
        cursor.execute("SELECT PatientID, LastName, FirstName, Email, BirthDate, Photo FROM Patient;")
        return cursor.fetchall()

def get_appointments(patient_id):
    # Вызов хранимой процедуры ХП2 через callproc
    with con.cursor() as cursor:
        # Передача параметров: id клиента и текущая дата
        cursor.callproc('ХП2', (patient_id, datetime.now().date()))
        return cursor.fetchall()

class MainWin(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.setWindowTitle("Медицинская карта пациентов")
        self.load_data()

    def setupUi(self):
        self.setGeometry(100, 100, 900, 800)
        self.scroll_area = QtWidgets.QScrollArea(self)
        self.scroll_area.setGeometry(0, 0, 900, 800)
        self.scroll_area.setWidgetResizable(True)
        self.content_widget = QtWidgets.QWidget()
        self.scroll_area.setWidget(self.content_widget)
        self.layout = QtWidgets.QVBoxLayout(self.content_widget)

    def load_data(self):
        photo_dir = "photo"
        if not os.path.exists(photo_dir):
            print(f"Папка '{photo_dir}' не найдена.")
            return

        patients = get_patients()

        for p in patients:
            patient_id = p[0]
            last_name = p[1]
            first_name = p[2]
            email = p[3]
            birth_date = p[4].strftime("%d.%m.%Y") if isinstance(p[4], datetime) else p[4]
            photo_blob = p[5]

            # Группа для пациента
            patient_group = QtWidgets.QGroupBox()
            patient_layout = QtWidgets.QHBoxLayout()
            patient_group.setLayout(patient_layout)

            # Фото
            img_path = os.path.join(photo_dir, f"{last_name}.jpg")
            if os.path.exists(img_path):
                qpixmap = QtGui.QPixmap(img_path)
                if qpixmap.isNull():
                    qpixmap = self.create_gray_pixmap()
                else:
                    qpixmap = qpixmap.scaled(170, 170, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            elif photo_blob:
                try:
                    qimage = QtGui.QImage.fromData(photo_blob)
                    qpixmap = QtGui.QPixmap.fromImage(qimage).scaled(170, 170, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
                except:
                    qpixmap = self.create_gray_pixmap()
            else:
                qpixmap = self.create_gray_pixmap()

            label_photo = QtWidgets.QLabel()
            label_photo.setPixmap(qpixmap)
            label_photo.setFixedSize(170, 170)
            label_photo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            patient_layout.addWidget(label_photo)

            # Информация о пациенте
            info_text = (
                f"<b>Фамилия:</b> {last_name}<br>"
                f"<b>Имя:</b> {first_name}<br>"
                f"<b>Email:</b> {email}<br>"
                f"<b>Дата рождения:</b> {birth_date}"
            )
            label_info = QtWidgets.QLabel()
            label_info.setTextFormat(QtCore.Qt.TextFormat.RichText)
            label_info.setText(info_text)
            label_info.setWordWrap(True)
            label_info.setFixedWidth(500)
            patient_layout.addWidget(label_info)

            self.layout.addWidget(patient_group)

            with con.cursor() as cursor:
                cursor.callproc('ХП1')
                result = cursor.fetchall()

            # Фильтрация по фамилии и имени
            patient_apps = [row for row in result if row[1] == last_name and row[2] == first_name]
            
            if patient_apps:
                header_label = QtWidgets.QLabel("<b>История приёмов:</b>")
                self.layout.addWidget(header_label)

                for app in patient_apps:
                    # Предположим структуру: Фото, LastName, FirstName, Email, BirthDate,
                    # AppointmentDate, ServicesCount, TotalCost
                    service_count = app[6]
                    total_cost = app[7]
                    app_date = app[5]
                    app_date_str = app_date.strftime("%d.%m.%Y") if isinstance(app_date, datetime) else str(app_date)

                    app_text = (
                        f"<b>Дата приёма:</b> {app_date_str}<br>"
                        f"<b>Фамилия:</b> {app[1]}<br>"
                        f"<b>Имя:</b> {app[2]}<br>"
                        f"<b>Количество услуг:</b> {service_count}<br>"
                        f"<b>Общая стоимость:</b> {total_cost} руб."
                    )

                    app_label = QtWidgets.QLabel()
                    app_label.setTextFormat(QtCore.Qt.TextFormat.RichText)
                    app_label.setText(app_text)
                    app_label.setWordWrap(True)
                    app_label.setStyleSheet("background: rgba(255,255,255,50); padding: 5px;")
                    self.layout.addWidget(app_label)
            else:
                no_app_label = QtWidgets.QLabel("Нет данных о приёмах")
                self.layout.addWidget(no_app_label)

            # Разделитель
            separator = QtWidgets.QFrame()
            separator.setFrameShape(QtWidgets.QFrame.Shape.HLine)
            separator.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
            self.layout.addWidget(separator)

    def create_gray_pixmap(self):
        pixmap = QtGui.QPixmap(170, 170)
        pixmap.fill(QtGui.QColor("gray"))
        return pixmap

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWin()
    window.show()
    sys.exit(app.exec())