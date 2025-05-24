from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QApplication
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

class SignupView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Signup View")
        self.setStyleSheet("background:black")

        # === Create horizontal layout for logo + text ===
        title_layout = QHBoxLayout()

        # Logo QLabel
        logo_label = QLabel()
        pixmap = QPixmap("xpressaiapp/images/app_logo.png").scaled(
            68, 70, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation
        )
        logo_label.setPixmap(pixmap)

        # Text QLabel
        text_label = QLabel("press AI")
        text_label.setStyleSheet("color: white;")  
        text_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))

        # Add both to title layout
        title_layout.addWidget(logo_label)
        title_layout.addWidget(text_label)
        title_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # === Combine into a vertical layout ===
        main_layout = QVBoxLayout()
        main_layout.addLayout(title_layout)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setLayout(main_layout)
        self.showMaximized()
