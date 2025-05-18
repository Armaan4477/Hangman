# Hangman Game

A Python implementation of the classic Hangman game with a graphical user interface built using PyQt5 and Firebase Realtime Database for word storage.

## Screenshots
![Hangman Game Start Screen](images/hangman_screenshot_1.png)
    This is the start screen where players can enter their name and select a difficulty level.

![Hangman Game In-Game Screen](images/hangman_screenshot_2.png)
    This is the in-game screen where players can guess letters and see their progress.

## Features

- User-friendly graphical interface
- Multiple difficulty levels (Easy, Medium, Hard)
- Custom word management (add and remove words)
- Persistent word storage using Firebase
- Visual hangman progression
- Keyboard and mouse input support

## Prerequisites

- Python 3.11 or higher
- Firebase account
- Internet connection for database access

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Armaan4477/Hangman.git
   cd Hangman
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Firebase Setup

### 1. Create a Firebase Project

1. Go to the [Firebase Console](https://console.firebase.google.com/)
2. Click "Add project" and follow the setup wizard
3. Give your project a name (e.g., "Hangman Game")
4. Follow the prompts to complete the setup

### 2. Set up Realtime Database

1. In the Firebase Console, select your project
2. Click on "Realtime Database" in the left sidebar
3. Click "Create Database"
4. Start in test mode for development (You'll set up proper security rules later)
5. Choose a database location closest to your users

### 3. Import Database Structure

1. In the Realtime Database section, click the overflow menu (three dots) and select "Import JSON"
2. Upload the provided `hangman_DB-export.json` file
3. This will populate your database with the required structure and some initial words

### 4. Set Database Rules

1. In the Realtime Database section, click the "Rules" tab
2. Replace the existing rules with the contents of the provided `rules.txt` file
3. Click "Publish"

### 5. Generate Firebase Credentials

1. In the Firebase Console, go to Project Settings (gear icon)
2. Click on the "Service Accounts" tab
3. Click "Generate new private key"
4. Save the downloaded JSON file as `credentials.json` in your project directory
5. Open the `credentials.json` file and add the `databaseURL` field manually:

```json
{
  "type": "service_account",
  "project_id": "your-project-id",
  "private_key_id": "your-private-key-id",
  "private_key": "-----BEGIN PRIVATE KEY-----\nYour Private Key\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-xxxxx@your-project-id.iam.gserviceaccount.com",
  "client_id": "your-client-id",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-xxxxx%40your-project-id.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com",
  "databaseURL": "https://your-project-id-default-rtdb.firebaseio.com"
}
```

> **Important**: Replace `https://your-project-id-default-rtdb.firebaseio.com` with your actual Firebase Realtime Database URL, which you can find in the Realtime Database section of the Firebase Console.

## Running the Game

Execute the main Python script:

```bash
python hangman.py
```

## How to Play

1. Enter your name and select a difficulty level in the start screen
2. Click "Start Game" to begin
3. Guess letters by either:
   - Clicking on the letter buttons
   - Typing on your keyboard
4. You have 7 lives (incorrect guesses) before the game ends
5. Try to guess the word before running out of lives!

## Keyboard Shortcuts

- Type a letter to guess it
- `Ctrl+G` to give up the current game
- `Ctrl+R` to restart with a new word

## Word Management

- Click "Add word" to add your own words to the database
- Click "Remove Current word" to remove the current word from the database
- Words are automatically assigned to difficulty levels based on their length:
  - Easy: 4 letters or less
  - Medium: 5-8 letters
  - Hard: 9+ letters

## Project Structure

```
Hangman/
├── hangman.py          # Main game code
├── requirements.txt    # Python dependencies
├── credentials.json    # Firebase credentials (you must create this)
├── README.md           # This file
├── images/             # Game images
│   ├── hangman_background.png
│   ├── hangman_background_2.png
│   ├── letter_icon.png
│   ├── 1img.png        # Hangman state images
│   ├── 2img.png
│   └── ...
├── database_backup/
    ├── hangman_DB_export.json
    └── rules.txt

```

## Troubleshooting

- If you see a Firebase initialization error, check your credentials.json file and ensure the databaseURL is correct
- Make sure your Firebase Realtime Database has been initialized and is in the correct region
- Verify that all the required images are in the images/ directory

## License

This project is licensed under the MIT License - see the LICENSE file for details.
