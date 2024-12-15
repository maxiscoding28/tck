import os
import sys
import shutil

def move_file_to_directory(arg, file_path):
    # Get the path to the .tck directory in the home directory
    home_dir = os.path.expanduser("~")
    tck_dir = os.path.join(home_dir, '.tck')

    # Check if the directory exists inside .tck
    subdirectory = os.path.join(tck_dir, arg)
    if not os.path.exists(subdirectory):
        print(f"Error: Directory '{subdirectory}' does not exist.")
        sys.exit(1)

    # Check if the file exists at the provided file path
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        sys.exit(1)

    # Move the file to the subdirectory
    try:
        # Extract the file name from the file path
        file_name = os.path.basename(file_path)

        # Construct the destination path
        destination = os.path.join(subdirectory, file_name)

        # Move the file
        shutil.move(file_path, destination)
        print(f"File '{file_path}' moved to '{destination}'.")

    except Exception as e:
        print(f"Error: Could not move the file. {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python move_file.py <directory_name> <file_path>")
        sys.exit(1)

    directory_name = sys.argv[1]
    file_path = sys.argv[2]
    move_file_to_directory(directory_name, file_path)

