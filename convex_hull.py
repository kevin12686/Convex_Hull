import sys
from copy import copy
from math import acos, sqrt
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

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    @staticmethod
    def random_generate():
        return Point(randint(0, Point.MAX_X), randint(0, Point.MAX_Y))

    @staticmethod
    def get_length(Vector):
        assert isinstance(Vector, Point)
        return sqrt(Vector.x ** 2 + Vector.y ** 2)

    @staticmethod
    def get_product(Vector1, Vector2):
        assert isinstance(Vector1, Point)
        assert isinstance(Vector2, Point)
        return Vector1.x * Vector2.x + Vector1.y * Vector2.y

    @staticmethod
    def get_radians(Point_pre, Point_cur, Point_nex):
        assert isinstance(Point_pre, Point)
        assert isinstance(Point_cur, Point)
        assert isinstance(Point_nex, Point)
        U = copy(Point_pre)
        V = copy(Point_nex)
        U.x -= Point_cur.x
        U.y -= Point_cur.y
        V.x -= Point_cur.x
        V.y -= Point_cur.y
        return acos(Point.get_product(U, V) / (Point.get_length(U) * Point.get_length(V)))


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
        self.run = False

        self.vertexconfirm.clicked.connect(self.generate_p)
        self.runbutton.clicked.connect(self.find_convex_hull)
        self.show()

    def set_Scene(self):
        self.Max_x = 750
        self.Max_y = 490
        self.gscene = QGraphicsScene(self)
        self.graphicsView.setScene(self.gscene)

    def set_Pen(self):
        self.POINT_PEN_Width = 2
        self.LINE_PEN_Width = 1
        self.POINT_PEN_Color = QColor(0, 0, 255)
        self.LINE_PEN_Color = QColor(0, 255, 0)
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
        self.run = False
        for i in range(self.inputbox.value()):
            p = Point.random_generate()
            self.Point_list.append(p)
            self.add_Point(p)
        self.all_input_enable()

    def find_convex_hull(self):
        self.all_input_disable()

        if len(self.Point_list) > 3 and not self.run:
            self.run = True
            self.Point_list.sort(key=lambda k: k.y)
            button = self.Point_list[-1]

            flag = False
            point_pre = Point(button.x - 1, button.y)
            point_cur = button

            while point_cur is not button or not flag:
                flag = True
                max_radians = 0
                target = None

                for point_nex in self.Point_list:
                    if point_nex != point_cur and point_nex != point_pre:
                        rad = Point.get_radians(point_pre, point_cur, point_nex)
                        if rad > max_radians:
                            max_radians = rad
                            target = point_nex

                point_pre = point_cur
                point_cur = target
                self.Point_list.remove(target)
                self.add_Line(Line(point_pre, point_cur))

        self.all_input_enable()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = main_gui()
    sys.exit(app.exec_())
