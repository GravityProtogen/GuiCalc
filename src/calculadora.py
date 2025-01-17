import sys


from mainwindow import MainWindow, ButtonsGrid, Display, Info
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme, WINDOW_ICON_PATH



if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()


    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    
    # Info
    info = Info('Sua Conta' )
    window.addWidgetToVLayout(info)    
    
    # Configuração para o icon aparecer na taskbar do Windows
    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            u'CompanyName.ProductName.SubProduct.VersionInformation')

    # Display
    display = Display()
    window.addWidgetToVLayout(display)
    
    # Grid e Botões
    buttonsGrid = ButtonsGrid(display, info)
    window.vLayout.addLayout(buttonsGrid)


    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()