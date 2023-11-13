import PyQt6
import sys
from datetime import datetime
from PyQt6.QtWidgets import  QApplication, QVBoxLayout, QLabel, QWidget,QGridLayout,QLineEdit,QPushButton,QMainWindow,QTableWidget,QTableWidgetItem
from PyQt6.QtGui import QAction
import sqlite3


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Management System')
        
        file_menu_item = self.menuBar().addMenu('&File')
        help_menu_item = self.menuBar().addMenu('&Help')
        
        add_student_action = QAction('Add Student',self)
        file_menu_item.addAction(add_student_action)
        
        about_action = QAction('About',self)
        help_menu_item.addAction(about_action)
        
        about_action.setMenuRole(QAction.MenuRole.NoRole)
        
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(('Id', 'Name', 'Course', 'Mobile'))
        self.setCentralWidget(self.table)
        self.load_data()
        
    def load_data(self):
        connection = sqlite3.connect('student_management\database.db')
        result = connection.execute("SELECT * FROM students")
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()
        
        
        
        
        
app = QApplication(sys.argv)
management_sys = MainWindow()
management_sys.show()
sys.exit(app.exec())