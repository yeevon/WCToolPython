import sys
import os

#TODO: Create ccwc.bat file with create paths if it doesn't exit

def count(text_file):
    file_size_bytes = os.path.getsize(text_file)
    print(file_size_bytes, os.path.basename(text_file))


if __name__ == "__main__":

    valid_commands_list = [
        "-c"
    ]

    #Todo: build out --help function that displays valid commands to the user
    if sys.argv[1].lower() not in valid_commands_list:
        print("You entered an invalid argument")
    else:
        command = sys.argv[1].lower()
        file = sys.argv[2]

        if command == '-c':
            count(file)

