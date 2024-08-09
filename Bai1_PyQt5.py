import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QWidget, QVBoxLayout

class YesNoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Đặt tiêu đề và kích thước ban đầu của cửa sổ
        self.setWindowTitle('Game App')
        self.setGeometry(100, 100, 300, 200)

        # Tạo tiện ích trung tâm và đặt nó làm tiện ích trung tâm của cửa sổ chính
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Tạo các nút "Có" và "Không"
        yes_button = QPushButton('Bắt đầu game', self)
        no_button = QPushButton('Thoát game', self)

        # Kết nối các lần nhấp vào nút với các phương thức
        yes_button.clicked.connect(self.show_yes_message)
        no_button.clicked.connect(self.show_no_message)

        # Tạo bố cục và thêm các nút vào bố cục
        layout = QVBoxLayout()
        layout.addWidget(yes_button)
        layout.addWidget(no_button)
        
        # Đặt bố cục cho tiện ích trung tâm
        central_widget.setLayout(layout)

    def show_yes_message(self):
        QMessageBox.information(self, 'Thông báo', 'Bạn đã bắt đầu game"')

    def show_no_message(self):
        QMessageBox.information(self, 'Thông báo', 'Bạn đã thoát game"')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = YesNoApp()
    window.show()
    sys.exit(app.exec_())
