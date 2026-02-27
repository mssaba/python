import sys
from PyQt5.QtWidgets import(
     QApplication, QWidget,QBoxLayout,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit,QMessageBox
)

class window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('AVERAGE CALCULATOR')
        self.setGeometry(300,300,500,450)

        self.info_label=QLabel('AVERAGE CALCULATOR')


        self.mark_1=QLineEdit()
        self.mark_1.setPlaceholderText('Enter Mark1')

        self.mark_2=QLineEdit()
        self.mark_2.setPlaceholderText('Enter Mark2')

        self.mark_3=QLineEdit()
        self.mark_3.setPlaceholderText('Enter Mark3')

        self.mark_4=QLineEdit()
        self.mark_4.setPlaceholderText('Enter Mark4')

        self.calculate=QPushButton("Calculate Average")
        layout = QVBoxLayout()
        layout.addWidget(self.info_label)
        layout.addWidget(self.mark_1)
        layout.addWidget(self.mark_2)
        layout.addWidget(self.mark_3)
        layout.addWidget(self.mark_4)
        layout.addWidget(self.calculate)
        self.setLayout(layout)
        self.calculate.clicked.connect(self.cal_avg)
    def cal_avg(self):
            a=(int(self.mark_1.text() + self.mark_2.text() + self.mark_3.text() + self.mark_4.text()))/4
            QMessageBox.information(self,
                                    'Average',
                                    f"Average: {a:.2f}"
                                    )
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = window()
    main_window.show()
    sys.exit(app.exec_())