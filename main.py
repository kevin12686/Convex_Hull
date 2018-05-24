import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsScene
from gui import Ui_ConvexHullGui


class main_gui(Ui_ConvexHullGui, QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setupUi(self)
        self.gscene = QGraphicsScene(self)
        self.graphicsView.setScene(self.gscene)
        self.vertexconfirm.clicked.connect(self.print_hello)
        self.show()

    def print_hello(self):
        print(self.inputbox.value())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = main_gui()
    sys.exit(app.exec_())
