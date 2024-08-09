import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QGridLayout, QWidget, QLineEdit
from PyQt5.QtCore import Qt

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Đặt tiêu đề và kích thước ban đầu của cửa sổ
        self.setWindowTitle('Màn hình chơi game')
        self.setGeometry(100, 100, 300, 400)

        # Tạo tiện ích trung tâm và đặt nó làm tiện ích trung tâm của cửa sổ chính
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Tạo QLineEdit để hiển thị dữ liệu đầu vào và kết quả
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(35)

        # Tạo các nút số và toán tử
        self.create_buttons()

        # Tạo bố cục chính
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.display)
        main_layout.addLayout(self.create_main_layout())

        self.central_widget.setLayout(main_layout)

    def create_buttons(self):
        self.buttons = {}
        self.numbers = [
            ('ô 7', 0, 0), ('ô 8', 0, 1), ('ô 9', 0, 2),
            ('ô 4', 1, 0), ('ô 5', 1, 1), ('ô 6', 1, 2),
            ('ô 1', 2, 0), ('ô 2', 2, 1), ('ô 3', 2, 2),
        ]
        self.operators = [
            ('tạm dừng', 0, 3), ('Bắt đầu', 1, 3),
            ('Kết thúc', 2, 3)
           
        ]
        
        for text, row, col in self.numbers:
            self.buttons[text] = QPushButton(text)
            self.buttons[text].clicked.connect(self.number_pressed)

        for text, row, col in self.operators:
            self.buttons[text] = QPushButton(text)
            self.buttons[text].clicked.connect(self.operator_pressed)

    def create_main_layout(self):
        layout = QGridLayout()

        # Thêm các nút số vào lưới
        for text, row, col in self.numbers:
            layout.addWidget(self.buttons[text], row, col)

        # Thêm các nút toán tử vào lưới
        for text, row, col in self.operators:
            layout.addWidget(self.buttons[text], row, col)

        return layout

    def number_pressed(self):
        button = self.sender()
        new_value = self.display.text() + button.text()
        self.display.setText(new_value)

    def operator_pressed(self):
        button = self.sender()
        operator = button.text()

        if operator == 'C':
            self.display.clear()
        elif operator == '=':
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText('Error')
        else:
            # Nếu người dùng nhấn vào toán tử, hãy đảm bảo không thêm nhiều hơn một toán tử liên tiếp
            if self.display.text() and self.display.text()[-1] not in "+-*/":
                self.display.setText(self.display.text() + operator)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())
