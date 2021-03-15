import sys
from PyQt5 import QtWidgets, QtCore
import design
import settings
import subprocess
import time

class settingsDialog(settings.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mp = self.mediaPlayer.currentText()
        self.mediaPlayer.currentTextChanged.connect(self.changeText)
        self.buttonBox.accepted.connect(self.fileWrite)
        
    def fileWrite(self):
        config = open("settings.conf", "w")
        config.write(f"mp:{self.mp}")
        config.close()
        
    def changeText(self):
        self.mp = self.mediaPlayer.currentText()


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
        self.youtubeView.urlChanged.connect(self.tryToOpenMP)
        self.settings.clicked.connect(self.showSettings)
        
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
        
    def tryToOpenMP(self):
        pageUrl = str(self.youtubeView.url())
        pageUrl = pageUrl.replace('PyQt5.QtCore.QUrl', '').replace('(', '').replace("'", '').replace(")", '')
        if "youtube.com" not in pageUrl:
            self.youtubeView.setUrl(QtCore.QUrl("https://youtube.com/"))
        elif "youtube.com/watch?v=" in pageUrl:
            mp = open("settings.conf", "r")
            for item in mp:
                if "mp:" in item:
                    player = item.replace("mp:", "")
                    if player == "VLC":
                        subprocess.Popen(["vlc", pageUrl])
                        time.sleep(3)
                        self.youtubeView.back()
                    elif player == "mpv":
                        subprocess.Popen(["mpv", pageUrl])
                        time.sleep(3)
                        self.youtubeView.back()
            mp.close()
            
    def showSettings(self):
        self.dialog = settingsDialog()
        self.dialog.show()


app = QtWidgets.QApplication(sys.argv)

my_mainWindow = MainWindow()
my_mainWindow.show()

sys.exit(app.exec_())
