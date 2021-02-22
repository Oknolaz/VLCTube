import sys
from PyQt5 import QtWidgets, QtCore
import design
import subprocess
import time

class MainWindow(design.Ui_MainWindow, QtWidgets.QMainWindow, QtCore.QUrl):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.progressBar.hide()
        self.youtubeView.setFocus()
        self.youtubeView.loadStarted.connect(self.LoadProgress)
        self.back.clicked.connect(self.backPage)
        self.forward.clicked.connect(self.forwardPage)
        self.home.clicked.connect(self.goHome)
        self.reload.clicked.connect(self.reloadPage)
        self.youtubeView.urlChanged.connect(self.tryToOpenVLC)
        
    def LoadProgress(self):
        self.progressBar.show()
        self.youtubeView.loadProgress.connect(self.progressBar.setValue)
        self.youtubeView.loadFinished.connect(self.progressBar.hide)

    def backPage(self):
        self.youtubeView.back()
        
    def forwardPage(self):
        self.youtubeView.forward()
        
    def goHome(self):
        self.youtubeView.setUrl(QtCore.QUrl("https://youtube.com/"))
        
    def reloadPage(self):
        self.youtubeView.reload()
        
    def tryToOpenVLC(self):
        pageUrl = str(self.youtubeView.url())
        pageUrl = pageUrl.replace('PyQt5.QtCore.QUrl', '').replace('(', '').replace("'", '').replace(")", '')
        if "youtube.com" not in pageUrl:
            self.youtubeView.setUrl(QtCore.QUrl("https://youtube.com/"))
        elif "youtube.com/watch?v=" in pageUrl:
            subprocess.Popen(["vlc", pageUrl])
            time.sleep(3)
            self.youtubeView.back()


app = QtWidgets.QApplication(sys.argv)

my_mainWindow = MainWindow()
my_mainWindow.show()

sys.exit(app.exec_())
