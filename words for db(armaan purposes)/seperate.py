def update_text_file(file_path):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Add " to the start and ", to the end of each line and a new line after every comma
    updated_lines = ['"' + line.strip() + '",\n' for line in lines]

    # Write the updated contents back to the file
    with open(file_path, 'w') as file:
        file.writelines(updated_lines)
        
    # Categorize words based on length
    easy_words = []
    medium_words = []
    hard_words = []
    for line in lines:
        word = line.strip()
        if len(word) <= 5:
            easy_words.append(word)
        elif 6 <= len(word) <= 8:
            medium_words.append(word)
        else:
            hard_words.append(word)

    # Write words to respective files
    with open("easy_words.txt", 'w') as easy_file:
        easy_file.write("\n".join(easy_words))
    with open("medium_words.txt", 'w') as medium_file:
        medium_file.write("\n".join(medium_words))
    with open("hard_words.txt", 'w') as hard_file:
        hard_file.write("\n".join(hard_words))

# Replace 'words.txt' with your actual file name
file_name = 'words.txt'

try:
    update_text_file(file_name)
    print(f'File "{file_name}" has been successfully updated and categorized into easy, medium, and hard words.')
except FileNotFoundError:
    print(f'Error: File "{file_name}" not found.')
except Exception as e:
    print(f'An error occurred: {e}')
