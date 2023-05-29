# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QToolBar, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(791, 535)
        self.actionzoom = QAction(MainWindow)
        self.actionzoom.setObjectName(u"actionzoom")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.open_folder = QPushButton(self.groupBox_2)
        self.open_folder.setObjectName(u"open_folder")
        self.open_folder.setGeometry(QRect(0, 20, 80, 24))
        self.qlist_images = QListWidget(self.groupBox_2)
        self.qlist_images.setObjectName(u"qlist_images")
        self.qlist_images.setGeometry(QRect(0, 47, 81, 531))
        self.qlist_images.setStyleSheet(u"background-color:white")
        self.qlist_images.setFrameShape(QFrame.Box)
        self.qlist_images.setFrameShadow(QFrame.Plain)
        self.qlist_images.setLayoutMode(QListView.Batched)
        self.qlist_images.setBatchSize(20)

        self.horizontalLayout.addWidget(self.groupBox_2)

        self.qlabel_image = QLabel(self.centralwidget)
        self.qlabel_image.setObjectName(u"qlabel_image")
        self.qlabel_image.setScaledContents(True)

        self.horizontalLayout.addWidget(self.qlabel_image)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ZoomIn = QPushButton(self.groupBox)
        self.ZoomIn.setObjectName(u"ZoomIn")

        self.verticalLayout_2.addWidget(self.ZoomIn)

        self.ZoomOut = QPushButton(self.groupBox)
        self.ZoomOut.setObjectName(u"ZoomOut")

        self.verticalLayout_2.addWidget(self.ZoomOut)

        self.toggle_move = QToolButton(self.groupBox)
        self.toggle_move.setObjectName(u"toggle_move")
        self.toggle_move.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggle_move.setAutoFillBackground(False)
        self.toggle_move.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"../../../Downloads/icons/move.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toggle_move.setIcon(icon)
        self.toggle_move.setIconSize(QSize(20, 20))
        self.toggle_move.setCheckable(True)
        self.toggle_move.setChecked(True)
        self.toggle_move.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toggle_move.setAutoRaise(False)

        self.verticalLayout_2.addWidget(self.toggle_move)


        self.horizontalLayout.addWidget(self.groupBox)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 10)
        self.horizontalLayout.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 791, 21))
        self.menufile = QMenu(self.menubar)
        self.menufile.setObjectName(u"menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(MainWindow)
        self.qlist_images.itemClicked.connect(MainWindow.item_click)
        self.open_folder.clicked.connect(MainWindow.selectDir)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionzoom.setText(QCoreApplication.translate("MainWindow", u"zoom ", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.open_folder.setText(QCoreApplication.translate("MainWindow", u"Open Folder", None))
        self.qlabel_image.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.ZoomIn.setText(QCoreApplication.translate("MainWindow", u"Zoom In", None))
        self.ZoomOut.setText(QCoreApplication.translate("MainWindow", u"Zoom Out", None))
#if QT_CONFIG(tooltip)
        self.toggle_move.setToolTip(QCoreApplication.translate("MainWindow", u"Move Image", None))
#endif // QT_CONFIG(tooltip)
        self.toggle_move.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.menufile.setTitle(QCoreApplication.translate("MainWindow", u"file ", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

