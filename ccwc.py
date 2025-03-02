import sys
import os

#TODO: Create ccwc.bat file with correct paths if it doesn't exit
#TODO: Create Py unit test

# Return file name
def file_name(text_file):
    return os.path.basename(text_file)

# get number of bytes in file
def get_bytes(text_file):
    file_size_bytes = os.path.getsize(text_file)
    return file_size_bytes

# returns all the lines in the file
def get_lines(text_file):
    # Got error reading file added encoding to fix this error:
    # UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 6673: character maps to <undefined>
    with open(text_file, 'r', encoding='UTF8') as f:
        lines = f.readlines()
    return lines

# counts number of lines in file
def count_lines(text_file):
    return len(get_lines(text_file))

# counts number of words in each line of the file
def count_word(text_file):
    count = 0
    for line in get_lines(text_file):
        words = line.split()
        count = count + len(words)
    return count

# counts number of characters in each line of the file
def count_char(text_file):
    count = 0
    for line in get_lines(text_file):
        for characters in line:
            count = count + len(characters)
    return count


if __name__ == "__main__":

    #List of commands user can use
    valid_commands_list = [
        "-c",
        "-l",
        "-w",
        "-m"
    ]

    #Todo: build out --help function that displays valid commands to the user

    # Get users argument and file
    command = sys.argv[1].lower()
    file = sys.argv[2]

    # Check if user passed a valid argument
    if command not in valid_commands_list:
        print("You entered an invalid argument")
    else:
        if command == '-c':
            print(get_bytes(file), file_name(file))
        elif command == '-l':
            print(count_lines(file), file_name(file))
        elif command == '-w':
            print(count_word(file), file_name(file))
        elif command == '-m':
            print(count_char(file), file_name(file))
