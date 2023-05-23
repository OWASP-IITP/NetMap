import client.environment # Fixes scaling issues on Windows
from PyQt5.QtWidgets import QApplication, QMainWindow, QOpenGLWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt

from OpenGL.GL import *
from OpenGL.GLU import *


class MyOpenGLWidget(QOpenGLWidget):
    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
    def resizeGL(self, w, h):
        pass


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("NetMap")
        self.resize(800, 600) 

        self.openGLWidget = MyOpenGLWidget(self)
        self.setCentralWidget(self.openGLWidget)
        

if __name__ == '__main__':
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()