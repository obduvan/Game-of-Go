from PyQt5.QtWidgets import QWidget


class Style(QWidget):
    def __init__(self):
        super(Style, self).__init__()
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
                color: #FFB433;
                font-size: 22px;
                font-weight: bold;              
            }
        """

        self.stylesheet_gamers = """   
            QLabel
            {   
                font: Lucida Console;
                color: #FFFFF;
                font-size: 22px;
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
                       font-size: 70px;
                       font-weight: bold;
                   }
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
            QPushButton:!hover { background-color: #786E7D   }
            QPushButton:pressed { background-color: #C6C5C6 }
            """
