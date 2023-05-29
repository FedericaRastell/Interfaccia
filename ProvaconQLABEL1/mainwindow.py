# This Python file uses the following encoding: utf-8
import sys,os

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Qt, QPoint
from actions import ImageViewer
from ui_form import Ui_MainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

def getImages(folder):
    ''' Get the names and paths of all the images in a directory. '''
    image_list = []
    VALID_FORMAT = ('.BMP', '.GIF', '.JPG', '.JPEG', '.PNG', '.PBM', '.PGM', '.PPM', '.TIFF', '.XBM')  # Image formats supported by Qt
    if os.path.isdir(folder):
        for file in os.listdir(folder):
            if file.upper().endswith(VALID_FORMAT):
                #im_path = os.path.join(folder file)
                im_path = folder + '/'+ file
                image_obj = {'name': file, 'path': im_path }
                image_list.append(image_obj)
    print(image_list)
    return image_list
QtGui.QImageReader.setAllocationLimit(0)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.cntr, self.ui.numImages = -1, -1  # self.cntr have the info of which image is selected/displayed
        self.image_viewer = ImageViewer(self.ui.qlabel_image)
        #self.__connectEvents()
        self.showMaximized()


    def __connectEvents(self):
        #self.open_folder.clicked.connect(self.selectDir)
        #self.next_im.clicked.connect(self.nextImg)
        #self.prev_im.clicked.connect(self.prevImg)
        #self.ui.qlist_images.itemClicked.connect(self.item_click)
        # self.save_im.clicked.connect(self.saveImg)

        #self.ui.zoomIn.clicked.connect(self.image_viewer.zoomPlus)
        #self.ui.zoomOut.clicked.connect(self.image_viewer.zoomMinus)
        #self.reset_zoom.clicked.connect(self.image_viewer.resetZoom)
        self.qlabel_image.mousePressEvent.connect(self.image_viewer.mousePressAction)
        self.qlabel_image.mouseMoveEvent.connect(self.image_viewer.mouseMoveAction)
        self.qlabel_image.mouseReleaseEvent.connect(self.image_viewer.mouseReleaseAction)

        #self.toggle_line.toggled.connect(self.action_line)
        #self.toggle_rect.toggled.connect(self.action_rect)
        self.toggle_move.toggled.connect(self.action_move)

    def selectDir(self):
        ''' Select a directory, make list of images in it and display the first image in the list. '''
        # open 'select folder' dialog box
        self.folder = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
        if not self.folder:
            QtWidgets.QMessageBox.warning(self, 'No Folder Selected', 'Please select a valid Folder')
            return

        self.logs = getImages(self.folder)
        self.numImages = len(self.logs)
        print(f' found {self.numImages} images')

        # make qitems of the image names
        self.items = [QtWidgets.QListWidgetItem(log['name']) for log in self.logs]
        for item in self.items:
            self.ui.qlist_images.addItem(item)

        # display first image and enable Pan
        self.cntr=0
        #self.image_viewer.enablePan(True)
        self.image_viewer.loadImage(self.logs[self.cntr]['path'])
        self.items[self.cntr].setSelected(True)
        print(self.items[self.cntr])
        #self.ui.qlist_images.setItemSelected(self.items[self.cntr], True)

        # enable the next image button on the gui if multiple images are loaded
        #if self.numImages > 1:
        #    self.next_im.setEnabled(True)

    def resizeEvent(self, evt):
        if self.cntr >= 0:
            self.image_viewer.onResize()

    def wheelEvent(self, event):
        mouse = event.angleDelta().y()
        if mouse > 0:
            self.image_viewer.zoomIn()
        else:
            self.image_viewer.zoomOut()


    def item_click(self, item):
        self.cntr = self.items.index(item)
        print('a')
        print(f"path is {self.logs[self.cntr]['path']}")
        self.image_viewer.loadImage(self.logs[self.cntr]['path'])


    def action_move(self):
        if self.toggle_move.isChecked():
            self.ui.qlabel_image.setCursor(QtCore.Qt.OpenHandCursor)
            self.image_viewer.enablePan(True)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
