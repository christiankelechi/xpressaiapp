from PyQt6.QtWidgets import (
    QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton,
    QApplication, QFrame, QLineEdit, QToolButton, QSizePolicy, QSpacerItem
)
from PyQt6.QtGui import QPixmap, QFont, QIcon
from PyQt6.QtCore import Qt
import sys

class SignupView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Signup View")
        self.setStyleSheet("background:black;")

        # === Logo + Text Layout ===
        title_layout = QHBoxLayout()
        logo_label = QLabel()
        pixmap = QPixmap("xpressaiapp/images/app_logo.png").scaled(
            68, 70, Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        logo_label.setPixmap(pixmap)

        text_label = QLabel("press AI")
        text_label.setStyleSheet("color: white;")
        text_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))

        title_layout.addWidget(logo_label)
        title_layout.addWidget(text_label)
        title_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # === Google Button ===
        google_button = self.create_google_button()

        # === Horizontal Line ===
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFixedWidth(400)
        line.setFixedHeight(1)
        line.setStyleSheet("color: #F3F3F380;")

        # === Input Fields (label + input vertically) ===
        form_layout = QVBoxLayout()
        form_layout.setSpacing(20)

        # Create each input group and add it to form_layout
        form_layout.addLayout(self.create_input_group("Email", "Enter your email"))
        form_layout.addLayout(self.create_input_group("Enter Password", "Enter your password", is_password=True))
        form_layout.addLayout(self.create_input_group("Confirm New Password", "Re-enter your password", is_password=True))

        # === Main Layout ===
        main_layout = QVBoxLayout()
        main_layout.addLayout(title_layout)
        main_layout.addSpacing(40)
        main_layout.addWidget(google_button, alignment=Qt.AlignmentFlag.AlignHCenter)
        main_layout.addSpacing(20)
        main_layout.addWidget(line, alignment=Qt.AlignmentFlag.AlignHCenter)
        main_layout.addSpacing(30)
        main_layout.addLayout(form_layout)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        # Bottom layout container with fixed width 400 (like inputs)
        bottom_container = QWidget()
        bottom_container.setFixedWidth(400)
        bottom_layout = QHBoxLayout(bottom_container)
        bottom_layout.setContentsMargins(0, 0, 0, 0)  # no margins inside container

        already_label = QLabel("Already have an account?")
        already_label.setStyleSheet("color: white; font-size: 14px;")
        login_label = QLabel("Login")
        login_label.setStyleSheet("""
            color: #1a73e8;  /* blue login */
            font-weight: bold;
            font-size: 14px;
            cursor: pointer;
        """)

        bottom_layout.addWidget(already_label)
        bottom_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        bottom_layout.addWidget(login_label)

        # Add bottom container centered like the inputs
        main_layout.addWidget(bottom_container, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(main_layout)
        self.showMaximized()

    def create_google_button(self):
        button = QPushButton("Continue with Google")
        button.setFixedHeight(50)
        button.setFixedWidth(400)

        pixmap = QPixmap("xpressaiapp/images/google_icon.png").scaled(
            20, 20, Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        button.setIcon(QIcon(pixmap))
        button.setIconSize(pixmap.size())

        button.setStyleSheet("""
            QPushButton {
                background-color: black;
                border: 1px solid #F3F3F380;
                border-radius: 8px;
                color: white;
                font-size: 14px;
                padding-left: 10px;
                text-align: center;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.15);
            }
            QPushButton:pressed {
                background-color: rgba(255, 255, 255, 0.25);
            }
        """)
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        return button

    def create_label(self, text):
        label = QLabel(text)
        label.setStyleSheet("color: white; margin-left: 2px;")
        label.setFont(QFont("Arial", 12))
        label.setFixedWidth(400)  # same width as input for alignment
        label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        return label

    def create_input(self, placeholder, is_password=False):
        input_field = QLineEdit()
        input_field.setPlaceholderText(placeholder)
        input_field.setFixedWidth(400)
        input_field.setFixedHeight(40)
        input_field.setStyleSheet("""
            QLineEdit {
                background-color: #1e1e1e;
                color: white;
                border: 1px solid #F3F3F380;
                border-radius: 6px;
                padding-left: 8px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 1px solid white;
            }
        """)

        if is_password:
            input_field.setEchoMode(QLineEdit.EchoMode.Password)

        return input_field

    def create_input_group(self, label_text, placeholder, is_password=False):
        layout = QVBoxLayout()
        layout.setSpacing(5)
        layout.setContentsMargins(0, 0, 0, 0)

        label = self.create_label(label_text)
        if is_password:
            # Create password input with toggle button
            input_with_toggle = self.create_password_input(placeholder)
            layout.addWidget(label)
            layout.addWidget(input_with_toggle)
        else:
            input_field = self.create_input(placeholder)
            layout.addWidget(label)
            layout.addWidget(input_field)

        # Align to center horizontally with fixed width
        wrapper = QHBoxLayout()
        wrapper.addStretch()
        wrapper.addLayout(layout)
        wrapper.addStretch()
        return wrapper

    def create_password_input(self, placeholder):
        # Create a QWidget to hold the input and toggle button
        container_widget = QWidget()
        container_widget.setFixedWidth(400)
        container_widget.setFixedHeight(40)
        container_widget.setStyleSheet("background: transparent;")  # transparent container

        # Use absolute positioning to overlap toggle button on the right edge inside the container
        input_field = QLineEdit(container_widget)
        input_field.setPlaceholderText(placeholder)
        input_field.setEchoMode(QLineEdit.EchoMode.Password)
        input_field.setGeometry(0, 0, 400, 40)  # full width initially
        input_field.setStyleSheet("""
            QLineEdit {
                background-color: #1e1e1e;
                color: white;
                border: 1px solid #F3F3F380;
                border-radius: 6px;
                padding-left: 8px;
                font-size: 14px;
                padding-right: 40px;  /* reserve space for toggle button */
            }
            QLineEdit:focus {
                border: 1px solid white;
            }
        """)

        toggle_btn = QToolButton(container_widget)
        toggle_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        toggle_btn.setStyleSheet("""
            QToolButton {
                background: transparent;
                border: none;
            }
            QToolButton:hover {
                background-color: rgba(255, 255, 255, 0.15);
                border-radius: 6px;
            }
        """)
        toggle_btn.setIcon(QIcon("xpressaiapp/images/eye.png"))
        toggle_btn.setIconSize(QPixmap("xpressaiapp/images/eye.png").size())
        toggle_btn.setFixedSize(30, 30)
        # Position toggle button inside right edge, vertically centered
        toggle_btn.move(container_widget.width() - toggle_btn.width() - 5, (container_widget.height() - toggle_btn.height()) // 2)

        def toggle_password():
            if input_field.echoMode() == QLineEdit.EchoMode.Password:
                input_field.setEchoMode(QLineEdit.EchoMode.Normal)
                toggle_btn.setIcon(QIcon("xpressaiapp/images/eye_closed.png"))
            else:
                input_field.setEchoMode(QLineEdit.EchoMode.Password)
                toggle_btn.setIcon(QIcon("xpressaiapp/images/eye.png"))

        toggle_btn.clicked.connect(toggle_password)

        return container_widget


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SignupView()
    sys.exit(app.exec())
