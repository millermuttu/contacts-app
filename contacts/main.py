import sys
from PyQt5.QtWidgets import QApplication

from .views import Window
from .database import createConnection


def main():
    # create the application
    app = QApplication(sys.argv)
    # Connect to the database before creating any window
    if not createConnection("contacts.sqlite"):
        sys.exit(1)
    win = Window()
    win.show()
    # Run the event loop
    sys.exit(app.exec())
