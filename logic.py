from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    MIN_VOL = 0
    MAX_VOL = 3
    MIN_CHN = 0
    MAX_CHN = 4

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.status = False
        self.muted = False
        self.channel = Logic.MIN_CHN
        self.volume = Logic.MIN_VOL

        self.power_button.clicked.connect(lambda: self.power())
        self.channelup_button.clicked.connect(lambda: self.channel_up())
        self.channeldown_button.clicked.connect(lambda: self.channel_down())
        self.volumeup_button.clicked.connect(lambda: self.volume_up())
        self.volumedown_channel.clicked.connect(lambda: self.volume_down())
        self.mute_button.clicked.connect(lambda: self.mute())

    def power(self):
        if self.status:
            self.status = False
            self.channel_image.setPixmap(QtGui.QPixmap("off_image.webp"))
            self.channel_output.clear()
            self.volume_output.clear()
        else:
            self.status = True
            self.channel = Logic.MIN_CHN + 1
            self.channel_image.setPixmap(QtGui.QPixmap("cnn_image.jpg"))
            self.channel_output.setText(str(self.channel))
            self.volume_output.setPixmap(QtGui.QPixmap("unmute_image.png"))

    def channel_up(self):
        if self.status:
            channel_images = ["cnn_image.jpg", "espn_image.webp",
                              "disney_image.jpg", "hbo_image.jpg"]
            self.channel += 1
            if self.channel > Logic.MAX_CHN:
                self.channel = Logic.MIN_CHN + 1
            self.channel_image.setPixmap(QtGui.QPixmap(channel_images[self.channel - 1]))
            self.channel_output.setText(str(self.channel))

    def channel_down(self):
        if self.status:
            channel_images = ["cnn_image.jpg", "espn_image.webp",
                              "disney_image.jpg", "hbo_image.jpg"]
            self.channel -= 1
            if self.channel < Logic.MIN_CHN + 1:
                self.channel = Logic.MAX_CHN
            self.channel_image.setPixmap(QtGui.QPixmap(channel_images[self.channel - 1]))
            self.channel_output.setText(str(self.channel))

    def mute(self):
       if self.status:
           if not self.muted:
               self.muted = True
               self.volume_output.setPixmap(QtGui.QPixmap("mute_image.png"))
           else:
               self.muted = False
               self.volume = self.MIN_VOL
               self.volume_output.setPixmap(QtGui.QPixmap("unmute_image.png"))

    def volume_up(self):
        if self.status:
            volume_images = ["vol1_image.png", "vol2_image.png",
                             "vol3_image.png"]
            self.muted = False
            self.volume += 1
            if self.volume > Logic.MAX_VOL:
                self.volume = Logic.MIN_VOL + 1
            self.volume_output.setPixmap(QtGui.QPixmap(volume_images[self.volume - 1]))

    def volume_down(self):
        if self.status:
            volume_images = ["vol1_image.png", "vol2_image.png",
                             "vol3_image.png"]
            self.muted = False
            self.volume -= 1
            if self.volume < Logic.MIN_VOL + 1:
                self.volume = Logic.MAX_VOL
            self.volume_output.setPixmap(QtGui.QPixmap(volume_images[self.volume - 1]))