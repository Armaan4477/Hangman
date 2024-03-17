def update_text_file(file_path):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Add " to the start and ", to the end of each line and a new line after every comma
    updated_lines = ['"' + line.strip() + '",\n' for line in lines]

    # Write the updated contents back to the file
    with open(file_path, 'w') as file:
        file.writelines(updated_lines)

# Replace 'words.txt' with your actual file name
file_name = 'hard_words.txt'

try:
    update_text_file(file_name)
    print(f'File "{file_name}" has been successfully updated.')
except FileNotFoundError:
    print(f'Error: File "{file_name}" not found.')
except Exception as e:
    print(f'An error occurred: {e}')