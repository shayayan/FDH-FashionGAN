import os
import shutil
from tqdm import tqdm


# Source directory containing folders of images
source_directory = 'C:/Users/User/Desktop//scraping'

# Destination directory where you want to copy JPG files
destination_directory = 'C:/Users/User/Desktop/all_images'

# Function to count JPG files
def count_jpg_files(directory):
    jpg_count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.jpg'):
                jpg_count += 1
    return jpg_count

# Count total number of JPG files
total_files = count_jpg_files(source_directory)

# Create a tqdm instance to display a progress bar
with tqdm(total=total_files, desc='Copying Files', unit='file') as pbar:
    # Iterate through each folder in the source directory
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if file.lower().endswith('.jpg'):
                source_file_path = os.path.join(root, file)
                destination_file_path = os.path.join(destination_directory, file)
                shutil.copy(source_file_path, destination_file_path)
                pbar.update(1)  # Update progress bar after copying each file