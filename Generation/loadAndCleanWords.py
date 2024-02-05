#     Copyright (C) 2022  Sumair Ijaz Hashmi - LUMS roll number: 24100004

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https:#www.gnu.org/licenses/>.


##### This creates the word list


import os

# load words as list
file_path_name = os.path.join(os.path.dirname(__file__), "5000-words.txt")
all_words = open(file_path_name, 'r')
all_words_str = all_words.read()
all_words_list = all_words_str.split('\n')

# remove last empty line if it is present
if all_words_list[-1] == '':
    all_words_list.remove(all_words_list[-1])

cleaned_words = []

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

hasNonAlphabet = False

# only insert those words with length >= 4
for word in all_words_list:
    hasNonAlphabet = False
    if len(word) >= 4:
        for i in range(len(word)):
            if word[i] not in alphabet:
                hasNonAlphabet = True
        if hasNonAlphabet == False:
            word = word.lower()
            cleaned_words.append(word)


# create new file of cleaned words
new_file = open("words.txt", 'w')
cleaned_words_str = ""
for i in range(len(cleaned_words)):
    cleaned_words_str += cleaned_words[i] + '\n'
new_file.write(cleaned_words_str)
new_file.close()

