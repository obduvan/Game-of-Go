from PyQt5.QtWidgets import QWidget


class Style(QWidget):
    def __init__(self):
        super(Style, self).__init__()
        self.setWindowTitle("Game of Go")
        self.styles()

        self.draw_background()

    def draw_background(self):
        """Отрисовка заднего фона"""

        self.setStyleSheet("background-color:  #AEA5BA")

    def styles(self):
        """Стили программы"""

        self.stylesheet_gamers_run = """
            QLabel
            {
                font: Lucida Console;
                color: #F2E699;
                font-size: 22px;
                font-weight: bold;
            }
        """

        self.stylesheet_gamers = """
        QLabel
            {
                font: Lucida Console;
                color: #000000;
                font-size: 22px;
                font-weight: bold;
            }
        """

        self.stylesheet_time_label = """
            QLabel
            {
                font: Lucida Console;
                color: #1F1F2E;
                font-size: 30px;
                font-weight: bold;

            }
            """

        self.stylesheet_clock = """
                   QLabel
                   {
                       font: Lucida Console;
                       color: #1F1F2E;
                       font-size: 30px;
                       font-weight: bold;

                   }
                   """

        self.stylesheet = """
            QLabel
            {
                font: Lucida Console;
                color: #1F1F2E;
                font-size: 40px;
                font-weight: bold;

            }
            """

        self.stylesheet_forb_move = """
            QLabel
            {
                font: Lucida Console;
                color: #FFB433;
                font-size: 24px;
                font-weight: bold;
            }
            """

        self.stylesheet_score = """
            QLabel
            {
                font: Lucida Console;
                color: #392A30;
                font-size: 24px;
                font-weight: bold;
            }
            """

        self.stylesheet_game_end = """
                   QLabel
                   {
                       font: Lucida Console;
                       color: #282428;
                       font-size: 49px;
                       font-weight: bold;
                   }
                   """
        self.stylesheet_score_end = """
                          QLabel
                          {
                              font: Lucida Console;
                              color: #282428;
                              font-size: 30px;
                              font-weight: bold;
                          }
                          """

        self.stylesheet_line = """
                        QLineEdit
                        {
                            background-color: #817784;
                            border-style: outset;
                            min-height:1.2em;
                            border-radius: 10px;
                            border-color: beige;
                            font: bold 20px;
                            min-width: 3em;
                            padding: 6px;
                        }
                        """

        self.stylesheet_button_back = """
                    QPushButton
                    {
                        font: Gill Sans;
                        color: #191616;
                        font-size: 20px;
                        font-weight: bold;
                        border-radius: 7px;
                    }

                    QPushButton:hover { background-color: #9D92A1 }
                    QPushButton:!hover { background-color: #A687A8   }
                    QPushButton:pressed { background-color: #C6C5C6 }
                    """

        self.stylesheet_button = """
            QPushButton
            {
                font: Gill Sans;
                color: #191616;
                font-size: 20px;
                font-weight: bold;
                border-radius: 7px;
            }

            QPushButton:hover { background-color: #9D92A1 }
            QPushButton:!hover { background-color: #817784   }
            QPushButton:pressed { background-color: #C6C5C6 }
            """
