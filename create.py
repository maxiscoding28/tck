import os
import sys

def create_tck_directory(arg):
    print("Test")
    # Get the path to the .tck directory in the home directory
    home_dir = os.path.expanduser("~")
    tck_dir = os.path.join(home_dir, '.tck')

    # Check if the .tck directory exists, if not, create it
    if not os.path.exists(tck_dir):
        print(f"Creating .tck directory at {tck_dir}...")
        os.makedirs(tck_dir)
    else:
        print(f".tck directory already exists at {tck_dir}.")

    # Create the subdirectory with the name provided in the argument
    subdirectory = os.path.join(tck_dir, arg)
    if os.path.exists(subdirectory):
        print(f"Error: Directory {subdirectory} already exists.")
        sys.exit(1)

    print(f"Creating subdirectory {subdirectory}...")
    os.makedirs(subdirectory)

    # Create the 'notes.md' file in the newly created subdirectory
    notes_file = os.path.join(subdirectory, 'notes.md')
    with open(notes_file, 'w') as f:
        f.write("# Notes\n\n")

    print(f"Created file {notes_file}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_name>")
        sys.exit(1)

    directory_name = sys.argv[1]
    create_tck_directory(directory_name)

