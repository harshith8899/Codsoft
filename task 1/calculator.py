from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QLabel
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon("cal_icon.png")) #For icon
        self.setWindowTitle("PYQT APP")
        self.setFixedSize(300, 400)
        label = QLabel("CALCULATOR", self)
        label.setFont(QFont("Arial", 15))
        label.setGeometry(0, 0, 300, 100)
        label.setStyleSheet("color:#3498db;"
                            "font-weight: bold;"
                            "background-color:WHITE;")
        
        label.setAlignment(Qt.AlignHCenter)

        #layouts
        main_layout = QVBoxLayout()
        grid_layout = QGridLayout()

        #Display Screen
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 20px; padding: 10px;")
        main_layout.addWidget(self.display)

        #button lables
        buttons = [
            ('7','8','9','/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('C', '0', '=', '+')
        ]

        #create buttons
        for row_idx, row in enumerate(buttons):
            for col_idx, label in enumerate(row):
                button = QPushButton(label)
                button.setFixedSize(50,50)
                button.setStyleSheet("""
                QPushButton {
                        background-color: #3498db;
                        border-radius: 10px;
                        font-size: 20px;
                        color: white;
                        border: none;
                    }
                    QPushButton:hover {
                        background-color: #2980b9;
                    }
                """)
                button.clicked.connect(lambda checked, text=label: self.on_button_click(text))
                grid_layout.addWidget(button, row_idx, col_idx)

                main_layout.addLayout(grid_layout)
        self.setLayout(main_layout)

    def on_button_click(self, text):
        """Handles button click events"""
        if text == "C":
            self.display.setText("")  # Clear display
        elif text == "=":
            try:
                result = eval(self.display.text())  # Evaluate the expression
                self.display.setText(str(result))
            except:
                self.display.setText("Error")  # Handle invalid input
        else:
            self.display.setText(self.display.text() + text)  # Append to display

# Run Application
app = QApplication(sys.argv)
window = Calculator()
window.show()
sys.exit(app.exec_())


