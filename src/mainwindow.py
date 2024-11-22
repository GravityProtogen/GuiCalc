from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget


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

    def addToVLayout(self, widget: QWidget):
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
        self.setStyleSheet(f'font-size:{BIG_FONT_SIZE}px')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
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
        font.setPixelSize(MEDIUM_FONT_SIZE)
        font.setBold(True)
        self.setFont(font)
        self.setMinimumSize(75, 75)
        self.setProperty('cssClass','specialButton')