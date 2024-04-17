import sys
import os
import random
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QInputDialog
)
import firebase_admin
from firebase_admin import db, credentials
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HangMan(object):
    def setupUi(self, HangMan):
        HangMan.setObjectName("HangMan")
        HangMan.resize(1303, 600)
        self.centralwidget = QtWidgets.QWidget(HangMan)
        self.centralwidget.setObjectName("centralwidget")

        # Create vertical layout for central widget
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 70, 1128, 388))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # Label for displaying word
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        # Textbox for displaying word
        self.textbox_word = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.textbox_word.setEnabled(False)
        self.textbox_word.setObjectName("textbox_word")
        self.verticalLayout.addWidget(self.textbox_word)

        # Horizontal layout for buttons
        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.setObjectName("button_layout")

        # Add buttons
        self.buttons = {}
        for letter in "abcdefghijklmnopqrstuvwxyz":
            button = QPushButton(letter)
            button.setObjectName(f"pushButton_{letter}")
            self.buttons[letter] = button
            self.button_layout.addWidget(button)
        self.verticalLayout.addLayout(self.button_layout)

        # Button for choosing another word
        self.pushButton = QtWidgets.QPushButton("Choose some other word")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        # Button for giving up
        self.pushButton_2 = QtWidgets.QPushButton("Give up")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        # Horizontal layout for remaining lives
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel("Remaining Lives")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)

        # Textbox for displaying remaining lives
        self.textbox_lives = QtWidgets.QLineEdit()
        self.textbox_lives.setEnabled(False)
        self.textbox_lives.setObjectName("textbox_lives")
        self.horizontalLayout_5.addWidget(self.textbox_lives)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        # Add layout to central widget
        self.centralwidget.setLayout(self.verticalLayout)

        # Add menu bar and status bar
        HangMan.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HangMan)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1303, 30))
        self.menubar.setObjectName("menubar")
        HangMan.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HangMan)
        self.statusbar.setObjectName("statusbar")
        HangMan.setStatusBar(self.statusbar)

        # Add "Add word" and "Remove word" buttons
        self.pushButton_add_word = QtWidgets.QPushButton("Add word")
        self.pushButton_add_word.setObjectName("pushButton_add_word")
        self.verticalLayout.addWidget(self.pushButton_add_word)

        self.pushButton_remove_word = QtWidgets.QPushButton("Remove Current word")
        self.pushButton_remove_word.setObjectName("pushButton_remove_word")
        self.verticalLayout.addWidget(self.pushButton_remove_word)

        # Connect signals and slots
        self.retranslateUi(HangMan)
        QtCore.QMetaObject.connectSlotsByName(HangMan)

    def retranslateUi(self, HangMan):
        _translate = QtCore.QCoreApplication.translate
        HangMan.setWindowTitle(_translate("HangMan", "HangMan"))
        self.label.setText(_translate("HangMan", "Word so far:"))


class HangMan_GUI(QMainWindow, Ui_HangMan):
    def __init__(self, parent=None):
        super(HangMan_GUI, self).__init__(parent)
        self.setupUi(self)

        # Initialize Firebase
        cred = credentials.Certificate("credentials.json")
        firebase_admin.initialize_app(cred, {'databaseURL': 'https://hangman-python.asia-southeast1.firebasedatabase.app/'})
        self.db_ref = db.reference('words')

        self.connectButtons()

        # Fetch a random word from Firebase
        self.load_random_word_from_firebase()
         
        # Choose a word for the game and mask it
        self.chosenWord = self.chooseWord()  # Call chooseWord method
        self.chosenMasked = self.maskWord()  # Call maskWord method

        self.lives = 10

        # Display word and lives
        self.display()

    def load_random_word_from_firebase(self):
        # Generate a random number between 1 and the total number of words
        total_words = db.reference('total_words').get()
        random_number = random.randint(1, total_words)
        self.chosenWord = db.reference('words').child(str(random_number)).get()

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

    def remakeMasked(self, letter):
        maskedSplit = []
        for i in range(len(self.chosenWord)):
            if self.chosenWord[i] == letter:
                maskedSplit.append(self.chosenMasked[:i] + letter + self.chosenMasked[i+1:])
            else:
                maskedSplit.append(self.chosenMasked[i])
        self.chosenMasked = "".join(maskedSplit)

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

    def add_word(self):
        word, ok = QInputDialog.getText(self.centralwidget, "Add word", "Enter a word")
        
        if not ok:
            return
        if word is None:
            QMessageBox.critical(self.centralwidget, "Error", "Please enter a word")
            return
        
        try:
            word_index = db.reference("words").get().index(word)
            if word_index != -1:
                QMessageBox.critical(self.centralwidget, "Error", "Word already exists")
                return
        except ValueError:
            pass
        
        empty_spaces_ref = db.reference("empty_spaces")
        empty_spaces = empty_spaces_ref.get()

        if empty_spaces:
            empty_space_key = next(iter(empty_spaces.keys()))
            empty_spaces_ref.child(empty_space_key).delete()
            db.reference("words").child(empty_space_key).set(word)
            db.reference("total_words").set(db.reference("total_words").get() + 1)
        else:
            db.reference("words").child(str(db.reference("total_words").get())).set(word)

        QMessageBox.information(self.centralwidget, "Success", "Word added successfully")
        
    def remove_word(self):
        current_word = self.chosenWord
        current_word_index = db.reference("words").get().index(current_word)
        db.reference("empty_spaces").child(str(current_word_index)).set(current_word)
        db.reference("words").child(str(current_word_index)).delete()
        db.reference("total_words").set(db.reference("total_words").get() - 1)
        QMessageBox.information(self.centralwidget, "Success", "Word removed successfully")
        self.chooseAnotherWord()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = HangMan_GUI()
    form.show()
    sys.exit(app.exec_())
