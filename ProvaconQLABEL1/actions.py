# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass


from PySide6.QtGui import QImage, QPixmap, QPainter, QTransform
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QPoint


class ImageViewer:
    ''' Basic image viewer class to show an image with zoom and pan functionaities.
        Requirement: Qt's Qlabel widget name where the image will be drawn/displayed.
    '''
    def __init__(self, qlabel):
        self.qlabel_image = qlabel                            # widget/window name where image is displayed (I'm usiing qlabel)
        self.qimage_scaled = QImage()                         # scaled image to fit to the size of qlabel_image
        self.qpixmap = QPixmap()                              # qpixmap to fill the qlabel_image

        self.zoomX = 1              # zoom factor w.r.t size of qlabel_image
        self.anchor = QPoint(0, 0)
        self.position = QPoint(0, 0) # position of top left corner of qimage_label w.r.t. qimage_scaled
        self.panFlag = False # to enable or disable pan
        self.pressed = None
        self.last_position=QPoint()
        self.qlabel_image.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.__connectEvents()

    def __connectEvents(self):
        # Mouse events
        self.qlabel_image.mousePressEvent = self.mousePressAction
        self.qlabel_image.mouseMoveEvent = self.mouseMoveAction
        self.qlabel_image.mouseReleaseEvent = self.mouseReleaseAction

    def onResize(self):
        ''' things to do when qlabel_image is resized '''
        self.qpixmap = QPixmap(self.qlabel_image.size())
        #self.qpixmap.fill(QtCore.Qt.black)
        self.qimage_scaled = self.qimage.scaled(self.qlabel_image.width() * self.zoomX, self.qlabel_image.height() * self.zoomX, QtCore.Qt.KeepAspectRatioByExpanding)
        #self.qpixmap_scaled = QPixmap(self.qimage_scaled
        self.update()
        #self.qlabel_image.setPixmap(self.qpixmap_scaled)


    def loadImage(self, imagePath):
        print('b')
        ''' To load and display new image.'''
        self.qimage = QImage(imagePath)
        #self.qpixmap = QPixmap(self.qimage)
        #self.qpixmap = QPixmap(self.qlabel_image.size())
        #self.qlabel_image.setPixmap(self.qpixmap)
        self.qlabel_image.setPixmap(QtGui.QPixmap.fromImage(self.qimage))
        if not self.qimage.isNull():
            # reset Zoom factor and Pan position
            self.zoomX = 1
            self.position = [0, 0]
            self.qimage_scaled = self.qimage.scaled(self.qlabel_image.width(), self.qlabel_image.height(), QtCore.Qt.KeepAspectRatioByExpanding)

            #self.update()
        else:
            self.statusbar.showMessage('Cannot open this image! Try another one.', 5000)


    """def update(self):
        ''' This function actually draws the scaled image to the qlabel_image.
            It will be repeatedly called when zooming or panning.
            So, I tried to include only the necessary operations required just for these tasks.
        '''
        if not self.qimage_scaled.isNull():
            #check if position is within limits to prevent unbounded panning.
            px, py = self.position
            px = px if (px <= self.qimage_scaled.width() - self.qlabel_image.width()) else (self.qimage_scaled.width() - self.qlabel_image.width())
            py = py if (py <= self.qimage_scaled.height() - self.qlabel_image.height()) else (self.qimage_scaled.height() - self.qlabel_image.height())
            px = px if (px >= 0) else 0
            py = py if (py >= 0) else 0
            self.position = (px, py)

            if self.zoomX == 1:
                self.qpixmap.fill(QtCore.Qt.white)

            #the act of painting the qpixamp
            painter = QPainter()
            painter.begin(self.qpixmap)
            painter.drawImage(QtCore.QPoint(0, 0), self.qimage_scaled,
                   QtCore.QRect(self.position[0], self.position[1], self.qlabel_image.width(), self.qlabel_image.height()) )
            painter.end()

            self.qlabel_image.setPixmap(self.qpixmap)
        else:
            pass"""

    def update(self):
        if not self.qimage_scaled.isNull():
            # Calculate the scaled size based on zoom factor
            scaled_width = self.qimage.width() * self.zoomX
            scaled_height = self.qimage.height() * self.zoomX

            # Calculate the center position of the scaled image
            center_x = scaled_width / 2
            center_y = scaled_height / 2

            # Calculate the top-left position for drawing the cropped image
            top_left_x = center_x - self.qlabel_image.width() / 2
            top_left_y = center_y - self.qlabel_image.height() / 2

            # Crop the image based on the top-left position and label size
            cropped_image = self.qimage.scaled(scaled_width, scaled_height).copy(
                int(top_left_x), int(top_left_y), self.qlabel_image.width(), self.qlabel_image.height()
            )

            # Display the cropped image
            self.qlabel_image.setPixmap(QPixmap.fromImage(cropped_image))
        else:
            pass



    def zoomIn(self):
        self.zoomX *=2
        self.onResize()

    def zoomOut(self):
        self.zoomX /= 2
        self.onResize()


    def mousePressAction(self, event):
        #print(x,y)
        if event.button() == Qt.LeftButton and self.panFlag:
            self.pressed = event.position()    # starting point of drag vector
            self.anchor = self.pressed        # save the pan position when panning starts

    def mouseMoveAction(self, event):
        x, y = event.pos().x(), event.pos().y()
        if self.pressed:
            dx, dy = x - self.pressed.x(), y - self.pressed.y()         # calculate the drag vector
            self.position = self.anchor[0] - dx, self.anchor[1] - dy    # update pan position using drag vector
            self.update()                                               # show the image with udated pan position

    def mouseReleaseAction(self, QMouseEvent):
        self.pressed = None                                             # clear the starting point of drag vector



    """def resetZoom(self):
        self.zoomX = 1
        self.position = [0, 0]
        self.qimage_scaled = self.qimage.scaled(self.qlabel_image.width() * self.zoomX, self.qlabel_image.height() * self.zoomX, QtCore.Qt.KeepAspectRatio)
        self.update() """

    def enablePan(self, value):
        self.panFlag = value
