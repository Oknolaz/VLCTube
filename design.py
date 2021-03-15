# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vlc.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(727, 519)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("yt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setText("")
        icon = QtGui.QIcon.fromTheme("back")
        self.back.setIcon(icon)
        self.back.setObjectName("back")
        self.horizontalLayout.addWidget(self.back)
        self.forward = QtWidgets.QPushButton(self.centralwidget)
        self.forward.setText("")
        icon = QtGui.QIcon.fromTheme("next")
        self.forward.setIcon(icon)
        self.forward.setObjectName("forward")
        self.horizontalLayout.addWidget(self.forward)
        self.home = QtWidgets.QPushButton(self.centralwidget)
        self.home.setText("")
        icon = QtGui.QIcon.fromTheme("user-home")
        self.home.setIcon(icon)
        self.home.setObjectName("home")
        self.horizontalLayout.addWidget(self.home)
        self.reload = QtWidgets.QPushButton(self.centralwidget)
        self.reload.setText("")
        icon = QtGui.QIcon.fromTheme("reload")
        self.reload.setIcon(icon)
        self.reload.setObjectName("reload")
        self.horizontalLayout.addWidget(self.reload)
        spacerItem = QtWidgets.QSpacerItem(468, 18, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.settings = QtWidgets.QPushButton(self.centralwidget)
        self.settings.setText("")
        icon = QtGui.QIcon.fromTheme("settings")
        self.settings.setIcon(icon)
        self.settings.setObjectName("settings")
        self.horizontalLayout.addWidget(self.settings)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.youtubeView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.youtubeView.setUrl(QtCore.QUrl("https://www.youtube.com/"))
        self.youtubeView.setObjectName("youtubeView")
        self.verticalLayout.addWidget(self.youtubeView)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VLCTube"))
from PyQt5 import QtWebEngineWidgets
