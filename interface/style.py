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
                font-size: 25px;
                font-weight: bold;              
            }
        """

        self.stylesheet_gamers = """   
            QLabel
            {   
                font: Lucida Console;
                color: #F7EDDC;
                font-size: 25px;
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

        self.stylesheet_score = """
            QLabel
            {
                font: Lucida Console;
                color: #392A30;
                font-size: 20px;
                font-weight: bold;       
            }
            """
