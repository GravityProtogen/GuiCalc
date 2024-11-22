import sys
 
from display import Display
from info import Info
from mainwindow import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme
from variables import WINDOW_ICON_PATH

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
    info = Info('242.3 ^ 12.45' )
    window.addToVLayout(info)    
    
    # Configuração para o icon aparecer na taskbar do Windows
    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            u'CompanyName.ProductName.SubProduct.VersionInformation')

    # Display
    display = Display()
    window.addToVLayout(display)


    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()