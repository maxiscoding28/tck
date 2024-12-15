import os

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
            print(f"- {directory}")

if __name__ == "__main__":
    list_directories_in_tck()

