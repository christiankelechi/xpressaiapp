import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt6.QtWidgets import QMainWindow,QLabel,QApplication
from xpressaiapp.screens.auth.signup import SignupView
import sys
# Test the widget
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SignupView()
    sys.exit(app.exec())