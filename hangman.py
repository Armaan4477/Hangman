import sys
import random
import os
import base64
import json
from cryptography.fernet import Fernet
from PyQt6.QtGui import QImage, QPixmap, QBrush, QPalette, QIcon, QFont
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QMessageBox, QInputDialog, QRadioButton, QGridLayout, QMenuBar, QStatusBar
)
from PyQt6.QtCore import Qt
from firebase_admin import db, credentials, initialize_app
from PyQt6 import QtCore

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    path = os.path.join(base_path, relative_path)
    
    # Verify the file exists
    if not os.path.exists(path):
        print(f"Warning: Resource not found: {path}")
    
    return path

def get_firebase_credentials():
    try:
        machine_id = os.name + sys.platform
        key_material = machine_id.encode() + b'hangman_secure_key'
        import hashlib
        key_hash = hashlib.sha256(key_material).digest()
        key = base64.urlsafe_b64encode(key_hash[:32])

        encrypted_file_path = resource_path('encrypted_credentials.txt')
        if not os.path.exists(encrypted_file_path):
            raise FileNotFoundError(f"Credentials file not found: {encrypted_file_path}")
            
        with open(encrypted_file_path, 'rb') as f:
            encrypted_creds = f.read()
        
        cipher = Fernet(key)
        decrypted_data = cipher.decrypt(encrypted_creds)
        cred_data = json.loads(decrypted_data)
        return cred_data
    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
        print("Please run encrypt_credentials.py to generate the encrypted credentials file.")
        return None
    except Exception as e:
        print(f"Error decrypting credentials: {str(e)}")
        return None

class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        StartWindow.setObjectName("StartWindow")
        StartWindow.resize(400, 300)
        self.centralwidget = QWidget(StartWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_window = StartWindow

        self.background_image = QPixmap(resource_path("images/hangman_background.png"))
        palette = self.centralwidget.palette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(self.background_image.scaled(
            StartWindow.size(), Qt.AspectRatioMode.IgnoreAspectRatio)))
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setPalette(palette)

        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_name = QLabel("Enter your name:", self.centralwidget)
        self.verticalLayout.addWidget(self.label_name)

        self.textbox_name = QLineEdit(self.centralwidget)
        self.verticalLayout.addWidget(self.textbox_name)

        self.label_difficulty = QLabel("Select difficulty:", self.centralwidget)
        self.verticalLayout.addWidget(self.label_difficulty)

        self.radio_layout = QVBoxLayout()
        self.verticalLayout.addLayout(self.radio_layout)

        self.radio_easy = QRadioButton("Easy", self.centralwidget)
        self.radio_layout.addWidget(self.radio_easy)

        self.radio_medium = QRadioButton("Medium", self.centralwidget)
        self.radio_layout.addWidget(self.radio_medium)

        self.radio_hard = QRadioButton("Hard", self.centralwidget)
        self.radio_layout.addWidget(self.radio_hard)

        self.start_button = QPushButton("Start Game", self.centralwidget)
        self.verticalLayout.addWidget(self.start_button)

        self.start_button.clicked.connect(self.start_game)

        StartWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartWindow)
        StartWindow.resizeEvent = self.resizeEvent

    def retranslateUi(self, StartWindow):
        StartWindow.setWindowTitle("Hangman Game")
        self.start_button.setText("Start Game")

    def resizeEvent(self, event):
        palette = self.centralwidget.palette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(self.background_image.scaled(
            event.size(), Qt.AspectRatioMode.IgnoreAspectRatio)))
        self.centralwidget.setPalette(palette)

    def start_game(self):
        player_name = self.textbox_name.text()
        if not player_name:
            QMessageBox.warning(self.main_window, "Warning", "Please enter your name.")
            return

        if self.radio_easy.isChecked():
            difficulty = "easy"
        elif self.radio_medium.isChecked():
            difficulty = "medium"
        elif self.radio_hard.isChecked():
            difficulty = "hard"
        else:
            QMessageBox.warning(self.main_window, "Warning", "Please select a difficulty level.")
            return

        game_window = HangMan_GUI(player_name, difficulty)
        game_window.show()
        # Destroy the current window
        self.main_window.close()

class StartWindow(QMainWindow):
    def __init__(self, parent=None):
        super(StartWindow, self).__init__(parent)
        self.ui = Ui_StartWindow()
        self.ui.setupUi(self)

class Ui_HangMan(object):
    def setupUi(self, HangMan, player_name):
        HangMan.setObjectName("HangMan")
        HangMan.resize(1303, 700)
        self.centralwidget = QWidget(HangMan)
        self.centralwidget.setObjectName("centralwidget")

        # Update image path using resource_path
        self.background_image = QPixmap(resource_path("images/hangman_background_2.png"))
        palette = self.centralwidget.palette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(self.background_image.scaled(
            HangMan.size(), Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)))
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setPalette(palette)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        #Set geometry such that widgets start from top left and end at bottom right with 200px space at the bottom side
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1301, 671))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.textbox_word = QLineEdit(self.verticalLayoutWidget)
        self.textbox_word.setEnabled(False)
        self.textbox_word.setObjectName("textbox_word")
        self.verticalLayout.addWidget(self.textbox_word)

        self.button_layout = QHBoxLayout()
        self.button_layout.setObjectName("button_layout")

        self.buttons = {}

        self.button_grid_layout = QGridLayout()
        self.button_grid_layout.setObjectName("button_grid_layout")
        self.verticalLayout.addLayout(self.button_grid_layout)

        row = 0
        col = 0
        for letter in "abcdefghijklmnopqrstuvwxyz":
            button = QPushButton(letter)
            button.setObjectName(f"pushButton_{letter}")
            self.buttons[letter] = button
            self.button_grid_layout.addWidget(button, row, col)
            col += 1
            if col == 7:
                col = 0
                row += 1

        self.pushButton = QPushButton("Choose some other word")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton("Give up")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QLabel("Remaining Lives")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)

        self.textbox_lives = QLineEdit()
        self.textbox_lives.setEnabled(False)
        self.textbox_lives.setObjectName("textbox_lives")
        self.horizontalLayout_5.addWidget(self.textbox_lives)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.centralwidget.setLayout(self.verticalLayout)

        HangMan.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(HangMan)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1303, 30))
        self.menubar.setObjectName("menubar")
        HangMan.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(HangMan)
        self.statusbar.setObjectName("statusbar")
        HangMan.setStatusBar(self.statusbar)

        self.pushButton_add_word = QPushButton("Add word")
        self.pushButton_add_word.setObjectName("pushButton_add_word")
        self.verticalLayout.addWidget(self.pushButton_add_word)

        self.pushButton_remove_word = QPushButton("Remove Current word")
        self.pushButton_remove_word.setObjectName("pushButton_remove_word")
        self.verticalLayout.addWidget(self.pushButton_remove_word) 

        #Place an image as a label on the top right of the window
        self.label_image = QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(1000, 0, 300, 300))
        # Update image path using resource_path
        self.label_image.setPixmap(QPixmap(resource_path("images/1img.png")))
        self.label_image.setScaledContents(True)
        self.label_image.setObjectName("label_image")

        #Place a label on the extreme top right of the window to display the name of the player
        self.label_player_name = QLabel(self.centralwidget)
        #place the label relative to the top right corner and also wrap the text so that it always is completely visible regardless of the length of the text
        self.label_player_name.setGeometry(QtCore.QRect(1000, 0, 300, 20))
        self.label_player_name.setWordWrap(True)
        text1 = "Player: " + player_name
        self.label_player_name.setText(text1)
        self.label_player_name.setObjectName("label_player_name")

        self.retranslateUi(HangMan)
        HangMan.setCentralWidget(self.centralwidget)
        #Bind the resize event to the resizeEvent method
        self.centralwidget.resizeEvent = self.resizeEvent

    def retranslateUi(self, HangMan):
        HangMan.setWindowTitle("HangMan")
        self.label.setText("Word so far:")
        #place the text at 10,150
        self.label.move(10, 150)

    def resizeEvent(self, event):
        palette = self.centralwidget.palette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(self.background_image.scaled(
            event.size(), Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)))
        self.centralwidget.setPalette(palette)
        #also resize the label_image and label_player_name and also enlarge the image and font of text
        self.label_image.setGeometry(QtCore.QRect(event.size().width()-300, 0, 300, 300))
        self.label_player_name.setGeometry(QtCore.QRect(event.size().width()-150, 0, 300, 20))
        # Update image path using resource_path
        self.label_image.setPixmap(QPixmap(resource_path("images/1img.png")).scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.label_player_name.setFont(QFont('Arial', 10))

class HangMan_GUI(QMainWindow, Ui_HangMan):
    def __init__(self, player_name, difficulty, parent=None):
        super(HangMan_GUI, self).__init__(parent)
        self.setupUi(self, player_name)

        try:
            cred_data = get_firebase_credentials()
            if not cred_data:
                raise ValueError("Failed to decrypt Firebase credentials")
                
            cred = credentials.Certificate(cred_data)
            database_url = cred_data.get("databaseURL")
                
            if not database_url:
                raise ValueError("databaseURL not found in credentials")
                
            initialize_app(cred, {'databaseURL': database_url})
            self.db_ref = db.reference('words')
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to initialize Firebase: {str(e)}")
            self.close()
            return

        self.player_name = player_name
        self.difficulty = difficulty

        self.hangman_images = []
        try:
            for i in range(1, 9):
                image_path = resource_path(f"images/{i}img.png")
                pixmap = QPixmap(image_path)
                if pixmap.isNull():
                    QMessageBox.critical(self, "Error", f"Failed to load image: {image_path}")
                    self.close()
                    return
                self.hangman_images.append(pixmap)
            
            # Set initial image
            self.label_image.setPixmap(self.hangman_images[0])
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load images: {str(e)}")
            self.close()
            return

        self.connectButtons()
        self.button_grid_layout = QGridLayout()

        # Load word with error handling
        try:
            self.load_random_word_from_firebase()
            self.chosenWord = self.chosenWord if hasattr(self, 'chosenWord') else "hangman"  # Default fallback
            self.chosenMasked = self.maskWord()
            self.lives = 7
            self.display()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load word: {str(e)}")
            self.chosenWord = "hangman"  # Default word as fallback
            self.chosenMasked = self.maskWord()
            self.lives = 7
            self.display()

    def load_random_word_from_firebase(self):
        try:
            if self.difficulty == "easy":
                total_words = db.reference('total_words_easy').get() or 0
            elif self.difficulty == "medium":
                total_words = db.reference('total_words_medium').get() or 0
            elif self.difficulty == "hard":
                total_words = db.reference('total_words_hard').get() or 0
            else:
                total_words = 0  # Default to 0 if difficulty not recognized
            
            if total_words <= 0:
                self.chosenWord = "hangman"  # Default word if no words are available
                return
                
            random_number = random.randint(1, total_words)
            
            # Use orderByKey for better performance with the index
            if self.difficulty == "easy":
                self.chosenWord = db.reference('easy_words').child(str(random_number)).get()
            elif self.difficulty == "medium":
                self.chosenWord = db.reference('medium_words').child(str(random_number)).get()
            elif self.difficulty == "hard":
                self.chosenWord = db.reference('hard_words').child(str(random_number)).get()
            
            # If the word is None (possibly deleted), try again or use default
            if self.chosenWord is None:
                # Try one more time with a different number
                random_number = random.randint(1, total_words) 
                if self.difficulty == "easy":
                    self.chosenWord = db.reference('easy_words').child(str(random_number)).get()
                elif self.difficulty == "medium":
                    self.chosenWord = db.reference('medium_words').child(str(random_number)).get()
                elif self.difficulty == "hard":
                    self.chosenWord = db.reference('hard_words').child(str(random_number)).get()
                
                # If still None, use default
                if self.chosenWord is None:
                    self.chosenWord = "hangman"
        except Exception as e:
            print(f"Error loading word from Firebase: {str(e)}")
            self.chosenWord = "hangman"  # Fallback to default word

    def chooseWord(self):
        self.load_random_word_from_firebase()
        return self.chosenWord

    def maskWord(self):
        mask = "*" * len(self.chosenWord)
        return mask

    def giveup(self):
        self.textbox_lives.setText("You Lose! The word was: " + self.chosenWord)
        self.freeze()

    def display(self):
        self.textbox_word.setText(self.chosenMasked)
        self.textbox_lives.setText(str(self.lives))

    def button_pressed(self, letter):
        if letter in self.chosenWord:
            self.remakeMasked(letter)
            self.display()
            if self.chosenMasked == self.chosenWord:
                self.textbox_lives.setText("You Win!!!")
                self.freeze()
                self.restartOption()
        else:
            self.lives -= 1
            # Use pre-loaded images instead of loading on each button press
            try:
                if 0 <= self.lives < 7:
                    # Images are zero-indexed in our array, but 1-indexed in filenames
                    # For lives=6, we want image index 1 (2img.png)
                    image_index = 7 - self.lives  # Convert lives to correct image index
                    self.label_image.setPixmap(self.hangman_images[image_index])
            except Exception as e:
                # If there's any error updating the image, log it but don't crash
                print(f"Error updating image: {str(e)}")
                
            self.display()
            if self.lives == 0:
                self.textbox_lives.setText("You Lose! The word was: " + self.chosenWord)
                self.freeze()
                self.restartOption()

        self.buttons[letter].setEnabled(False)

    def remakeMasked(self, letter):
        newMasked = ""
        for i in range(len(self.chosenWord)):
            if self.chosenWord[i] == letter:
                newMasked += letter
            else:
                newMasked += self.chosenMasked[i]
        self.chosenMasked = newMasked

    def restartOption(self):
        self.pushButton.setText("Restart Game")
        self.pushButton.clicked.connect(self.chooseAnotherWord)

    def freeze(self):
        for button in self.buttons.values():
            button.setEnabled(False)

    def chooseAnotherWord(self):
        try:
            self.load_random_word_from_firebase()
            self.chosenMasked = self.maskWord()
            self.lives = 7
            # Use pre-loaded image
            self.label_image.setPixmap(self.hangman_images[0])
            self.display()
            for button in self.buttons.values():
                button.setEnabled(True)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load new word: {str(e)}")
            # Fallback to a default word if we can't load from Firebase
            self.chosenWord = "hangman"
            self.chosenMasked = self.maskWord()
            self.lives = 7
            self.label_image.setPixmap(self.hangman_images[0])
            self.display()
            for button in self.buttons.values():
                button.setEnabled(True)

    def connectButtons(self):
        for letter, button in self.buttons.items():
            button.clicked.connect(lambda _, l=letter: self.button_pressed(l))

        self.pushButton_2.clicked.connect(self.giveup)
        self.pushButton_add_word.clicked.connect(self.add_word)
        self.pushButton_remove_word.clicked.connect(self.remove_word)
        self.pushButton.clicked.connect(self.chooseAnotherWord)

    def keyPressEvent(self, event):
        key = event.text().lower()
        if key in self.buttons and self.buttons[key].isEnabled():
            self.button_pressed(key)
        elif event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            if event.key() == Qt.Key.Key_G:
                self.giveup()
            elif event.key() == Qt.Key.Key_R:
                self.chooseAnotherWord()

    def add_word(self):
        word, ok = QInputDialog.getText(self.centralwidget, "Add word", "Enter a word")
        
        if not ok:
            return
        if not word:
            QMessageBox.critical(self.centralwidget, "Error", "Please enter a word")
            return
        
        word = word.strip().lower()  # Normalize words to lowercase
        word_length = len(word)
        if word_length <= 4:
            difficulty = "easy"
        elif 5 <= word_length <= 8:
            difficulty = "medium"
        else:
            difficulty = "hard"
        
        word_list_ref = db.reference(f"{difficulty}_words")
        total_words_ref = db.reference(f"total_words_{difficulty}")

        total_words = total_words_ref.get() or 0
        
        # Check if word exists by using the index
        word_exists = False
        words_snapshot = word_list_ref.order_by_value().equal_to(word).get()
        if words_snapshot:
            word_exists = True
            
        if word_exists:
            QMessageBox.critical(self.centralwidget, "Error", "Word already exists")
            return

        empty_spaces_ref = db.reference("empty_spaces").child(difficulty)
        empty_spaces = empty_spaces_ref.get() or {}
        
        if empty_spaces:
            # Sort the empty indices to use the smallest one first
            empty_indices = sorted([int(key) for key in empty_spaces.keys()])
            if empty_indices:
                index = empty_indices[0]
                # Add the word to the previously empty slot
                word_list_ref.child(str(index)).set(word)
                # Remove the used empty space
                empty_spaces_ref.child(str(index)).remove()
                # Update the total word count
                total_words_ref.set(total_words + 1)
                QMessageBox.information(self.centralwidget, "Success", "Word added successfully")
                return

        # If no empty space found or word exists, append the word to the end
        word_list_ref.child(str(total_words + 1)).set(word)
        total_words_ref.set(total_words + 1)
        QMessageBox.information(self.centralwidget, "Success", "Word added successfully")

    def remove_word(self):
        current_word = self.chosenWord
        if not current_word:
            QMessageBox.warning(self.centralwidget, "Warning", "No word to remove")
            return
            
        current_word_length = len(current_word.strip())

        if current_word_length <= 4:
            difficulty = "easy"
        elif 5 <= current_word_length <= 8:
            difficulty = "medium"
        else:
            difficulty = "hard"

        # Find the word by its value using the index
        word_ref = db.reference(f"{difficulty}_words")
        words_snapshot = word_ref.order_by_value().equal_to(current_word).get()
        
        if not words_snapshot:
            QMessageBox.warning(self.centralwidget, "Warning", "Word not found in database")
            self.chooseAnotherWord()
            return
            
        # Get the first key where the value matches the current word
        word_key = list(words_snapshot.keys())[0]
        
        # Mark the position as empty
        db.reference("empty_spaces").child(difficulty).child(word_key).set(True)
        # Remove the word
        word_ref.child(word_key).remove()
        # Update the total word count
        total_words_ref = db.reference(f"total_words_{difficulty}")
        total_words = total_words_ref.get() or 0
        if total_words > 0:
            total_words_ref.set(total_words - 1)

        QMessageBox.information(self.centralwidget, "Success", "Word removed successfully")
        self.chooseAnotherWord()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    start_window = StartWindow()
    start_window.show()
    sys.exit(app.exec())  # Note: exec() not exec_() in PyQt6