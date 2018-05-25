import sys
from PyQt5 import QtWidgets


class gui(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.move_center()
        self.resize(800, 600)
        self.setWindowTitle('gui_main')
        self.initUI()
        self.show()

    def initUI(self):
        self.groupbox = QtWidgets.QGroupBox('Setting')
        layout = QtWidgets.QGridLayout()
        lebal = QtWidgets.QLabel('Vertex: ', self)
        layout.addWidget(lebal, 0, 0)
        number_input = QtWidgets.QSpinBox(self)
        number_input.setRange(3, 50)
        layout.addWidget(number_input, 0, 1)
        start_button = QtWidgets.QPushButton('Run', self)
        layout.addWidget(start_button, 0, 5)
        self.groupbox.setLayout(layout)
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.groupbox)
        self.setLayout(main_layout)

    def move_center(self):
        frameGm = self.frameGeometry()
        cursorPos = QtWidgets.QApplication.desktop().cursor().pos()
        screem = QtWidgets.QApplication.desktop().screenNumber(cursorPos)
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screem).center()
        frameGm.moveCenter(centerPoint)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = gui()
    sys.exit(app.exec_())
