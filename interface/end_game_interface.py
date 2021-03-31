from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton

from interface.style import Style


class EndGameInterFace(QMainWindow):
    def __init__(self, parent, signal, points_black, points_white):
        super(EndGameInterFace, self).__init__(parent)
        self.setFixedSize(850, 700)
        self.points_black = points_black
        self.points_white = points_white
        self.style = Style()
        self.signal = signal
        self.winner_points = 0
        self.winner = "draw"
        self.draw_button()
        self.get_winner()
        self.draw_winner()

    def get_winner(self):
        if self.points_black > self.points_white:
            self.winner = "Black"
            self.winner_points = str(self.points_black)
        elif self.points_white > self.points_black:
            self.winner = "White"
            self.winner_points = str(self.points_white)
        else:
            self.winner_points = str(self.points_black)

    def draw_winner(self):
        if self.winner == "draw":
            winner_text = "No winners"
        else:
            winner_text = f"Winner: {self.winner}"
        winner_label = QLabel(winner_text, self)
        winner_score = QLabel(f"Score: {self.winner_points}", self)
        winner_label.setStyleSheet(self.style.stylesheet_game_end)
        winner_score.setStyleSheet(self.style.stylesheet_score_end)

        winner_label.move(180, 190)
        winner_label.resize(500, 60)
        winner_score.move(180, 250)
        winner_score.resize(500, 60)

    def draw_button(self):
        self.button_1 = QPushButton("Play again", self)
        self.button_1.setStyleSheet(self.style.stylesheet_button)
        self.button_1.clicked.connect(self.restart_game)
        self.button_1.move(180, 405)
        self.button_1.setFixedSize(500, 50)

        self.button_2 = QPushButton("Exit", self)
        self.button_2.setStyleSheet(self.style.stylesheet_button)
        self.button_2.clicked.connect(self.close_game)

        self.button_2.move(180, 475)
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
