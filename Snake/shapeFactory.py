import sys
from PySide6.QtWidgets import (
    QGraphicsScene, QGraphicsView,
    QGraphicsRectItem, QApplication
)
from PySide6.QtGui import QBrush, QPen
from PySide6.QtCore import Qt

class shape: 
    def __init__(self, height, width, x_pos, y_pos):
        self.height = height
        self.width = width
        self.x_pos = x_pos
        self.y_pos = y_pos

    def rectangle(self, colour, b_colour, pen_w):
        rect = QGraphicsRectItem(0, 0, self.height, self.width)
        rect.setPos(self.x_pos, self.y_pos)
        rect.setBrush(QBrush(colour))
        pen = QPen(b_colour)
        pen.setWidth(pen_w)
        rect.setPen(pen)
        
        return rect