import os
import json

def list_directories_in_tck():
    # Get the path to the .tck directory in the home directory
    home_dir = os.path.expanduser("~")
    tck_dir = os.path.join(home_dir, '.tck')

    # Check if the .tck directory exists
    if not os.path.exists(tck_dir):
        print(f"Error: .tck directory does not exist in {home_dir}.")
        return

    # List all subdirectories in .tck
    directories = [d for d in os.listdir(tck_dir) if os.path.isdir(os.path.join(tck_dir, d))]

    # Check if there are any subdirectories
    if not directories:
        print(f"No subdirectories found in {tck_dir}.")
    else:
        print(f"Subdirectories in {tck_dir}:")
        for directory in directories:
            subdirectory_path = os.path.join(tck_dir, directory)
            meta_file_path = os.path.join(subdirectory_path, 'meta.json')
            
            # Try to read the description from meta.json
            description = "No description found."
            if os.path.exists(meta_file_path):
                try:
                    with open(meta_file_path, 'r') as meta_file:
                        meta_data = json.load(meta_file)
                        description = meta_data.get("description", "No description found.")
                except (json.JSONDecodeError, IOError) as e:
                    description = f"Error reading meta.json: {e}"
            
            print(f"- {directory}: {description}")

if __name__ == "__main__":
    list_directories_in_tck()