import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget,QBoxLayout,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit,QMessageBox
)

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Welcome')
        self.setGeometry(200,200,400,350)

        self.title_label=QLabel("Welcome to PYQT")
        self.title_label.setStyleSheet('font-size:16px;font-weight=bold')

        self.name_input=QLineEdit()
        self.name_input.setPlaceholderText('Enter your Name')

        self.greet_button=QPushButton('greet')
        self.clear_button=QPushButton('clear')

        button=QHBoxLayout()
        button.addWidget(self.greet_button)
        button.addWidget(self.clear_button)

        main=QVBoxLayout()
        main.addWidget(self.title_label)
        main.addWidget(self.name_input)
        main.addLayout(button)

        self.setLayout(main)
        self.greet_button.clicked.connect(self.greet)
        self.clear_button.clicked.connect(self.clear)
  
    def greet(self):
        """Greets the user using input from QLineEdit"""
        name = self.name_input.text()

        if name.strip() == "":
            QMessageBox.warning(self, "Input Error", "Please enter your name")
        else:
            QMessageBox.information(self, "Greeting", f"Hello, {name}!")

    def clear(self):
        """Clears the text field"""
        self.name_input.clear()


class LogicExamples(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Logical Examples")
        self.setGeometry(650, 200, 400, 300)

        self.info_label = QLabel("Logical Examples (Real-World Problems)")

        # Example 1: Age Validation
        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Enter your age")

        self.age_button = QPushButton("Check Eligibility")

        # Example 2: Simple Login Validation
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Username")

        self.pass_input = QLineEdit()
        self.pass_input.setPlaceholderText("Password")
        self.pass_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login")

        # Example 3: Bill Calculation
        self.bill_input = QLineEdit()
        self.bill_input.setPlaceholderText("Enter bill amount")

        self.bill_button = QPushButton("Calculate Discount")

        layout = QVBoxLayout()
        layout.addWidget(self.info_label)
        layout.addWidget(self.age_input)
        layout.addWidget(self.age_button)
        layout.addWidget(self.user_input)
        layout.addWidget(self.pass_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.bill_input)
        layout.addWidget(self.bill_button)

        self.setLayout(layout)

        # Signals
        self.age_button.clicked.connect(self.check_age)
        self.login_button.clicked.connect(self.login_check)
        self.bill_button.clicked.connect(self.calculate_discount)

    # Logical Example 1: Age Eligibility Check
    # Real-world use: Voting / Driving / Admission
    def check_age(self):
        try:
            age = int(self.age_input.text())
            if age >= 18:
                QMessageBox.information(self, "Eligible", "You are eligible!")
            else:
                QMessageBox.warning(self, "Not Eligible", "You must be 18+")
        except ValueError:
            QMessageBox.warning(self, "Error", "Enter a valid number")

    # Logical Example 2: Login Validation
    # Real-world use: Authentication systems
    def login_check(self):
        username = self.user_input.text()
        password = self.pass_input.text()

        # Hardcoded credentials (for learning purpose)
        if username == "admin" and password == "4321":
            QMessageBox.information(self, "Login Success", "Welcome Admin")
        else:
            QMessageBox.critical(self, "Login Failed", "Invalid credentials")

    # Logical Example 3: Bill Discount Calculation
    # Real-world use: Shopping apps
    def calculate_discount(self):
        try:
            amount = float(self.bill_input.text())

            if amount >= 1000:
                discount = amount * 0.10
            else:
                discount = amount * 0.05

            final_amount = amount - discount

            QMessageBox.information(
                self,
                "Bill Summary",
                f"Discount: ₹{discount:.2f}\nFinal Amount: ₹{final_amount:.2f}"
            )
        except ValueError:
            QMessageBox.warning(self, "Error", "Enter a valid amount")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    main_window = window()
    logic_window = LogicExamples()

    main_window.show()
    logic_window.show()

    sys.exit(app.exec_())




