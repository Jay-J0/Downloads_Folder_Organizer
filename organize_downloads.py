import os
import shutil
from pathlib import Path

# Get the home directory of the current user using Pathlib for clean cross-platform paths
HOME = Path.home()

# Path to the Downloads folder 
DOWNLOADS = HOME / "Downloads"

# Dictionary mapping destination folders to a list of file extensions
# Helps the program know where to move what based on file type
DESTINATIONS = {
    "Music": [".mp3", ".wav", ".flac"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Pictures": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".odt"],
}

# Function to move a single file based on its extension
def move_file(file_path):
    # Go through each folder and its associated extensions
    for folder, extensions in DESTINATIONS.items():
        # Check if the file's extension matches one in the current list
        if file_path.suffix.lower() in extensions:
            # Create the destination directory if it doesn't exist
            target_dir = HOME / folder
            target_dir.mkdir(exist_ok=True)

            # Move the file to the target directory
            shutil.move(str(file_path), str(target_dir / file_path.name))
            print(f"Moved {file_path.name} to {folder}")
            return  # Once moved, no need to keep checking
    # If the extension isn't in our list, we just skip it 
    print(f"No rule for {file_path.name}, skipping.")

# Main function to organize the entire Downloads folder
def organize_downloads():
    # Loop through each item in the Downloads directory
    for item in DOWNLOADS.iterdir():
        # Make sure we only process files, not folders
        if item.is_file():
            move_file(item)

# Python best practice: run the main function if this script is executed directly
if __name__ == "__main__":
    organize_downloads()

