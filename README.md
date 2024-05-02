
# Hangman Game 

## Introduction

The Hangman Game with Python, PyQt5, and Firebase Integration is a modern rendition of the classic word-guessing game, designed to offer an engaging and interactive gaming experience. Developed using Python, PyQt5, and Firebase technologies, this project brings together a blend of programming prowess and contemporary database management.

With PyQt5 as the framework for the graphical user interface (GUI), players can enjoy a visually appealing and intuitive interface, allowing seamless interaction with game elements such as masked words and letter selection buttons. Firebase integration serves as the backbone of the game, providing a dynamic repository of words for gameplay. This integration ensures a constantly evolving word pool, enriching the gaming experience with a diverse range of words across various categories.

## Features

- Start game screen
- Main game screen
- Interactive GUI
- Keybinds to all letters to play
- Ability to add or remove words from the database that's being used

## Setup Instructions for Specific Database

To run our project using your specific database, follow these steps:

1. **Clone the Project:**
   - Clone the project repository into your local directory using Git:
     ```
     git clone https://github.com/ChampionSamay1644/Sem_4_Mini_Project.git
     ```

2. **Create a Firebase Account and Project:**
   - Sign up for a Firebase account or log in if you already have one.
   - Create a new project in Firebase.

3. **Download Firebase Credentials:**
   - In your Firebase project settings, download the security key file.
   - Rename the downloaded file to `credentials.json` and copy it to the root directory of the cloned project.

4. **Set Up Firebase Realtime Database:**
   - Create a Realtime Database in your Firebase project.
   - Add all the words you require in the specific format
   - You can use the `example.json` to import into your realtime database for a basic start and add or remove words from there.

5. **Update Main File with Database Link:**
   - Open `main.py` in your preferred code editor.
   - Replace `"############"` at line 259 of the `Hangman.py` file with your Firebase Realtime Database URL.
     ```python
     cred = credentials.Certificate("credentials.json")
        initialize_app(cred, {'databaseURL': '############'}) #Replace ############ with your Firebase Realtime Database URL
        self.db_ref = db.reference('words')
     ```

6. **Install Required Modules:**
   - Ensure that Python 3.12 and pip are installed on your system, and their paths are properly defined.
   - Open a terminal in the project directory.
   - Install all the required modules listed in `requirements.txt` using pip:
     ```
     pip install -r requirements.txt
     ```

8. **Run the Project:**
   - Run the main Python file to start the application:
     ```
     python main.py
     ```

## Conclusion

In conclusion, Hangman remains a timeless favorite, blending simplicity with challenge and educational value. It fosters language skills and strategic thinking. With its enduring appeal and innovative design, Hangman stands as a testament to the power of classic entertainment in the digital era, bringing joy.
