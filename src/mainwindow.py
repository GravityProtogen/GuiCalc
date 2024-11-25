from typing import TYPE_CHECKING
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton,QGridLayout
from PySide6.QtCore import Qt, Slot
from utils import *
from styles import *
if TYPE_CHECKING:
    from mainwindow import Display,Info


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configurando o layout básico
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        # Título da janela
        self.setWindowTitle('Calculadora')

    def adjustFixedSize(self):
        # Última coisa a ser feita
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
        
        
# Parte da tela que mostra os numeros digitados em cimazinho
class Info(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.configStyle()
    def configStyle(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)

# Parte de input da tela
class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size:{MEDIUM_FONT_SIZE}px')
        self.setMinimumHeight(MEDIUM_FONT_SIZE * 2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)
        self.setMinimumWidth(MINIMUN_WIDTH)


# Botões
class Button(QPushButton):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.configStyle()
    
    def configStyle(self):
        # Fonte
        font = self.font()
        font.setPixelSize(SMALL_FONT_SIZE)
        font.setBold(True)
        self.setFont(font)
        self.setMinimumSize(45, 45)

class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info : 'Info', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self.equation = ''
        self._makeGrid()
        
        @property
        def equation(self):
            return self._equation
        @equation.setter
        def equation(self, value):
            self._equation = value
            self.info.setText(value)
        
    def _makeGrid(self):
        for numero_linha, row in enumerate(self._grid_mask):
            for numero_coluna, button_text in enumerate(row):
                button = Button(button_text)
                
                if not eNumouDot(button_text) and not len(button_text) == 0:
                    button.setProperty('cssClass','specialButton')
                
                self.addWidget(button, numero_linha, numero_coluna)
                buttonSlot = self._ButtonDisplayConnection(
                    self._ButtonTextToDisplay,
                    button,
                    
                    )
                button.clicked.connect(buttonSlot)
                
    def _ButtonDisplayConnection(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot
    
    def _ButtonTextToDisplay(self, button):
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText
        if not eNumeroValido(newDisplayValue):
            return
        self.display.insert(buttonText)