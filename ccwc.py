import sys
import os

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
        count += len(line) + line.count("\n")
    return count

if __name__ == "__main__":

    command = 'default'
    #List of commands user can use
    valid_commands_list = [
        "-c",
        "-l",
        "-w",
        "-m",
        "-help",
        "default"
    ]

    # Get arguments being passed
    if len(sys.argv) > 3:
        print(">> You are passing to many arguments")
        print(">> Format: `ccwc -command filename`")
        print(">> For list of valid commands enter `ccwc -help`")
        sys.exit()
    elif len(sys.argv) == 3:
        command = sys.argv[1]
        file = sys.argv[2]
    else:
        file = sys.argv[1]


    if '-help' in sys.argv :
        print('''
>> List of valid commands:
    -c: bytes .. Returns the number of bytes in the file
    -l: lines .. Returns the number of lines in the file
    -w: words .. Returns the number of words in the file
    -m: characters .. Returns the number of characters in the file
    ''')
        sys.exit()

    # Check if user passed a valid argument
    if (command not in valid_commands_list) or not os.path.isfile(file):
        print("You entered an invalid argument")
        print("If you need assistance please run '-help' for list of commands")
    else:
        if command == '-c':
            print(get_bytes(file), file_name(file))
        elif command == '-l':
            print(count_lines(file), file_name(file))
        elif command == '-w':
            print(count_word(file), file_name(file))
        elif command == '-m':
            print(count_char(file), file_name(file))
        else:
            print(get_bytes(file), count_lines(file), count_word(file), file_name(file))