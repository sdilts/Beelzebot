#!/usr/bin/python3

from character import Character
import server
import queue
import client
import sys
import board
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMainWindow, QLabel
import PyQt5.QtGui as QtGui
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import QtGui, QtCore
from bodyControl import *
import traceback

class GameThread(QtCore.QThread):

    def __init__(self, bot,board, ipAddr, portNum):
        # super(Threading, self).__init__()
        QtCore.QThread.__init__(self)
        self.bot = bot
        self.board = board
        self.ipAddr = ipAddr
        self.portNum = portNum

    def run(self):
        self.run_game()
        self.quit()
        self.terminate()

    def run_game(self):
        # bot = Character(ipAddr, portNum, b, controller)
        try:
            while (not self.board.at_end(self.bot.position)) and self.bot.isAlive():
                # if not self.queue.empty():
                #     print("Quiting the game")
                #     raise Exception
                self.bot.take_turn()
                self.board.print_stats()
            if not self.bot.isAlive():
                print("Done!")
                client.say_phrase(self.ipAddr, self.portNum, "Better luck next time!", False)
            else:
                client.say_phrase(self.ipAddr, self.portNum, "We are victorious!", False)

            if server.wait_for_command.server:
                server.wait_for_command.server.stop()
        except Exception as e:
            traceback.print_exc()
            if server.wait_for_command.server:
                server.wait_for_command.server.stop()

class Display_game(QMainWindow):

    image_size = 480
    end_signal = pyqtSignal(name='end_signal')

    def __init__(self, ipAddr, portNum, parent=None):
        QObject.__init__(self, parent)

        self.ipAddr = ipAddr
        self.portNum = portNum

        controller = RobotController()
        controller.reset_pos()
        self.b = board.Board()
        self.bot = Character(ipAddr, portNum, self.b, controller, self)
        self.bot.changed_location.connect(self.change_picture)

        self.startButton = QPushButton("Start the game!")
        self.startButton.clicked.connect(self.start_playing)

        self.endButton = QPushButton("End the game!")
        self.endButton.clicked.connect(self.end_game)

        self.image_label = QLabel(self)
        pixmap = QtGui.QPixmap("gui_images/entrance.jpg")
        pixmap = pixmap.scaled(self.image_size,self.image_size, PyQt5.QtCore.Qt.KeepAspectRatio)
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(PyQt5.QtCore.Qt.AlignCenter)

        # main layout
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.image_label)
        self.mainLayout.addWidget(self.startButton)
        self.mainLayout.addWidget(self.endButton)

        # central widget
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.mainLayout)

        # set central widget
        self.setCentralWidget(self.centralWidget)

    def end_game(self):
        self.showNormal()
        print("Ending game")

    def start_playing(self):
        self.thread = GameThread(self.bot, self.b, self.ipAddr, self.portNum)
        self.thread.start()

    def change_picture(self, new_location):
        print("********************************")
        print("Location changed to:", new_location)
        print("********************************")
        if new_location == board.Location_types.START:
            pixmap = QtGui.QPixmap("gui_images/entrance.jpg")
        elif new_location == board.Location_types.END:
            pixmap = QtGui.QPixmap("gui_images/the_end.png")
        elif new_location == board.Location_types.RECHARGE:
            pixmap = QtGui.QPixmap("gui_images/recharging.jpg")
        elif new_location == board.Location_types.COFFEE:
            pixmap = QtGui.QPixmap("gui_images/coffee_shop.png")
        elif new_location == board.Location_types.EASY:
            pixmap = QtGui.QPixmap("gui_images/blob_monster.png")
        elif new_location == board.Location_types.MED:
            pixmap = QtGui.QPixmap("gui_images/goblin.png")
        elif new_location == board.Location_types.DIFFICULT:
            pixmap = QtGui.QPixmap("gui_images/monster.png")
        elif new_location == board.Location_types.FUN:
            pixmap = QtGui.QPixmap("gui_images/eyes.jpg")

        pixmap = pixmap.scaled(self.image_size,self.image_size, PyQt5.QtCore.Qt.KeepAspectRatio)
        self.image_label.setPixmap(pixmap)
        self.image_label.repaint()



if __name__ == "__main__":
    # run_game(sys.argv[1], sys.argv[2])
    app = QApplication(sys.argv)
    myWidget = Display_game("10.152.166.102", 5015)
    myWidget.showFullScreen()
    app.exec_()
