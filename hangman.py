import sys
import random
from PyQt5.QtGui import QImage, QPixmap, QBrush, QPalette, QIcon
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QMessageBox, QInputDialog, QRadioButton
)
from PyQt5.QtCore import Qt
from firebase_admin import db, credentials, initialize_app
from PyQt5 import QtCore, QtWidgets

class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        StartWindow.setObjectName("StartWindow")
        StartWindow.resize(400, 300)
        self.centralwidget = QWidget(StartWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_window = StartWindow

        # Add a background image using QPixmap
        self.background_image = QPixmap("hangman_background.png")
        palette = self.centralwidget.palette()
        palette.setBrush(QPalette.Background, QBrush(self.background_image.scaled(
            StartWindow.size(), Qt.IgnoreAspectRatio)))
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
        _translate = QApplication.translate
        StartWindow.setWindowTitle(_translate("StartWindow", "Hangman Game"))
        self.start_button.setText(_translate("StartWindow", "Start Game"))

    def resizeEvent(self, event):
        palette = self.centralwidget.palette()
        palette.setBrush(QPalette.Background, QBrush(self.background_image.scaled(
            event.size(), Qt.IgnoreAspectRatio)))
        self.centralwidget.setPalette(palette)

    def start_game(self):
        player_name = self.textbox_name.text()
        if not player_name:
            QMessageBox.critical(self, "Error", "Please enter your name.")
            return

        if self.radio_easy.isChecked():
            difficulty = "easy"
        elif self.radio_medium.isChecked():
            difficulty = "medium"
        elif self.radio_hard.isChecked():
            difficulty = "hard"
        else:
            QMessageBox.critical(self, "Error", "Please select a difficulty level.")
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

    # def start_game(self):
    #     player_name = self.textbox_name.text()
    #     if not player_name:
    #         QMessageBox.critical(self, "Error", "Please enter your name.")
    #         return

    #     if self.radio_easy.isChecked():
    #         difficulty = "easy"
    #     elif self.radio_medium.isChecked():
    #         difficulty = "medium"
    #     elif self.radio_hard.isChecked():
    #         difficulty = "hard"
    #     else:
    #         QMessageBox.critical(self, "Error", "Please select a difficulty level.")
    #         return

    #     game_window = HangMan_GUI(player_name, difficulty)
    #     game_window.show()
    #     self.close()

class Ui_HangMan(object):
    def setupUi(self, HangMan):
        HangMan.setObjectName("HangMan")
        HangMan.resize(1303, 700)
        self.centralwidget = QWidget(HangMan)
        self.centralwidget.setObjectName("centralwidget")

        # Add a background image using QPixmap
        self.background_image = QPixmap("hangman_background_2.png")
        palette = self.centralwidget.palette()
        palette.setBrush(QPalette.Background, QBrush(self.background_image.scaled(
            HangMan.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)))  # Updated scaling and added SmoothTransformation
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

        self.button_grid_layout = QtWidgets.QGridLayout()
        self.button_grid_layout.setObjectName("button_grid_layout")
        self.verticalLayout.addLayout(self.button_grid_layout)

        row = 0
        col = 0
        for letter in "abcdefghijklmnopqrstuvwxyz":
            button = QPushButton(letter)
            button.setObjectName(f"pushButton_{letter}")
            button.setIcon(QIcon("letter_icon.png"))
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
        self.menubar = QtWidgets.QMenuBar(HangMan)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1303, 30))
        self.menubar.setObjectName("menubar")
        HangMan.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HangMan)
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
        self.label_image.setGeometry(QtCore.QRect(1000, 10, 300, 300))
        self.label_image.setPixmap(QPixmap("1img.png"))
        self.label_image.setScaledContents(True)
        self.label_image.setObjectName("label_image")

        self.retranslateUi(HangMan)
        HangMan.setCentralWidget(self.centralwidget)
        #Bind the resize event to the resizeEvent method
        self.centralwidget.resizeEvent = self.resizeEvent
        QtCore.QMetaObject.connectSlotsByName(HangMan)

    def retranslateUi(self, HangMan):
        _translate = QtCore.QCoreApplication.translate
        HangMan.setWindowTitle(_translate("HangMan", "HangMan"))
        self.label.setText(_translate("HangMan", "Word so far:"))
        #place the text at 10,150
        self.label.move(10, 150)

    def resizeEvent(self, event):
        print("Resizing")
        palette = self.centralwidget.palette()
        palette.setBrush(QPalette.Background, QBrush(self.background_image.scaled(
            event.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)))  # Updated scaling and added SmoothTransformation
        self.centralwidget.setPalette(palette)

class HangMan_GUI(QMainWindow, Ui_HangMan):
    def __init__(self, player_name, difficulty, parent=None):
        super(HangMan_GUI, self).__init__(parent)
        self.setupUi(self)

        cred = credentials.Certificate("credentials.json")
        initialize_app(cred, {'databaseURL': 'https://hangman-python.asia-southeast1.firebasedatabase.app/'})
        self.db_ref = db.reference('words')

        self.player_name = player_name
        self.difficulty = difficulty

        self.connectButtons()
        self.button_grid_layout = QtWidgets.QGridLayout()

        self.load_random_word_from_firebase()

        self.chosenWord = self.chooseWord()
        self.chosenMasked = self.maskWord()

        self.lives = 7

        self.display()

    def load_random_word_from_firebase(self):
        if self.difficulty == "easy":
            total_words = db.reference('total_words_easy').get()
        elif self.difficulty == "medium":
            total_words = db.reference('total_words_medium').get()
        elif self.difficulty == "hard":
            total_words = db.reference('total_words_hard').get()
        else:
            total_words = 0  # Default to 0 if difficulty not recognized
        
        random_number = random.randint(1, total_words)

        if self.difficulty == "easy":
            self.chosenWord = db.reference('easy_words').child(str(random_number)).get()
        elif self.difficulty == "medium":
            self.chosenWord = db.reference('medium_words').child(str(random_number)).get()
        elif self.difficulty == "hard":
            self.chosenWord = db.reference('hard_words').child(str(random_number)).get()

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
            # Update the image
            match self.lives:
                case 6:
                    self.label_image.setPixmap(QPixmap("2img.png"))
                case 5:
                    self.label_image.setPixmap(QPixmap("3img.png"))
                case 4:
                    self.label_image.setPixmap(QPixmap("4img.png"))
                case 3:
                    self.label_image.setPixmap(QPixmap("5img.png"))
                case 2:
                    self.label_image.setPixmap(QPixmap("6img.png"))
                case 1:
                    self.label_image.setPixmap(QPixmap("7img.png"))
                case 0:
                    self.label_image.setPixmap(QPixmap("8img.png"))
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
        self.load_random_word_from_firebase()
        self.chosenMasked = self.maskWord()
        self.lives = 7
        self.label_image.setPixmap(QPixmap("1img.png"))
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
        elif event.modifiers() == QtCore.Qt.ControlModifier:
            if event.key() == QtCore.Qt.Key_G:
                self.giveup()
            elif event.key() == QtCore.Qt.Key_R:
                self.chooseAnotherWord()

    def add_word(self):
        word, ok = QInputDialog.getText(self.centralwidget, "Add word", "Enter a word")
        
        if not ok:
            return
        if not word:
            QMessageBox.critical(self.centralwidget, "Error", "Please enter a word")
            return
        
        word = word.strip()
        word_length = len(word)
        if word_length <= 4:
            difficulty = "easy"
        elif 5 <= word_length <= 8:
            difficulty = "medium"
        else:
            difficulty = "hard"
        
        print(f"Word: {word}, Difficulty: {difficulty}")

        word_list_ref = db.reference(f"{difficulty}_words")
        total_words_ref = db.reference(f"total_words_{difficulty}")

        total_words = total_words_ref.get() or 0
        print(f"Total words: {total_words}")

        if word in word_list_ref.get():
            QMessageBox.critical(self.centralwidget, "Error", "Word already exists")
            return

        empty_spaces_ref = db.reference("empty_spaces")
        empty_spaces = empty_spaces_ref.get()
        print(f"Empty spaces: {empty_spaces}")

        if not word in word_list_ref.get():
            if empty_spaces and isinstance(empty_spaces, dict) and difficulty in empty_spaces:
                empty_indices = empty_spaces[difficulty]
                if empty_indices:
                    # Convert string keys to integers
                    empty_indices = [int(key) for key in empty_indices]
                    index = empty_indices.pop(0)
                    word_list_ref.child(str(index)).set(word)
                    total_words_ref.set(total_words + 1)
                    empty_spaces_ref.update({difficulty: empty_indices})
                    QMessageBox.information(self.centralwidget, "Success", "Word added successfully")
                    return

        # If no empty space found or word exists, append the word to the end
        word_list_ref.child(str(total_words + 1)).set(word)
        total_words_ref.set(total_words + 1)
        QMessageBox.information(self.centralwidget, "Success", "Word added successfully")

    def remove_word(self):
        current_word = self.chosenWord
        current_word_length = len(current_word.strip())

        if current_word_length <= 5:
            difficulty = "easy"
        elif 6 <= current_word_length <= 8:
            difficulty = "medium"
        else:
            difficulty = "hard"

        current_word_index = db.reference(f"{difficulty}_words").get().index(current_word)
        db.reference("empty_spaces").child(difficulty).child(str(current_word_index)).set(current_word)
        db.reference(f"{difficulty}_words").child(str(current_word_index)).delete()
        db.reference(f"total_words_{difficulty}").set(db.reference(f"total_words_{difficulty}").get() - 1)

        QMessageBox.information(self.centralwidget, "Success", "Word removed successfully")
        self.chooseAnotherWord()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    start_window = StartWindow()
    start_window.show()
    sys.exit(app.exec_())