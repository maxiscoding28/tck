import os
import sys
import json

def create_tck_directory(directory_name, description):
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
    subdirectory = os.path.join(tck_dir, directory_name)
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

    # Create the 'meta.json' file with the description
    meta_file = os.path.join(subdirectory, 'meta.json')
    meta_data = {
        "description": description
    }
    with open(meta_file, 'w') as f:
        json.dump(meta_data, f, indent=4)

    print(f"Created file {meta_file} with description.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory_name> <description>")
        sys.exit(1)

    directory_name = sys.argv[1]
    description = sys.argv[2]
    create_tck_directory(directory_name, description)