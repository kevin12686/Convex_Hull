import sys
from math import acos, sqrt, pow, fabs
from random import randint
from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsScene, QGraphicsLineItem, QGraphicsEllipseItem
from PyQt5.QtGui import QPen, QColor
from gui import Ui_ConvexHullGui


class Point:
    MAX_X = 750
    MAX_Y = 490

    def __init__(self, x, y):
        assert isinstance(x, int) and isinstance(y, int)
        self.x = x
        self.y = y

    def __repr__(self):
        return '<Point x:{} y:{}>'.format(self.x, self.y)

    @staticmethod
    def random_generate():
        return Point(randint(0, Point.MAX_X), randint(0, Point.MAX_Y))

    @staticmethod
    def get_x_distance(Point1, Point2):
        assert isinstance(Point1, Point)
        assert isinstance(Point2, Point)
        return fabs(Point1.x - Point1.x)

    @staticmethod
    def get_y_distance(Point1, Point2):
        assert isinstance(Point1, Point)
        assert isinstance(Point2, Point)
        return fabs(Point1.y - Point1.y)

    @staticmethod
    def get_hyp(Point1, Point2):
        assert isinstance(Point1, Point)
        assert isinstance(Point2, Point)
        return sqrt(pow(Point1.x - Point2.x, 2) + pow(Point1.y - Point2.y, 2))


class Line:
    def __init__(self, Point1, Point2):
        assert isinstance(Point1, Point) and isinstance(Point2, Point)
        self.End_p = (Point1, Point2)

    def __repr__(self):
        return '<Line p1:{} p2:{}>'.format(self.End_p[0].__repr__(), self.End_p[1].__repr__())


class main_gui(Ui_ConvexHullGui, QWidget):

    def __init__(self):
        super(QWidget, self).__init__()
        self.setupUi(self)
        self.set_Scene()
        self.set_Pen()
        self.Point_list = list()
        self.Line_list = list()

        self.vertexconfirm.clicked.connect(self.generate_p)
        self.runbutton.clicked.connect(self.find_convex_hull)
        self.show()

    def set_Scene(self):
        self.Max_x = 750
        self.Max_y = 490
        self.gscene = QGraphicsScene(self)
        self.graphicsView.setScene(self.gscene)

    def set_Pen(self):
        self.POINT_PEN_Width = 4
        self.LINE_PEN_Width = 2
        self.POINT_PEN_Color = QColor(0, 0, 255)
        self.LINE_PEN_Color = QColor(0, 0, 255)
        self.pointPen = QPen()
        self.pointPen.setWidth(self.POINT_PEN_Width)
        self.pointPen.setColor(self.POINT_PEN_Color)
        self.linePen = QPen()
        self.linePen.setWidth(self.LINE_PEN_Width)
        self.linePen.setColor(self.LINE_PEN_Color)

    def add_Point(self, p):
        assert isinstance(p, Point)
        point = QGraphicsEllipseItem(p.x, p.y, self.POINT_PEN_Width, self.POINT_PEN_Width)
        point.setPen(self.pointPen)
        self.gscene.addItem(point)

    def add_Line(self, l):
        assert isinstance(l, Line)
        line = QGraphicsLineItem(l.End_p[0].x, l.End_p[0].y, l.End_p[1].x, l.End_p[1].y)
        line.setPen(self.linePen)
        self.Line_list.append(line)
        self.gscene.addItem(line)

    def remove_last_Line(self):
        self.gscene.removeItem(self.Line_list.pop())

    def clear(self):
        self.gscene.clear()
        self.Point_list.clear()
        self.Line_list.clear()

    def all_input_disable(self):
        self.inputbox.setEnabled(False)
        self.vertexconfirm.setEnabled(False)
        self.runbutton.setEnabled(False)

    def all_input_enable(self):
        self.inputbox.setEnabled(True)
        self.vertexconfirm.setEnabled(True)
        self.runbutton.setEnabled(True)

    def generate_p(self):
        self.all_input_disable()
        self.clear()
        for i in range(self.inputbox.value()):
            p = Point.random_generate()
            self.Point_list.append(p)
            self.add_Point(p)
        self.all_input_enable()

    def find_convex_hull(self):
        self.all_input_disable()

        if len(self.Point_list) > 0:
            sort_x = self.Point_list
            sort_y = self.Point_list.copy()
            sort_x.sort(key=lambda k: k.x)
            sort_y.sort(key=lambda k: k.y)

        self.all_input_enable()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = main_gui()
    sys.exit(app.exec_())
