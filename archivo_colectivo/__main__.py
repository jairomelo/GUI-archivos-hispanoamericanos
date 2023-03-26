import sys

from ui import App
from __version__ import __version__

def iniciar_interfaz():
    """ Inicia la interfaz de usuario """
    app = App()
    sys.excepthook = app.mostrar_errores
    app.mainloop()

if __name__ == '__main__':
    iniciar_interfaz()