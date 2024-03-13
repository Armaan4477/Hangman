import sys
import os
import random
from PyQt5.QtWidgets import QMessageBox
import firebase_admin
from firebase_admin import db,credentials
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HangMan(object):
    def setupUi(self, HangMan):
        HangMan.setObjectName("HangMan")
        HangMan.resize(1303, 600)
        self.centralwidget = QtWidgets.QWidget(HangMan)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 70, 1128, 388))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textbox_word = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.textbox_word.setEnabled(False)
        self.textbox_word.setObjectName("textbox_word")
        self.verticalLayout.addWidget(self.textbox_word)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        
        self.textbox_lives = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.textbox_lives.setEnabled(False)
        self.textbox_lives.setObjectName("textbox_lives")
        self.horizontalLayout_5.addWidget(self.textbox_lives)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_10 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_4.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_4.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_4.addWidget(self.pushButton_12)
        self.pushButton_13 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_4.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_4.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_4.addWidget(self.pushButton_15)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_16 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_3.addWidget(self.pushButton_16)
        self.pushButton_17 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout_3.addWidget(self.pushButton_17)
        self.pushButton_18 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_3.addWidget(self.pushButton_18)
        self.pushButton_19 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout_3.addWidget(self.pushButton_19)
        self.pushButton_20 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_20.setObjectName("pushButton_20")
        self.horizontalLayout_3.addWidget(self.pushButton_20)
        self.pushButton_21 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_21.setObjectName("pushButton_21")
        self.horizontalLayout_3.addWidget(self.pushButton_21)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_22 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_22.setObjectName("pushButton_22")
        self.horizontalLayout_2.addWidget(self.pushButton_22)
        self.pushButton_23 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_23.setObjectName("pushButton_23")
        self.horizontalLayout_2.addWidget(self.pushButton_23)
        self.pushButton_24 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_24.setObjectName("pushButton_24")
        self.horizontalLayout_2.addWidget(self.pushButton_24)
        self.pushButton_25 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_25.setObjectName("pushButton_25")
        self.horizontalLayout_2.addWidget(self.pushButton_25)
        self.pushButton_26 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_26.setObjectName("pushButton_26")
        self.horizontalLayout_2.addWidget(self.pushButton_26)
        self.pushButton_27 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_27.setObjectName("pushButton_27")
        self.horizontalLayout_2.addWidget(self.pushButton_27)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_28 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_28.setObjectName("pushButton_28")
        self.horizontalLayout.addWidget(self.pushButton_28)
        self.pushButton_29 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_29.setObjectName("pushButton_29")
        self.horizontalLayout.addWidget(self.pushButton_29)
        self.pushButton_30 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_30.setObjectName("pushButton_30")
        self.horizontalLayout.addWidget(self.pushButton_30)
        self.pushButton_31 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_31.setObjectName("pushButton_31")
        self.horizontalLayout.addWidget(self.pushButton_31)
        self.pushButton_32 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_32.setObjectName("pushButton_32")
        self.horizontalLayout.addWidget(self.pushButton_32)
        self.pushButton_33 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_33.setObjectName("pushButton_33")
        self.horizontalLayout.addWidget(self.pushButton_33)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_34 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_34.setObjectName("pushButton_34")
        self.horizontalLayout_6.addWidget(self.pushButton_34)
        self.pushButton_35 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_35.setObjectName("pushButton_35")
        self.horizontalLayout_6.addWidget(self.pushButton_35)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        HangMan.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HangMan)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1303, 30))
        self.menubar.setObjectName("menubar")
        HangMan.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HangMan)
        self.statusbar.setObjectName("statusbar")
        HangMan.setStatusBar(self.statusbar)
        # self.pushButton_add_word = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_add_word.setObjectName("pushButton_add_word")
        # self.pushButton_add_word.setText("Add word")
        # self.pushButton_add_word.clicked.connect(HangMan.add_word)
        # self.horizontalLayout.addWidget(self.pushButton_add_word)
        # Create a QHBoxLayout for the Add word button
        self.horizontalLayout_top = QtWidgets.QHBoxLayout()

        # Add a stretch to push the Add word button to the left
        self.horizontalLayout_top.addStretch(1)

        # Create the Add word button
        self.pushButton_add_word = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add_word.setObjectName("pushButton_add_word")
        self.pushButton_add_word.setText("Add word")
        self.pushButton_add_word.clicked.connect(HangMan.add_word)

        # Add the Add word button to the layout
        self.horizontalLayout_top.addWidget(self.pushButton_add_word)

        # Create the Remove word button
        self.pushButton_remove_word = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_remove_word.setObjectName("pushButton_remove_word")
        self.pushButton_remove_word.setText("Remove Current word")
        self.pushButton_remove_word.clicked.connect(HangMan.remove_word)

        # Add the Remove word button to the layout
        self.horizontalLayout_top.addWidget(self.pushButton_remove_word)

        # Add the layout to the verticalLayout
        self.verticalLayout.addLayout(self.horizontalLayout_top)


        self.retranslateUi(HangMan)
        QtCore.QMetaObject.connectSlotsByName(HangMan)

    def retranslateUi(self, HangMan):
        _translate = QtCore.QCoreApplication.translate
        HangMan.setWindowTitle(_translate("HangMan", "HangMan"))
        self.label.setText(_translate("HangMan", "Word so far:"))
        self.pushButton.setText(_translate("HangMan", "Choose some other word"))
        self.pushButton_2.setText(_translate("HangMan", "Give up"))
        self.label_2.setText(_translate("HangMan", "Remaining Lives"))
        self.pushButton_10.setText(_translate("HangMan", "a"))
        self.pushButton_11.setText(_translate("HangMan", "b"))
        self.pushButton_12.setText(_translate("HangMan", "c"))
        self.pushButton_13.setText(_translate("HangMan", "d"))
        self.pushButton_14.setText(_translate("HangMan", "e"))
        self.pushButton_15.setText(_translate("HangMan", "f"))
        self.pushButton_16.setText(_translate("HangMan", "g"))
        self.pushButton_17.setText(_translate("HangMan", "h"))
        self.pushButton_18.setText(_translate("HangMan", "i"))
        self.pushButton_19.setText(_translate("HangMan", "j"))
        self.pushButton_20.setText(_translate("HangMan", "k"))
        self.pushButton_21.setText(_translate("HangMan", "l"))
        self.pushButton_22.setText(_translate("HangMan", "m"))
        self.pushButton_23.setText(_translate("HangMan", "n"))
        self.pushButton_24.setText(_translate("HangMan", "o"))
        self.pushButton_25.setText(_translate("HangMan", "p"))
        self.pushButton_26.setText(_translate("HangMan", "q"))
        self.pushButton_27.setText(_translate("HangMan", "r"))
        self.pushButton_28.setText(_translate("HangMan", "s"))
        self.pushButton_29.setText(_translate("HangMan", "t"))
        self.pushButton_30.setText(_translate("HangMan", "u"))
        self.pushButton_31.setText(_translate("HangMan", "v"))
        self.pushButton_32.setText(_translate("HangMan", "w"))
        self.pushButton_33.setText(_translate("HangMan", "x"))
        self.pushButton_34.setText(_translate("HangMan", "y"))
        self.pushButton_35.setText(_translate("HangMan", "z"))


class HangMan_GUI(QtWidgets.QMainWindow, Ui_HangMan):
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
        #Generate a random number between 1 and 5008
        random_number = random.randint(1, db.reference('total_words').get())
        self.chosenWord = db.reference('words').child(str(random_number)).get()
        # words_snapshot = self.db_ref.get()
        # words_list = [word for word in words_snapshot if word]
        
        # if words_list:
        #     self.chosenWord = random.choice(words_list)
        # else:
        #     raise ValueError("No words available. Ensure the Firebase database has words.")


    # Choose a word for the game
    def chooseWord(self):
        self.load_random_word_from_firebase()
        return self.chosenWord

    # mask chosen word
    def maskWord(self):
        mask = ""
        for i in range(len(self.chosenWord)):
            mask += "*"
        return mask

    # what happens when the button "give up" is clicked.
    def giveup(self):
        self.textbox_lives.setText("You Lose! The word was: " + self.chosenWord)
        self.freeze()

    def display(self):
        self.textbox_word.setText(self.chosenMasked)
        self.textbox_lives.setText(str(self.lives)) 

    # game logic:
    def button_pressed(self, letter):
        
        if letter in self.chosenWord:
            self.remakeMasked(letter)
            self.display()
            # win check: 
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

    # change masked word to show letter once it has been correctly guessed
    def remakeMasked(self, letter):
        for i in range(len(self.chosenWord)):
            maskedSplit = []
            if self.chosenWord[i] == letter:
                maskedSplit.append(self.chosenMasked[ : i])
                maskedSplit.append(self.chosenMasked[i + 1 : ])
                self.chosenMasked = maskedSplit[0] + letter + maskedSplit[1]

    # restart game if needed
    def restartOption(self):
        self.pushButton.setText("Restart Game")
        self.pushButton.clicked.connect(self.chooseAnotherWord)

    # freeze game once won or lost
    def freeze(self):
        self.pushButton_2.setEnabled(False)
        self.pushButton_10.setEnabled(False)
        self.pushButton_11.setEnabled(False)
        self.pushButton_12.setEnabled(False)
        self.pushButton_13.setEnabled(False)
        self.pushButton_14.setEnabled(False)
        self.pushButton_15.setEnabled(False)
        self.pushButton_16.setEnabled(False)
        self.pushButton_17.setEnabled(False)
        self.pushButton_18.setEnabled(False)
        self.pushButton_19.setEnabled(False)
        self.pushButton_20.setEnabled(False)
        self.pushButton_21.setEnabled(False)
        self.pushButton_22.setEnabled(False)
        self.pushButton_23.setEnabled(False)
        self.pushButton_24.setEnabled(False)
        self.pushButton_25.setEnabled(False)
        self.pushButton_26.setEnabled(False)
        self.pushButton_27.setEnabled(False)
        self.pushButton_28.setEnabled(False)
        self.pushButton_29.setEnabled(False)
        self.pushButton_30.setEnabled(False)
        self.pushButton_31.setEnabled(False)
        self.pushButton_32.setEnabled(False)
        self.pushButton_33.setEnabled(False)
        self.pushButton_34.setEnabled(False)
        self.pushButton_35.setEnabled(False)

    # choose another word
    def chooseAnotherWord(self):
        self.load_random_word_from_firebase()
        self.chosenMasked = self.maskWord()
        self.lives = 10
        self.display()
        # Restore all buttons
        self.restore_buttons()

    def restore_buttons(self):
        for button in self.findChildren(QtWidgets.QPushButton):
            button.setEnabled(True)

    def connectButtons(self):
        self.pushButton_2.clicked.connect(self.giveup)
        self.pushButton.clicked.connect(self.chooseAnotherWord)
        self.pushButton_10.clicked.connect(self.a_press)
        self.pushButton_11.clicked.connect(self.b_press)
        self.pushButton_12.clicked.connect(self.c_press)
        self.pushButton_13.clicked.connect(self.d_press)
        self.pushButton_14.clicked.connect(self.e_press)
        self.pushButton_15.clicked.connect(self.f_press)
        self.pushButton_16.clicked.connect(self.g_press)
        self.pushButton_17.clicked.connect(self.h_press)
        self.pushButton_18.clicked.connect(self.i_press)
        self.pushButton_19.clicked.connect(self.j_press)
        self.pushButton_20.clicked.connect(self.k_press)
        self.pushButton_21.clicked.connect(self.l_press)
        self.pushButton_22.clicked.connect(self.m_press)
        self.pushButton_23.clicked.connect(self.n_press)
        self.pushButton_24.clicked.connect(self.o_press)
        self.pushButton_25.clicked.connect(self.p_press)
        self.pushButton_26.clicked.connect(self.q_press)
        self.pushButton_27.clicked.connect(self.r_press)
        self.pushButton_28.clicked.connect(self.s_press)
        self.pushButton_29.clicked.connect(self.t_press)
        self.pushButton_30.clicked.connect(self.u_press)
        self.pushButton_31.clicked.connect(self.v_press)
        self.pushButton_32.clicked.connect(self.w_press)
        self.pushButton_33.clicked.connect(self.x_press)
        self.pushButton_34.clicked.connect(self.y_press)
        self.pushButton_35.clicked.connect(self.z_press)

    def a_press(self):
        self.button_pressed('a')
        self.pushButton_10.setEnabled(False)
    def b_press(self):
        self.button_pressed('b')
        self.pushButton_11.setEnabled(False)
    def c_press(self):
        self.button_pressed('c')
        self.pushButton_12.setEnabled(False)
    def d_press(self):
        self.button_pressed('d')
        self.pushButton_13.setEnabled(False)
    def e_press(self):
        self.button_pressed('e')
        self.pushButton_14.setEnabled(False)
    def f_press(self):
        self.button_pressed('f')
        self.pushButton_15.setEnabled(False)
    def g_press(self):
        self.button_pressed('g')
        self.pushButton_16.setEnabled(False)
    def h_press(self):
        self.button_pressed('h')
        self.pushButton_17.setEnabled(False)
    def i_press(self):
        self.button_pressed('i')
        self.pushButton_18.setEnabled(False)
    def j_press(self):
        self.button_pressed('j')
        self.pushButton_19.setEnabled(False)
    def k_press(self):
        self.button_pressed('k')
        self.pushButton_20.setEnabled(False)
    def l_press(self):
        self.button_pressed('l')
        self.pushButton_21.setEnabled(False)
    def m_press(self):
        self.button_pressed('m')
        self.pushButton_22.setEnabled(False)
    def n_press(self):
        self.button_pressed('n')
        self.pushButton_23.setEnabled(False)
    def o_press(self):
        self.button_pressed('o')
        self.pushButton_24.setEnabled(False)
    def p_press(self):
        self.button_pressed('p')
        self.pushButton_25.setEnabled(False)
    def q_press(self):
        self.button_pressed('q')
        self.pushButton_26.setEnabled(False)
    def r_press(self):
        self.button_pressed('r')
        self.pushButton_27.setEnabled(False)
    def s_press(self):
        self.button_pressed('s')
        self.pushButton_28.setEnabled(False)
    def t_press(self):
        self.button_pressed('t')
        self.pushButton_29.setEnabled(False)
    def u_press(self):
        self.button_pressed('u')
        self.pushButton_30.setEnabled(False)
    def v_press(self):
        self.button_pressed('v')
        self.pushButton_31.setEnabled(False)
    def w_press(self):
        self.button_pressed('w')
        self.pushButton_32.setEnabled(False)
    def x_press(self):
        self.button_pressed('x')
        self.pushButton_33.setEnabled(False)
    def y_press(self):
        self.button_pressed('y')
        self.pushButton_34.setEnabled(False)
    def z_press(self):
        self.button_pressed('z')
        self.pushButton_35.setEnabled(False)
    
    def add_word(self):
        # Show a dialog to get the word
        word, ok = QtWidgets.QInputDialog.getText(self.centralwidget, "Add word", "Enter a word")
        
        # Check if the user clicked OK
        if not ok:
            return
        if word is None:
            QMessageBox.critical(self.centralwidget, "Error", "Please enter a word")
            return
        
        # # Fetch all words from the database at once
        # words_snapshot = db.reference("words").get()
        
        # # Check if the word already exists
        # if words_snapshot:
        #     if isinstance(words_snapshot, list):
        #         if word in words_snapshot:
        #             QMessageBox.critical(self.centralwidget, "Error", "Word already exists")
        #             return
        #     elif isinstance(words_snapshot, dict):
        #         if word in words_snapshot.values():
        #             QMessageBox.critical(self.centralwidget, "Error", "Word already exists")
        #             return
        try:
            word_index = db.reference("words").get().index(word)
            if word_index != -1:
                QMessageBox.critical(self.centralwidget, "Error", "Word already exists")
                return
        except ValueError:
            pass
        
        empty_spaces_ref = db.reference("empty_spaces")
        empty_spaces = empty_spaces_ref.get()

        # Check if there are available empty spaces
        if empty_spaces:
            # Get the first empty space key
            empty_space_key = next(iter(empty_spaces.keys()))

            # Remove the specific empty space key
            empty_spaces_ref.child(empty_space_key).delete()

            # Set the word in the database
            db.reference("words").child(empty_space_key).set(word)
            db.reference("total_words").set(db.reference("total_words").get() + 1)
        else:
            # If there are no available empty spaces, add the word at the end
            db.reference("words").child(str(db.reference("total_words").get())).set(word)

        # Indicate success
        QMessageBox.information(self.centralwidget, "Success", "Word added successfully")
        
    def remove_word(self):
        #Get the current word and its index
        current_word = self.chosenWord
        current_word_index = db.reference("words").get().index(current_word)
        db.reference("empty_spaces").child(str(current_word_index)).set(current_word)
        db.reference("words").child(str(current_word_index)).delete()
        db.reference("total_words").set(db.reference("total_words").get() - 1)
        # Indicate success
        QMessageBox.information(self.centralwidget, "Success", "Word removed successfully")
        self.chooseAnotherWord()
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = HangMan_GUI()
    form.show()
    app.exec()