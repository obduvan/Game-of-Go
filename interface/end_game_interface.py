from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton

from interface.style import Style


class EndGameInterFace(QMainWindow):
    def __init__(self, parent, signal):
        super(EndGameInterFace, self).__init__(parent)
        self.setFixedSize(600, 500)
        self.style = Style()
        self.signal = signal
        self.draw_label()
        self.draw_button()

    def draw_label(self):
        self.score_label = QLabel("The End ", self)
        self.score_label.setStyleSheet(self.style.stylesheet_game_end)
        self.score_label.move(170, 60)
        self.score_label.resize(500, 60)

    def draw_button(self):
        self.button_1 = QPushButton("Play again", self)
        self.button_1.setStyleSheet(self.style.stylesheet_button)
        self.button_1.clicked.connect(self.restart_game)
        self.button_1.move(50, 290)
        self.button_1.setFixedSize(500, 50)

        self.button_2 = QPushButton("Exit", self)
        self.button_2.setStyleSheet(self.style.stylesheet_button)
        self.button_2.clicked.connect(self.close_game)

        self.button_2.move(50, 360)
        self.button_2.setFixedSize(500, 50)

    def close_this(self):
        self.close()

    def restart_game(self):
        self.close_this()
        self.signal.restart_signal.emit()

    def close_game(self):
        self.close_this()
        self.signal.closed_signal.emit()

    def closeEvent(self, event):
        self.signal.closed_signal.emit()
