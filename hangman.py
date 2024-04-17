import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QMessageBox, QInputDialog, QRadioButton
)
from PyQt5.QtGui import QIcon
from firebase_admin import db, credentials, initialize_app
from PyQt5 import QtCore, QtWidgets

class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        StartWindow.setObjectName("StartWindow")
        StartWindow.resize(400, 300)
        self.centralwidget = QWidget(StartWindow)
        self.centralwidget.setObjectName("centralwidget")

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

        StartWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartWindow)
        QtCore.QMetaObject.connectSlotsByName(StartWindow)

    def retranslateUi(self, StartWindow):
        _translate = QtCore.QCoreApplication.translate
        StartWindow.setWindowTitle(_translate("StartWindow", "Hangman Game"))
        self.start_button.setText(_translate("StartWindow", "Start Game"))

class StartWindow(QMainWindow, Ui_StartWindow):
    def __init__(self, parent=None):
        super(StartWindow, self).__init__(parent)
        self.setupUi(self)

        self.start_button.clicked.connect(self.start_game)

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
        self.close()

class Ui_HangMan(object):
    def setupUi(self, HangMan):
        HangMan.setObjectName("HangMan")
        HangMan.resize(1303, 500)
        self.centralwidget = QWidget(HangMan)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 70, 1128, 388))
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

        self.retranslateUi(HangMan)
        QtCore.QMetaObject.connectSlotsByName(HangMan)

    def retranslateUi(self, HangMan):
        _translate = QtCore.QCoreApplication.translate
        HangMan.setWindowTitle(_translate("HangMan", "HangMan"))
        self.label.setText(_translate("HangMan", "Word so far:"))

class HangMan_GUI(QMainWindow, Ui_HangMan):
    def __init__(self, player_name, difficulty, parent=None):
        super(HangMan_GUI, self).__init__(parent)
        self.setupUi(self)

        cred = credentials.Certificate("credentials.json")
        initialize_app(cred, {'databaseURL': 'https://python-test-hangman.asia-southeast1.firebasedatabase.app/'})
        self.db_ref = db.reference('words')

        self.player_name = player_name
        self.difficulty = difficulty

        self.connectButtons()
        self.button_grid_layout = QtWidgets.QGridLayout()

        self.load_random_word_from_firebase()

        self.chosenWord = self.chooseWord()
        self.chosenMasked = self.maskWord()

        self.lives = 10

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
        self.lives = 10
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
        if word is None:
            QMessageBox.critical(self.centralwidget, "Error", "Please enter a word")
            return
        
        word_list_ref = db.reference(f"{self.difficulty}_words")
        total_words_ref = db.reference(f"total_words_{self.difficulty}")

        total_words = total_words_ref.get()
        if total_words is None:
            total_words = 0

        word_index = total_words + 1

        word_list_ref.child(str(word_index)).set(word)
        total_words_ref.set(total_words + 1)

        QMessageBox.information(self.centralwidget, "Success", "Word added successfully")
        
    def remove_word(self):
        current_word = self.chosenWord
        word_list_ref = db.reference(f"{self.difficulty}_words")
        total_words_ref = db.reference(f"total_words_{self.difficulty}")

        current_word_index = word_list_ref.get().index(current_word)
        word_list_ref.child(str(current_word_index)).delete()
        total_words_ref.set(total_words_ref.get() - 1)

        QMessageBox.information(self.centralwidget, "Success", "Word removed successfully")
        self.chooseAnotherWord()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    start_window = StartWindow()
    start_window.show()
    sys.exit(app.exec_())
