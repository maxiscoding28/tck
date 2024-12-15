import os
import sys
import subprocess

def open_directory_in_editor(arg):
    # Get the path to the .tck directory in the home directory
    home_dir = os.path.expanduser("~")
    tck_dir = os.path.join(home_dir, '.tck')

    # Check if the directory exists inside .tck
    subdirectory = os.path.join(tck_dir, arg)
    if not os.path.exists(subdirectory):
        print(f"Error: Directory {subdirectory} does not exist.")
        sys.exit(1)

    # Check if notes.md exists in the subdirectory
    notes_file = os.path.join(subdirectory, 'notes.md')
    if not os.path.exists(notes_file):
        print(f"Error: {notes_file} does not exist.")
        sys.exit(1)

    # Get the editor from the $EDITOR environment variable
    editor = os.getenv('EDITOR', None)
    if editor is None:
        print("Error: No editor specified in the $EDITOR environment variable.")
        sys.exit(1)

    # Open the directory in the specified editor
    print(f"Opening directory {subdirectory} in the editor {editor}...")

    try:
        # Open the folder in the editor specified by $EDITOR
        subprocess.run([editor, subdirectory], check=True)
    except FileNotFoundError:
        print(f"Error: The specified editor '{editor}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: Could not open the directory in the editor. {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python open_directory_in_editor.py <directory_name>")
        sys.exit(1)

    directory_name = sys.argv[1]
    open_directory_in_editor(directory_name)

