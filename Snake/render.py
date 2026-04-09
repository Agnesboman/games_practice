import sys
from PySide6.QtWidgets import (
    QGraphicsScene, QGraphicsView,
    QGraphicsRectItem, QApplication
)
from PySide6.QtGui import QBrush, QPen
from PySide6.QtCore import Qt
from shapeFactory import shape


class View:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.app = QApplication(sys.argv)
        self.scene = QGraphicsScene(0, 0, self.width, self.height)
        self.view = QGraphicsView(self.scene)

    def startView(self):
        #graphics
        rect_obj = shape(200, 50, 0, 0)
        rect = rect_obj.rectangle(Qt.red, Qt.black, 3)

        self.scene.addItem(rect)
        self.view.show()

        return self.app.exec()

    def gameView(self):
        self.view.show()
        return self.app.exec()

    def gameOverView(self):
        self.scene.clear()
        self.scene.addText("Game Over")
        self.view.show()
        return self.app.exec()


# Run
if __name__ == "__main__":
    v = View(200, 5000)
    v.startView()